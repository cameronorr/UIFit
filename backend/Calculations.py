import math


class Calculations:

    def __init__(self, H):
        self.height = H
        #self.inches_pixel_midpoint = 0
        self.inches_pixel = 0

    def calculateInchesPerPixel(self, points):
        if len(points) < 1:
            return 0, 0
        midpoint_ankle = (points[13][0]+points[14][0])/2

        distance_head_ankles = math.sqrt((points[0][0] - midpoint_ankle)**(2) + (points[0][1] - points[13][1])**(2))
        distance_head_ankles_y = math.sqrt((points[0][1] - max(points[13][1], points[14][1]))**(2))

        #self.inches_pixel = self.height/distance_head_ankles
        self.inches_pixel = self.height/distance_head_ankles_y

    #def getInchesMidPoint(self):
    #    return self.inches_pixel_midpoint

    def getInchesPerPixel(self):
        return self.inches_pixel

    def getDistanceInInches(self, point1, point2):
        if isinstance(point1, int or float) or isinstance(point2, int or float):
            return math.sqrt((point1 - point2)**2) * self.inches_pixel
        return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2) * self.inches_pixel

    def getDistance(self, point1, point2):
        if isinstance(point1, int or float) or isinstance(point2, int or float):
            return math.sqrt((point1 - point2)**2)
        return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

