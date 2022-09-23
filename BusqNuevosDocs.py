from os import listdir
from os.path import isfile, join
import glob
import time

"""Variables"""
pdf = glob.glob("*.pdf")
jpg = glob.glob("*.jpg")
ocr = glob.glob("*.ocr")

"""Busqueda de archivos en el directorio"""
def fileInDirectory(my_dir: str):

    onlyfiles = glob.glob("*.pdf") + glob.glob("*.jpg") + glob.glob("*.ocr")
    """onlyfiles = [f for f in listdir(my_dir) if isfile(join(my_dir, f))]"""
    return(onlyfiles)


"""Lista de comparacion"""
def listComparison(OriginalList: list, NewList: list):
    differencesList = [x for x in NewList if x not in OriginalList] 
    return(differencesList)

def fileWatcher(my_dir: str, pollTime: int):
    while True:
        if 'watching' not in locals(): 
            previousFileList = fileInDirectory(my_dir)
            watching = 1
            print('First Time')
            print(previousFileList)
        
        time.sleep(pollTime)
        
        newFileList = fileInDirectory(my_dir)
        
        fileDiff = listComparison(previousFileList, newFileList)
        
        print (fileDiff)

        previousFileList = newFileList
        if len(fileDiff) == 0: continue

    """ doThingsWithNewFiles(fileDiff) """

fileWatcher ("F:\ProyectosVS\Marcos", 10)

