from .calculations import Calculations
from .openpose_model import *
import math

class Measurements:

    def __init__(self, H, frontView="", bentArmsView="", backView=""):

        self.calc = Calculations(H)
        self.shoulder_width = 0
        self.right_shoulder_elbow = 0
        self.right_elbow_wrist = 0
        self.left_shoulder_elbow = 0
        self.left_elbow_wrist = 0
        self.right_shoulder_wrist = 0
        self.left_shoulder_wrist = 0
        self.shoulder_hip = 0
        self.right_hip_ankle = 0
        self.left_hip_ankle = 0
        self.right_hip_knee = 0
        self.left_hip_knee = 0
        self.hip_ankle_max = 0
        self.chest_point = (0, 0)
        self.model = openpose_model.general_pose_model("", mode="MPI")
        self.inchesPerPixel = 0
        self.points = None


        if frontView != "":
            self.__calculateMeasurementsFromFrontView(frontView)
            self.inchesPerPixel = self.calc.getInchesPerPixel()

        if bentArmsView != "":
            self.__calculateMeasurementsFromBentArmsView(bentArmsView)

        if backView != "":
            self.__calculateMeasurementsFromBackView(backView)

    def __calculateMeasurementsFromFrontView(self, path):
        res_points = self.model.predict(path)
        self.calc.calculateInchesPerPixel(res_points)
        self.shoulder_hip = self.calc.getDistanceInInches(min(res_points[2][1], res_points[5][1]),
                                                          min(res_points[8][1], res_points[11][1]))
        self.points = res_points
        #self.model.vis_pose(path, res_points)


    def __calculateMeasurementsFromBentArmsView(self, path):
        res_points = self.model.predict(path)
        self.calc.calculateInchesPerPixel(res_points)
        self.right_shoulder_elbow = self.calc.getDistanceInInches(res_points[2], res_points[3])
        self.right_elbow_wrist = self.calc.getDistanceInInches(res_points[3], res_points[4])
        self.right_shoulder_wrist = self.calc.getDistanceInInches(res_points[2], res_points[4])
        self.left_shoulder_elbow = self.calc.getDistanceInInches(res_points[5], res_points[6])
        self.left_elbow_wrist = self.calc.getDistanceInInches(res_points[6], res_points[7])
        self.left_shoulder_wrist = self.calc.getDistanceInInches(res_points[5], res_points[7])
        self.right_hip_ankle = self.calc.getDistanceInInches(res_points[8], res_points[10])
        self.left_hip_ankle = self.calc.getDistanceInInches(res_points[11], res_points[13])
        self.right_hip_knee = self.calc.getDistanceInInches(res_points[8], res_points[9])
        self.left_hip_knee = self.calc.getDistanceInInches(res_points[11], res_points[12])
        self.chest_point = res_points[14]

        self.hip_ankle_max = self.calc.getDistanceInInches((res_points[8][1]+res_points[11][1])/2,
                                                           max(res_points[10][1], res_points[13][1]))
        #self.model.vis_pose(path, res_points)


    def __calculateMeasurementsFromBackView(self, path):
        res_points = self.model.predict(path)
        self.calc.calculateInchesPerPixel(res_points)
        self.shoulder_width = self.calc.getDistanceInInches(res_points[2], res_points[5])
        #self.model.vis_pose(path, res_points)
