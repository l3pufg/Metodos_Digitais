import os

for fich in os.listdir('.'):
        if fich[-3:]=="pdf":
                os.system("ps2pdf -dPDFSETTINGS=/ebook %s reduc/%s" % (fich,fich))
