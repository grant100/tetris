from Shapes import Shapes
import math
class ZShape(Shapes):
    def __init__(self):
        self.origin    = []
        self.point_1   = []
        self.point_2   = []
        self.point_3   = []
        self.angle     = math.radians(90)
        self.generate()
        self.points    = [self.point_1,self.origin,self.point_2,self.point_3]
        Shapes.__init__(self,self.origin,self.points,self.angle)
    def rotate(self):
        _points = super(ZShape,self).rotate();
        self.angle = self.angle * -1;
        return _points

    def generate(self):
        line = line();
        self.origin  = line.origin
        self.point_1 = line.point_1
        if line.direction > 0:
           #vertical alignment
           
   
class ZShapeR(Shapes):
    def __init__(self):
        self.type = 0
#        self.origin  = [4,4]
#        self.point_1 = [3,4]
#        self.point_2 = [4,5]
#        self.point_3 = [5,5]
#        self.points    = [self.point_1,self.origin,self.point_2,self.point_3]
#        self.angle   = math.radians(90);
        ZShape.__init__(self)


class ZShapeL(Shapes):
    def __init__(self):
        self.type = 1
#        self.origin  = [4,4]
#        self.point_1 = [3,4]
#        self.point_2 = [4,3]
#        self.point_3 = [5,3]
#        self.points    = [self.point_1,self.origin,self.point_2,self.point_3]
#        self.angle   = math.radians(90);
        ZShape.__init__(self)
