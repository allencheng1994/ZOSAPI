from win32com.client import CastTo, constants

class ZOSMFE(object):
    def __init__(self, TheSystem, startIndex = 1):
        self.__operandCounter = startIndex
        self.__TheMFE = TheSystem.MFE
    
    def addOperandTOTR(self, Weight = 0, Target = 0):
        self.__operandCounter += 1
        setOperand = self.__TheMFE.InsertNewOperandAt(self.__operandCounter)
        setOperand.ChangeType(constants.MeritOperandType_TOTR)
        setOperand.Weight = Weight
        setOperand.Target = Target

    def addOperandWFNO(self, Weight = 0, Target = 0):
        self.__operandCounter += 1
        setOperand = self.__TheMFE.InsertNewOperandAt(self.__operandCounter)
        setOperand.ChangeType(constants.MeritOperandType_WFNO)
        setOperand.Weight = Weight
        setOperand.Target = Target

    def addOperandCONF(self, config):
        self.__operandCounter += 1
        setOperand = self.__TheMFE.InsertNewOperandAt(self.__operandCounter)
        setOperand.ChangeType(constants.MeritOperandType_CONF)
        setOperand.GetOperandCell(2).IntegerValue = config

    def addOperandEFFL(self, Weight, WaveIndex):
        self.__operandCounter += 1
        setOperand = self.__TheMFE.InsertNewOperandAt(self.__operandCounter)
        setOperand.ChangeType(constants.MeritOperandType_EFFL)
        setOperand.Weight = Weight
        setOperand.GetOperandCell(3).IntegerValue = WaveIndex

    def addOperandTTHI(self, Weight, Surface1, Surface2):
        self.__operandCounter += 1
        setOperand = self.__TheMFE.InsertNewOperandAt(self.__operandCounter)
        setOperand.ChangeType(constants.MeritOperandType_TTHI)
        setOperand.Weight = Weight
        setOperand.GetOperandCell(2).IntegerValue = Surface1
        setOperand.GetOperandCell(3).IntegerValue = Surface2

    def addOperandCTVA(self, Weight, Surface):
        self.__operandCounter += 1
        setOperand = self.__TheMFE.InsertNewOperandAt(self.__operandCounter)
        setOperand.ChangeType(constants.MeritOperandType_CTVA)
        setOperand.Weight = Weight
        setOperand.GetOperandCell(2).IntegerValue = Surface

    def addOperandETVA(self, Weight, Surface, Code = 1):
        self.__operandCounter += 1
        setOperand = self.__TheMFE.InsertNewOperandAt(self.__operandCounter)
        setOperand.ChangeType(constants.MeritOperandType_ETVA)
        setOperand.Weight = Weight
        setOperand.GetOperandCell(2).IntegerValue = Surface
        setOperand.GetOperandCell(3).IntegerValue = Code

    def addOperandRAID(self, Weight, Surface, WaveIndex = 0, Hx = 0, Hy = 0, Px = 0, Py = 0):
        self.__operandCounter += 1
        setOperand = self.__TheMFE.InsertNewOperandAt(self.__operandCounter)
        setOperand.ChangeType(constants.MeritOperandType_RAID)
        setOperand.Weight = Weight
        setOperand.GetOperandCell(2).IntegerValue = Surface
        setOperand.GetOperandCell(3).IntegerValue = WaveIndex
        setOperand.GetOperandCell(4).DoubleValue = Hx
        setOperand.GetOperandCell(5).DoubleValue = Hy
        setOperand.GetOperandCell(6).DoubleValue = Px
        setOperand.GetOperandCell(7).DoubleValue = Py

    def addOperandRELI(self, Weight, Sample, WaveIndex, Field = 11, PolFlag = 1):
        self.__operandCounter += 1
        setOperand = self.__TheMFE.InsertNewOperandAt(self.__operandCounter)
        setOperand.ChangeType(constants.MeritOperandType_RELI)
        setOperand.Weight = Weight
        setOperand.GetOperandCell(2).IntegerValue = Sample
        setOperand.GetOperandCell(3).IntegerValue = WaveIndex
        setOperand.GetOperandCell(4).IntegerValue = Field
        setOperand.GetOperandCell(5).IntegerValue = PolFlag

    def addOperandDISG(self, Weight, Field, WaveIndex, Hx = 0, Hy = 0, Px = 0, Py = 0):
        self.__operandCounter += 1
        setOperand = self.__TheMFE.InsertNewOperandAt(self.__operandCounter)
        setOperand.ChangeType(constants.MeritOperandType_DISG)
        setOperand.Weight = Weight
        setOperand.GetOperandCell(2).IntegerValue = Field
        setOperand.GetOperandCell(3).IntegerValue = WaveIndex
        setOperand.GetOperandCell(4).DoubleValue = Hx
        setOperand.GetOperandCell(5).DoubleValue = Hy
        setOperand.GetOperandCell(6).DoubleValue = Px
        setOperand.GetOperandCell(7).DoubleValue = Py

    def addOperandMTFS(self, Weight, Sample, WaveIndex, Field, Frequency):
        self.__operandCounter += 1
        setOperand = self.__TheMFE.InsertNewOperandAt(self.__operandCounter)
        setOperand.ChangeType(constants.MeritOperandType_MTFS)
        setOperand.Weight = Weight
        setOperand.GetOperandCell(2).IntegerValue = Sample
        setOperand.GetOperandCell(3).IntegerValue = WaveIndex
        setOperand.GetOperandCell(4).IntegerValue = Field
        setOperand.GetOperandCell(5).DoubleValue = Frequency

    def addOperandMTFT(self, Weight, Sample, WaveIndex, Field, Frequency):
        self.__operandCounter += 1
        setOperand = self.__TheMFE.InsertNewOperandAt(self.__operandCounter)
        setOperand.ChangeType(constants.MeritOperandType_MTFT)
        setOperand.Weight = Weight
        setOperand.GetOperandCell(2).IntegerValue = Sample
        setOperand.GetOperandCell(3).IntegerValue = WaveIndex
        setOperand.GetOperandCell(4).IntegerValue = Field
        setOperand.GetOperandCell(5).DoubleValue = Frequency

    def addOperandPROB(self, Weight, Target, TargetOperand, Factor = 1):
        self.__operandCounter += 1
        setOperand = self.__TheMFE.InsertNewOperandAt(self.__operandCounter)
        setOperand.ChangeType(constants.MeritOperandType_PROB)
        setOperand.Weight = Weight
        setOperand.Target = Target
        setOperand.GetOperandCell(2).IntegerValue = TargetOperand
        setOperand.GetOperandCell(4).DoubleValue = Factor

    def addOperandOPLT(self, Weight, Target, TargetOperand):
        self.__operandCounter += 1
        setOperand = self.__TheMFE.InsertNewOperandAt(self.__operandCounter)
        setOperand.ChangeType(constants.MeritOperandType_OPLT)
        setOperand.Weight = Weight
        setOperand.Target = Target
        setOperand.GetOperandCell(2).IntegerValue = TargetOperand

    def addOperandOPGT(self, Weight, Target, TargetOperand):
        self.__operandCounter += 1
        setOperand = self.__TheMFE.InsertNewOperandAt(self.__operandCounter)
        setOperand.ChangeType(constants.MeritOperandType_OPGT)
        setOperand.Weight = Weight
        setOperand.Target = Target
        setOperand.GetOperandCell(2).IntegerValue = TargetOperand

    def removeOperand(self, startOperandIndex, endOperandIndex = -1):
        if endOperandIndex == -1:
            endOperandIndex = startOperandIndex
        self.__TheMFE.RemoveOperandsAt(startOperandIndex, endOperandIndex)

    def getOperandCounter(self):
        return self.__operandCounter

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
