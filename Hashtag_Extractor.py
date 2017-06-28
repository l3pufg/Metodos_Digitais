# -*- coding: utf-8 -*-
"""
Created on Fri Jun 23 11:37:58 2017
@author: LuisMDlab
Métodos Digitais - L3P - UFG
"""

#Script Core de extração de hashtags "#", através de REGEX

#Importar a biblioteca "re" de expressões regulares.
import re

#Definição da string a ser minerada. Para documentos, usar a funçao open e definir o acesso ao documento a partir do documento.
x = 'From #Name stephen.marquard@uct.ac.za #IWon Sat Jan  5 09:14:16 2008 #SouFree e #pronto'

#Busca qualquer coisa que se pareça com uma Hashtag na string, e armazena como uma list aem Y.
y = re.findall('(#.+?\S+)\s*?', x)

print(y)
