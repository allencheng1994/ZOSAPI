import glob, sys, os, math, datetime
import xlwings as xw

def getzmxfileUni():
    pyfile = sys.argv[0]
    dirpath = os.path.dirname(pyfile)
    zmxfile = glob.glob(dirpath + "\\*.zmx")
    if len(zmxfile) < 1:
        print("You don't have any .zmx file here!")
        os._exit(0)
    elif len(zmxfile) > 1:
        print("You have more than one .zmx file here!")
        os._exit(0)
    else:
        return zmxfile[0]

def getzmxfile(zmxFilename):
    pyfile = sys.argv[0]
    dirpath = os.path.dirname(pyfile)
    zmxfile = glob.glob(dirpath + "\\" + zmxFilename)
    if len(zmxfile) < 1:
        print("You don't have the .zmx file here!")
        os._exit(0)
    else:
        return zmxfile[0]

def getxlsxfile(xlsxFilename):
    pyfile = sys.argv[0]
    dirpath = os.path.dirname(pyfile)
    xlsxfile = glob.glob(dirpath + "\\" + xlsxFilename)
    if len(xlsxfile) < 1:
        print("You don't have the .xlsx file here!")
        os._exit(0)
    else:
        return xlsxfile[0]

def addPictureAt(figName, selectedCell, figWidth = 271.8, figHeight = 204.3):
    pyfile = sys.argv[0]
    dirpath = os.path.dirname(pyfile)
    pic = active_sheet.pictures.add(dirpath + '\\' + figName,\
         top=xw.Range(selectedCell).top, left=xw.Range(selectedCell).left, width=figWidth, height=figHeight)

def setMFName(filename):
    pyfile = sys.argv[0]
    dirpath = os.path.dirname(pyfile)
    mf_filename = dirpath + '\\' + filename + '.mf'
    return mf_filename
