from win32com.client import CastTo, constants

dictQuickFocusType = {'RMS':'constants.QuickFocusCriterion_RMSWavefront', 'SPOTR':'constants.QuickFocusCriterion_SpotSizeRadial',\
    'SPOTX':'constants.QuickFocusCriterion_SpotSizeXOnly', 'SPOTY':'constants.QuickFocusCriterion_SpotSizeYOnly'}

class ZOSTools(object):
    def __init__(self, TheSystem):
        self.__tools = TheSystem.Tools

    def doQFocus(self, type='RMS', times = 1):
        QFocus = self.__tools.OpenQuickFocus()
        QFocus.Criterion = eval(dictQuickFocusType[type])
        QFocus.UseCentroid = False
        baseTool = CastTo(QFocus, 'ISystemTool')
        for j in range(times):
            baseTool.RunAndWaitForCompletion()
        baseTool.Close()