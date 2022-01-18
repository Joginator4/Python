import math


class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__x = x
        self.__y = y
        

    def getx(self):
        return self.__x

        

    def gety(self):
        return self.__y

    def distance_from_xy(self, x, y):
        return math.hypot(abs(self.__x - x), abs(self.__y - y))

    def distance_from_point(self, point):
        return self.distance_from_xy(point.getx(), point.gety())
        
# test= Point(2,2)
# print(test.getx())
# print(test.gety())
# print(test.distance_from_xy(1,1))

        

point1 = Point(0.0, 0.0)
point2 = Point(1.0, 1.0)
print(point2.distance_from_xy(2, 0))
print(point1.distance_from_point(point2))
