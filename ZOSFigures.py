from ZOSCOM import *
from matplotlib import cm
from matplotlib.ticker import FormatStrFormatter, MaxNLocator
from matplotlib.colors import ListedColormap, LinearSegmentedColormap
import matplotlib.pyplot as plt
import numpy as np
import glob, sys, os, math

pyfile = sys.argv[0]
dirpath = os.path.dirname(pyfile)

class ZOSFigure():
    def __init__(self, TheSystem):
        self.__TheSystemData = TheSystem.SystemData
        self.__colors = ('b','g','r','c', 'm', 'y', 'k')
        self.__field_case_legend = []
        self.__numberOfWavelength = self.__TheSystemData.Wavelengths.NumberOfWavelengths
        self.__Wavelengthslst = np.zeros(self.__numberOfWavelength)
        for i in range(self.__numberOfWavelength):
            self.__Wavelengthslst[i] = self.__TheSystemData.Wavelengths.GetWavelength(i + 1).Wavelength

        self.__Fields = []
        for i in range(self.__TheSystemData.Fields.NumberOfFields):
            self.__Fields.append(self.__TheSystemData.Fields.GetField(i + 1).Y)

        for i in range(len(self.__Fields)):
            if not (i == 0 or i == 6 or i == 8 or i == 10):
                continue
            mtft_append_legend = '{:.4f}'.format(self.__Fields[i]) + 'mm (T)'
            mtfs_append_legend = '{:.4f}'.format(self.__Fields[i]) + 'mm (S)'
            self.__field_case_legend.append(mtft_append_legend)
            self.__field_case_legend.append(mtfs_append_legend)

    def export_figFCD(self, newFCD_ResultsCast, distType = 'F-Tan(theta)', distXScale = 3):
        figFCD, axs = plt.subplots(1, 2)
        distTitle = distType + ' Distortion'
        for gridN in range(newFCD_ResultsCast.NumberOfDataSeries):
            dataFCD = newFCD_ResultsCast.GetDataSeries(gridN)
            y = np.array(dataFCD.YData.Data)
            x = np.array(dataFCD.XData.Data)
            axs[0].plot(y[:,0], x[:],linestyle='--',color=self.__colors[gridN], label = str(self.__Wavelengthslst[gridN]) + '(T)')
            axs[0].plot(y[:,1], x[:],color=self.__colors[gridN], label = str(self.__Wavelengthslst[gridN]) + '(S)')
        axs[0].set_xlim(-0.2 , 0.2)
        axs[0].set_ylim(0 ,max(x))
        axs[0].xaxis.set_major_locator(MaxNLocator(5))
        axs[0].xaxis.set_major_formatter(FormatStrFormatter('%.1f'))
        axs[0].set_xlabel('Millimeters')
        axs[0].set_ylabel('+Y')
        axs[0].legend(loc = 'lower right', frameon=False, fontsize = 10)
        axs[0].grid(True)
        axs[0].set_title('Field Curvature', fontsize = 16, fontweight = 'bold')

        for gridN in range(newFCD_ResultsCast.NumberOfDataSeries):
            dataFCD = newFCD_ResultsCast.GetDataSeries(gridN)
            y = np.array(dataFCD.YData.Data)
            x = np.array(dataFCD.XData.Data)
            axs[1].plot(y[:,4], x[:],color=self.__colors[gridN],label=str(self.__Wavelengthslst[gridN]))
        axs[1].set_xlim(-distXScale , distXScale)
        axs[1].set_ylim(0 ,max(x))
        axs[1].xaxis.set_major_locator(MaxNLocator(5))
        axs[1].xaxis.set_major_formatter(FormatStrFormatter('%.1f'))
        axs[1].set_xlabel('Percent')
        axs[1].set_ylabel('+Y')
        axs[1].legend(loc = 'lower right', frameon=False, fontsize = 10)
        axs[1].grid(True)
        axs[1].set_title(distTitle, fontsize = 16, fontweight = 'bold')
    
        plt.suptitle('Maximum Field is ' + '{:.3f}'.format(max(x)) + ' Degrees')
        FilePath = dirpath + '//FCD.png'
        figFCD.savefig(FilePath)
        plt.close()

    def export_figMTF(self, newMTF_ResultsCast):
        figMTF = plt.figure()
        ax = plt.subplot(111)
        j = 0
        for seriesNum in range(0,newMTF_ResultsCast.NumberOfDataSeries,1):
            if seriesNum == 0 or seriesNum == 6 or seriesNum == 8 or seriesNum == 10:
                data = newMTF_ResultsCast.GetDataSeries(seriesNum)
                x = np.array(data.XData.Data)
                y = np.array(data.YData.Data)

                ax.plot(x[:],y[:,0],linestyle='--',color=self.__colors[j])
                ax.plot(x[:],y[:,1],color=self.__colors[j])
                j += 1
        plt.title('Data for ' + str(min(self.__Wavelengthslst)) + r'$\mu$m to ' + str(max(self.__Wavelengthslst)) + r'$\mu$m'
            , fontsize = 12)
        plt.suptitle('Polychromatic Diffracton MTF', fontsize = 16, fontweight = 'bold')
        plt.xlabel('Spatial Frequency in cycles per mm')
        plt.ylabel('Modulus of the OTF')
        plt.grid(True)
        plt.xlim(0 , max(x))
        plt.ylim(0 ,1)

        ax.legend(self.__field_case_legend, loc='lower center', bbox_to_anchor=(0.5, -0.25), fontsize = 10,
          ncol=4, fancybox=True, shadow=False)
        box = ax.get_position()
        ax.set_position([box.x0, box.y0 + box.height * 0.1, box.width, box.height * 0.9])

        FilePath = dirpath + '//MTF.png'
        figMTF.savefig(FilePath)
        plt.close()

    def export_figMTFvsField(self, newMtfvsField_ResultsCast):
        figMTFvsField = plt.figure()
        ax = plt.subplot(111)
        figLegend = []
        for seriesNum in range(0,newMtfvsField_ResultsCast.NumberOfDataSeries,1):
            data = newMtfvsField_ResultsCast.GetDataSeries(seriesNum)
            legend = ''.join(list(filter(lambda ch: ch in '0123456789.', data.Description)))
            legend, ignore = legend[:-1], legend[-1]
            legendT = legend + 'cyc/mm (T)'
            legendS = legend + 'cyc/mm (S)'
            figLegend.append(legendT)
            figLegend.append(legendS)
            x = np.array(data.XData.Data)
            y = np.array(data.YData.Data)
            ax.plot(x[:],y[:,0],linestyle='--',color=self.__colors[seriesNum])
            ax.plot(x[:],y[:,1],color=self.__colors[seriesNum])
        plt.suptitle('FFT MTF vs. Field', fontsize = 16, fontweight = 'bold')
        plt.xlabel('Y Field in the Millimeters')
        plt.ylabel('Modulus of the OTF')
        plt.grid(True)
        plt.xlim(0 , max(x))
        plt.ylim(0 ,1)
        ax.legend(figLegend, loc='lower center', bbox_to_anchor=(0.5, 0), fontsize = 10,
          ncol=4, fancybox=True, shadow=False)
        FilePath = dirpath + '//MTFvsField.png'
        figMTFvsField.savefig(FilePath)
        plt.close()

    def export_figTFM(self, newTFM_ResultsCast, tfmXScale = 0.05):
        figTFM = plt.figure()
        ax = plt.subplot(111)
        j = 0
        for seriesNum in range(0,newTFM_ResultsCast.NumberOfDataSeries,1):
            if seriesNum == 0 or seriesNum == 6 or seriesNum == 8 or seriesNum == 10:
                data = newTFM_ResultsCast.GetDataSeries(seriesNum)
                x = np.array(data.XData.Data)
                y = np.array(data.YData.Data)

                ax.plot(x[:],y[:,0],linestyle='--',color=self.__colors[j])
                ax.plot(x[:],y[:,1],color=self.__colors[j])
                j += 1
        plt.title('Data for ' + str(min(self.__Wavelengthslst)) + r'$\mu$m to ' + str(max(self.__Wavelengthslst)) + r'$\mu$m'
            , fontsize = 12)
        plt.suptitle('Polychromatic Diffraction Through Focus MTF', fontsize = 16, fontweight = 'bold')
        plt.xlabel('Focus Shift in Millimeters')
        plt.ylabel('Modulus of the OTF')
        plt.grid(True)
        plt.xlim(-tfmXScale , tfmXScale)
        plt.ylim(0 ,1)

        ax.legend(self.__field_case_legend, loc='lower center', bbox_to_anchor=(0.5, -0.25), fontsize = 10,
          ncol=4, fancybox=True, shadow=False)
        box = ax.get_position()
        ax.set_position([box.x0, box.y0 + box.height * 0.1, box.width, box.height * 0.9])

        FilePath = dirpath + '//TFM.png'
        figTFM.savefig(FilePath)
        plt.close()


    def export_figREL(self, Fields, reliValue):
        figREL = plt.figure()
        ax = plt.subplot(111)
        ax.plot(Fields[:],reliValue[:],color='b')
        plt.suptitle('Relative Illumination')
        plt.title('Wavelength is ' + str(self.__Wavelengthslst[int(self.__numberOfWavelength / 2)]) + r'$\mu$m')
        plt.xlabel('Y Field in Millimeters')
        plt.ylabel('Relative Illumination', fontsize = 16, fontweight = 'bold')
        plt.xlim(0 , max(Fields))
        plt.ylim(0 ,1)
        plt.grid(True)
        relFilePath = dirpath + '//REL.png'
        figREL.savefig(relFilePath)
        plt.close()
