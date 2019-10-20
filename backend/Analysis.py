from Measurements import Measurements
import math

class Analysis:

    def __init__(self, company, gender, clothing, H, frontView=None, backView=None, bentArmsView=None):
        self.mes = Measurements(H, frontView, bentArmsView, backView)
        self.company = company
        self.gender = gender
        self.clothing = clothing
        self.errorCalc = 0
        self.rating = ''
        self.Fit = []

    def calcShortSleeveSuccess(self):
        U_shirtlen = self.mes.getShoulderHip()
        U_shoulderWidth = self.mes.getShoulderWidth()
        U_rightSleeve = self.mes.getRightShoulderElbow()
        U_leftSleeve = self.mes.getLeftShoulderElbow()

        I_shirtlen = 24.875
        I_shoulderWidth = 18.75
        I_sleeveRatio = 5

        shirtLenError = abs(U_shirtlen - I_shirtlen) / I_shirtlen
        shoulderWidthError = abs(U_shoulderWidth - I_shoulderWidth) / I_shoulderWidth

        if shirtLenError < 0.1:
            self.Fit.append('Length of shirt is good')
        elif shirtLenError < 0.2:
            self.Fit.append('Length of shirt is decent')
        else:
            self.Fit.append('Length of shirt is bad')

        if shoulderWidthError < 0.1:
            self.Fit.append('Shoulders are well-fitted')
        elif shoulderWidthError < 0.2:
            self.Fit.append('Shoulders have a decent fit')
        else:
            self.Fit.append('Shoulders are not well-fitted')
        # rightSleeveError = I_sleeveRatio / U_rightSleeve
        # print(rightSleeveError)
        # leftSleeveError = I_sleeveRatio / U_leftSleeve
        # print(leftSleeveError)
        self.errorCalc = shirtLenError + shoulderWidthError

    def calcLongSleeveSuccess(self):
        U_shirtlen = self.mes.getShoulderHip()
        U_shoulderWidth = self.mes.getShoulderWidth()
        U_rightArm = self.mes.getRightShoulderElbow() + self.mes.getRightElbowWrist()
        U_leftArm = self.mes.getLeftShoulderElbow() + self.mes.getLeftElbowWrist()

        I_shirtlen = 24.875
        I_shoulderWidth = 18.75
        I_LongSleeve = 32.5

        shirtLenError = abs(U_shirtlen - I_shirtlen) / I_shirtlen
        shoulderWidthError = (abs(U_shoulderWidth - I_shoulderWidth)) / I_shoulderWidth
        longSleeveError = (abs(max(U_rightArm, U_leftArm) - I_LongSleeve)) / I_LongSleeve

        self.errorCalc = shirtLenError + shoulderWidthError + longSleeveError

    def calcJeansSuccess(self):
        U_rightJean = self.mes.getRightHipAnkle()
        U_leftJean = self.mes.getLeftHipAnkle()
        U_hipWidth = self.mes.getHipWidth()

        I_hipWidth = 31
        I_jeanLen = 10

        jeanError = (abs(max(U_rightJean, U_leftJean) - I_jeanLen)) / I_jeanLen
        HipError = (abs(U_hipWidth - I_hipWidth)) / I_hipWidth

        print(jeanError)
        print(HipError)

        self.errorCalc = jeanError + HipError

    def getCalcError(self):
        if self.errorCalc < 0.1:
            return 'Well-Fitted'
        elif self.errorCalc < 0.15:
            return 'Fitted'
        elif self.errorCalc < 0.2:
            return 'Adequate'
        elif self.errorCalc < 0.35:
            return 'Loose'
        else:
            return 'Very Loose'

    def getFit(self):
        return self.Fit
