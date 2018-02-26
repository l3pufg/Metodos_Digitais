''
esse script utiliza o python 2.7
''

from cStringIO import StringIO
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
import os
import sys, getopt
import codecs

#converte o pdf, retorna seu texto em uma string
def convert(fname, pages=None):
    if not pages:
        pagenums = set()
    else:
        pagenums = set(pages)

    output = StringIO()
    manager = PDFResourceManager()
    converter = TextConverter(manager, output, laparams=LAParams())
    interpreter = PDFPageInterpreter(manager, converter)

    infile = file(fname, 'rb')
    for page in PDFPage.get_pages(infile, pagenums):
        interpreter.process_page(page)
    infile.close()
    converter.close()
    text = output.getvalue()
    output.close
    return text 
   
def convertMultiple(pdfDir, txtDir):
    if pdfDir == "": pdfDir = os.getcwd() + "\\" #verifica se existe a pasta com pdfs 
    for pdf in os.listdir(pdfDir): #itera os pdfs na pasta onde estão
        fileExtension = pdf.split(".")[-1]
        if fileExtension == "pdf":
            pdfFilename = pdfDir + pdf 
            text = convert(pdfFilename) #obtém as strings de texto do pdf
            textFilename = txtDir + pdf + ".txt"
            textFile = open(textFilename, "w") #cria o arquivo de texto
            textFile.write(text) #escreve no arquivo de texto
			#textFile.close

pdfDir = "Pasta com os PDF´s"
txtDir = "Pasta com os arquivos de texto"
convertMultiple(pdfDir, txtDir)
