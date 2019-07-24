from win32com.client import CastTo, constants

class ZOSMCE(object):
    def __init__(self, TheSystem, opStartIndex = 1, confStartIndex = 1):
        self.__TheMCE = TheSystem.MCE
        self.__operandCounter = opStartIndex
        self.__configCounter = confStartIndex

    def addConfig(self, quantity = 1):
        for i in range(quantity):
            self.__TheMCE.AddConfiguration(False)
            self.__configCounter += 1

    def addOperandPRAM(self, Surface, ParaNum):
        self.__operandCounter += 1
        self.__TheMCE.InsertNewOperandAt(0)
        

    def rmAllConfig(self):
        pass

    def rmAllConfig(self, index):
        pass

    def getConfigQuan(self):
        return self.__configCounter

    def getOperandQuan(self):
        return self.__operandCounter