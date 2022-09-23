import os
from re import A
import time
import glob

try:

    loc = str("F:\ProyectosVS\Marcos")

    floc = loc.replace("'\'","'/'")

    os.chdir(floc)

    x = 0

    for file in glob.glob("*.pdf") + glob.glob("*.ocr") + glob.glob("*.jpg"):
        if (file != ''):
            os.startfile(file,"print")
            print('Archivo de impresión >> ' + str(file))
            x = x + 1

            time.sleep(2)

        print('Numero de archivo impreso = ' + str(x) )



except Exception as a:
    print (a)