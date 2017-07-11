#
#
#BAIXE E INSTALE O GHOSTSCRIPT PRIMEIRO / install ghostscript first
#
#
from __future__ import print_function
import os
import subprocess

for root, dirs, files in os.walk("pasta com os arquivos / folder with files"):
    for file in files:
        if file.endswith(".pdf"):
            filename = os.path.join(root, file)
            print (filename)
            arg1= '-sOutputFile=' + "c" +  file #added a c to the filename
            p = subprocess.Popen(['C:/Program Files (x86)/gs/gs9.21/bin/gswin32c.exe', #path to the ghostscript
                                  '-sDEVICE=pdfwrite', 
                                  '-dCompatibilityLevel=1.5',
                                  '-sstdout=%stderr',
                                  '-dGrayImageResolution=600',
                                  '-dMonoImageResolution=1200',
                                  '-dColorImageResolution=300',
                                  '-dPDFSETTINGS=/screen', '-dNOPAUSE', 
                                  '-dBATCH', '-dQUIET', str(arg1), filename], 
                                 stdout=subprocess.PIPE)
            print (p.communicate())
