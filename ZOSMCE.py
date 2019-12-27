from win32com.client import CastTo, constants

class ZOSMCE(object):
    def __init__(self, TheSystem, opStartIndex = 1, confStartIndex = 1):
        self.__TheMCE = TheSystem.MCE
        self.__operandCounter = opStartIndex
        self.__configCounter = confStartIndex

    def addConfigs(self, quantity = 1):
        for i in range(quantity):
            self.__TheMCE.AddConfiguration(False)
            self.__configCounter += 1

    def addOperandPRAM(self, surface, paraNum):
        self.__operandCounter += 1
        setOperand = self.__TheMCE.InsertOperandAt(self.__operandCounter)
        setOperand.ChangeType(constants.MultiConfigOperandType_PRAM)
        setOperand.Param1 = surface
        setOperand.Param2 = paraNum
        
    def addOperandWAVE(self, wavelength):
        self.__operandCounter += 1
        setOperand = self.__TheMCE.InsertOperandAt(self.__operandCounter)
        setOperand.ChangeType(constants.MultiConfigOperandType_WAVE)
        setOperand.Param1 = wavelength

    def addOperandTHIC(self, surface):
        self.__operandCounter += 1
        setOperand = self.__TheMCE.InsertOperandAt(self.__operandCounter)
        setOperand.ChangeType(constants.MultiConfigOperandType_THIC)
        setOperand.Param1 = surface

    def addOperandTEMP(self):
        self.__operandCounter += 1
        setOperand = self.__TheMCE.InsertOperandAt(self.__operandCounter)
        setOperand.ChangeType(constants.MultiConfigOperandType_TEMP)

    def getOperandCounter(self):
        return self.__operandCounter
