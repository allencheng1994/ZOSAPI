from ZOSCOM import *
import sys, os

class ZOSMFE(object):
    def __init__(self, TheMFE, startIndex = 1):
        self.operandCounter = startIndex
        self.__TheMFE = TheMFE
    
    def addOperandEFFL(self, Weight, WaveIndex):
        self.operandCounter += 1
        setOperand = self.__TheMFE.InsertNewOperandAt(self.operandCounter)
        setOperand.ChangeType(constants.MeritOperandType_EFFL)
        setOperand.Weight = Weight
        setOperand.GetOperandCell(3).IntegerValue = WaveIndex

    def addOperandTTHI(self, Weight, Surface1, Surface2):
        self.operandCounter += 1
        setOperand = self.__TheMFE.InsertNewOperandAt(self.operandCounter)
        setOperand.ChangeType(constants.MeritOperandType_TTHI)
        setOperand.Weight = Weight
        setOperand.GetOperandCell(2).IntegerValue = Surface1
        setOperand.GetOperandCell(3).IntegerValue = Surface2

    def addOperandRAID(self, Weight, Surface, WaveIndex, Hx, Hy, Px, Py):
        self.operandCounter += 1
        setOperand = self.__TheMFE.InsertNewOperandAt(self.operandCounter)
        setOperand.ChangeType(constants.MeritOperandType_RAID)
        setOperand.Weight = Weight
        setOperand.GetOperandCell(2).IntegerValue = Surface
        setOperand.GetOperandCell(3).IntegerValue = WaveIndex
        setOperand.GetOperandCell(4).DoubleValue = Hx
        setOperand.GetOperandCell(5).DoubleValue = Hy
        setOperand.GetOperandCell(6).DoubleValue = Px
        setOperand.GetOperandCell(7).DoubleValue = Py

    def addOperandRELI(self, Weight, Sample, WaveIndex, Field, PolFlag):
        self.operandCounter += 1
        setOperand = self.__TheMFE.InsertNewOperandAt(self.operandCounter)
        setOperand.ChangeType(constants.MeritOperandType_RELI)
        setOperand.Weight = Weight
        setOperand.GetOperandCell(2).IntegerValue = Sample
        setOperand.GetOperandCell(3).IntegerValue = WaveIndex
        setOperand.GetOperandCell(4).IntegerValue = Field
        setOperand.GetOperandCell(5).IntegerValue = PolFlag

    def addOperandMTFS(self, Weight, Sample, WaveIndex, Field, Frequency):
        self.operandCounter += 1
        setOperand = self.__TheMFE.InsertNewOperandAt(self.operandCounter)
        setOperand.ChangeType(constants.MeritOperandType_MTFS)
        setOperand.Weight = Weight
        setOperand.GetOperandCell(2).IntegerValue = Sample
        setOperand.GetOperandCell(3).IntegerValue = WaveIndex
        setOperand.GetOperandCell(4).IntegerValue = Field
        setOperand.GetOperandCell(5).DoubleValue = Frequency

    def addOperandMTFT(self, Weight, Sample, WaveIndex, Field, Frequency):
        self.operandCounter += 1
        setOperand = self.__TheMFE.InsertNewOperandAt(self.operandCounter)
        setOperand.ChangeType(constants.MeritOperandType_MTFT)
        setOperand.Weight = Weight
        setOperand.GetOperandCell(2).IntegerValue = Sample
        setOperand.GetOperandCell(3).IntegerValue = WaveIndex
        setOperand.GetOperandCell(4).IntegerValue = Field
        setOperand.GetOperandCell(5).DoubleValue = Frequency

    def removeOperand(self, startOperandIndex, endOperandIndex = -1):
        if endOperandIndex == -1:
            endOperandIndex = startOperandIndex
        self.__TheMFE.RemoveOperandsAt(startOperandIndex, endOperandIndex)

    def getOperandValueAt(self, OpIdx):
        return self.__TheMFE.GetOperandAt(OpIdx).Value

    def removeAllOperands(self):
        self.__TheMFE.RemoveOperandsAt(1, self.__TheMFE.NumberOfOperands)

    def save(self, mf_filename):
        self.__TheMFE.SaveMeritFunction(mf_filename)

    def load(self, mf_filename):
        self.__TheMFE.LoadMeritFunction(mf_filename)
    
    def calculate(self):
        self.__TheMFE.CalculateMeritFunction()
