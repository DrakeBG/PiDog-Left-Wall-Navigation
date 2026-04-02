class Point:
    def __init__(self, xcoord, ycoord):
        self.xcoord = xcoord
        self.ycoord = ycoord

    def dist_from_point (self, secondpoint):
        dist = ( (self.xcoord - secondpoint.xcoord)**2 + (self.ycoord - secondpoint.ycoord)**2 ) **0.5
        return dist


point1 = Point (5,7)
point2 = Point (3,8)
point3 = Point(0,0)

distance = point1.dist_from_point(point2)
print (distance)

distance = point1.dist_from_point(point3)
print (distance)