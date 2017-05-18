from Line import Line
from LRectangle import LRectangleR
from LRectangle import LRectangleL
from Square import Square
from Triangle import Triangle
from ZShape import ZShapeR
from ZShape import ZShapeL
from random import randint
import threading
import time

class ShapesWrapper():
      def __init__(self):
          self.shiftIndex = 0
          self.shape = []
          self.getNewObject()
          self.exit = False

      def getNewObject(self):
          val = randint(0,6);
          o   = [Line(),LRectangleL(),LRectangleR(),Triangle(),Square(),ZShapeL(),ZShapeR()]
          self.shape = o[val]

      def shift(self):
          if not self.exit:
             if self.shiftIndex > 7:
                self.shiftIndex = 0
                self.getNewObject()
             self.shape.shiftDown()
             self.shiftIndex+=1
             threading.Timer(1, self.shift).start()

      def start(self):
          self.shift()
          while not self.exit:
#               self.shape.rotate();
                self.shape.draw()
                time.sleep(.2)
#      def getNewObject(self):
#         val = randint(0,6);
#          obj = [Line(),LRectangleL(),LRectangleR(),Triangle(),Square(),ZShapeL(),ZShapeR()]
#         return obj[val]