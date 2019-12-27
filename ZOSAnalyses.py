from win32com.client import CastTo, constants

dictSampleSize = {32:'constants.SampleSizes_S_32x32', 64:'constants.SampleSizes_S_64x64', 128:'constants.SampleSizes_S_64x64', \
    256:'constants.SampleSizes_S_256x256', 512:'constants.SampleSizes_S_512x512', 1024:'constants.SampleSizes_S_1024x1024',\
    2048:'constants.SampleSizes_S_2048x2048', 4096:'constants.SampleSizes_S_4096x4096', 8192:'constants.SampleSizes_S_8196x8192', \
    16384: 'constants.SampleSizes_S_16384x16384'}

dictScanType = {'+y':'constants.ScanTypes_Plus_Y', '-y':'constants.ScanTypes_Minus_Y', '+x':'constants.ScanTypes_Plus_X',\
    '-x':'constants.ScanTypes_Minus_X'}

dictDistortions = {'F_TanTheta':'constants.Distortions_F_TanTheta', 'F_Theta':'constants.Distortions_F_Theta',\
    'Cal_F_Theta':'constants.Distortions_Cal_F_Theta', 'Cal_F_TanTheta':'constants.Distortion_Cal_F_TanTheta'}

dictReferType = {'ChiefRay':'constants.ChiefRay', 'Centroid':'constants.Centroid', 'Vertex':'constants.Vertex'}

class ZOSAnalyses(object):
    def __init__(self, TheSystem):
        self.__TheAnalyses = TheSystem.Analyses

    def FieldCurvatureAndDistortion(self, distType = 'F_TanTheta'):
        newFCD = self.__TheAnalyses.New_FieldCurvatureAndDistortion()
        newFCD_Settings = newFCD.GetSettings()
        newFCD_SettingsCast = CastTo(newFCD_Settings,'IAS_FieldCurvatureAndDistortion')
        newFCD_SettingsCast.Distortion = eval(dictDistortions[distType])
        newFCD.ApplyAndWaitForCompletion()
        newFCD_Results = newFCD.GetResults()
        newFCD_ResultsCast = CastTo(newFCD_Results, 'IAR_')
        return newFCD_ResultsCast

    def FftMtf(self, MaximumFrequency, SampleSizes = 32):
        newMTF = self.__TheAnalyses.New_FftMtf()
        newMTF_Settings = newMTF.GetSettings()
        newMTF_SettingsCast = CastTo(newMTF_Settings,'IAS_FftMtf')
        newMTF_SettingsCast.MaximumFrequency = MaximumFrequency
        newMTF_SettingsCast.SampleSize = eval(dictSampleSize[SampleSizes])
        newMTF.ApplyAndWaitForCompletion()
        newMTF_Results = newMTF.GetResults()
        newMTF_ResultsCast = CastTo(newMTF_Results, 'IAR_')
        return newMTF_ResultsCast

    def FftTfm(self, Frequency, SampleSizes = 64):
        newTFM = self.__TheAnalyses.New_FftThroughFocusMtf()
        newTFM_Settings = newTFM.GetSettings()
        newTFM_SettingsCast = CastTo(newTFM_Settings,'IAS_FftThroughFocusMtf')
        newTFM_SettingsCast.Frequency = Frequency
        newTFM_SettingsCast.SampleSize = eval(dictSampleSize[SampleSizes])
        newTFM.ApplyAndWaitForCompletion()
        newTFM_Results = newTFM.GetResults()
        newTFM_ResultsCast = CastTo(newTFM_Results, 'IAR_')
        return newTFM_ResultsCast

    def FftMtfvsField(self, FieldDensity = 10, ScanType = '+y', SampleSizes = 64, Freq_1 = 0, Freq_2 = 0, Freq_3 = 0, \
        Freq_4 = 0, Freq_5 = 0, Freq_6 = 0, RemoveVignetting = False, UsePolarization = False):

        newMtfvsField = self.__TheAnalyses.New_FftMtfvsField()
        newMtfvsField_Settings = newMtfvsField.GetSettings()
        newMtfvsField_SettingsCast = CastTo(newMtfvsField_Settings,'IAS_FftMtfvsField')
        newMtfvsField_SettingsCast.FieldDensity = FieldDensity
        newMtfvsField_SettingsCast.ScanType = eval(dictScanType[ScanType])
        newMtfvsField_SettingsCast.SampleSize = eval(dictSampleSize[SampleSizes])
        newMtfvsField_SettingsCast.Freq_1 = Freq_1
        newMtfvsField_SettingsCast.Freq_2 = Freq_2
        newMtfvsField_SettingsCast.Freq_3 = Freq_3
        newMtfvsField_SettingsCast.Freq_4 = Freq_4
        newMtfvsField_SettingsCast.Freq_5 = Freq_5
        newMtfvsField_SettingsCast.Freq_6 = Freq_6
        newMtfvsField_SettingsCast.RemoveVignetting = RemoveVignetting
        newMtfvsField_SettingsCast.UsePolarization = UsePolarization
        newMtfvsField.ApplyAndWaitForCompletion()
        newMtfvsField_Results = newMtfvsField.GetResults()
        newMtfvsField_ResultsCast = CastTo(newMtfvsField_Results, 'IAR_')
        return newMtfvsField_ResultsCast

    def StandardSpot(self, referType):
        spot = self.__TheAnalyses.New_Analysis(constants.AnalysisIDM_StandardSpot)
        spot_setting = spot.GetSettings()
        baseSetting = CastTo(spot_setting, 'IAS_Spot')
        baseSetting.Field.UseAllFields()
        baseSetting.ReferTo = eval(dictReferType[referType])
        base = CastTo(spot, 'IA_')
        base.ApplyAndWaitForCompletion()
        spot_results = base.GetResults()
        return spot_results

    def RelativeIllumination(self):
        pass

    def LateralColor(self, useAllWavelengths = True, showAiryDisk = True, useRealRays = True):
        newLateralColor = self.__TheAnalyses.New_LateralColor()
        newLateralColor_Settings = newLateralColor.GetSettings()
        newLateralColor_SettingsCast = CastTo(newLateralColor_Settings, 'IAS_LateralColor')
        newLateralColor_SettingsCast.AllWavelengths = useAllWavelengths
        newLateralColor_SettingsCast.ShowAiryDisk = showAiryDisk
        newLateralColor_SettingsCast.UseRealRays = useRealRays
        newLateralColor.ApplyAndWaitForCompletion()
        newLateralColor_Results = newLateralColor.GetResults()
        newLateralColor_ResultsCast = CastTo(newLateralColor_Results, 'IAR_')
        return newLateralColor_ResultsCast
        
    def FocalShiftDiagram(self, maximumShift = 0, pupilZone = 0):
        newFocalShift = self.__TheAnalyses.New_FocalShiftDiagram()
        newFocalShift_Settings = newFocalShift.GetSettings()
        newFocalShift_SettingsCast = CastTo(newFocalShift_Settings, 'IAS_FocalShiftDiagram')
        newFocalShift_SettingsCast.MaximumShift = maximumShift
        newFocalShift_SettingsCast.PupilZone = pupilZone
        newFocalShift.ApplyAndWaitForCompletion()
        newFocalShift_Results = newFocalShift.GetResults()
        newFocalShift_ResultsCast = CastTo(newFocalShift_Results, 'IAR_')
        return newFocalShift_ResultsCast

    def LayOut2D(self):
        newLayOut = self.__TheAnalyses.New_Analysis(constants.AnalysisIDM_Draw2D)

