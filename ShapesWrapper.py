from Line import Line
from LRectangle import LRectangleR
from LRectangle import LRectangleL
from Square import Square
from Triangle import Triangle
from ZShape import ZShapeR
from ZShape import ZShapeL
from random import randint
from Board import Board
import threading
import time
height = 32
class ShapesWrapper():
      def __init__(self, observer):
          self.shiftIndex = 0
          self.shape = []
	  self.board = Board()
          self.getNewObject()
          self.exit = False
	  self.observer = observer
	  self.speed = .2

      def getNewObject(self):
          val = randint(0,6);
          o   = [Line(),LRectangleL(),LRectangleR(),Triangle(),Square(),ZShapeL(),ZShapeR()]
          self.shape = o[val]
          self.shape.setBoard(self.board)

      def shift(self):
          if not self.exit:
             if self.shiftIndex > height - 1:
                self.shiftIndex = 0
                self.getNewObject()
#		self.speed = self.speed - .005
#             self.board.detect(self.shape);
             self.shape.shiftDown(self)
#	     self.speed = self.speed - .01
             threading.Timer(.1, self.shift).start()

      def start(self):
          self.shift()

