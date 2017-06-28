# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 13:25:32 2017
@author: LuisMDlab
Métodos Digitais - L3P - UFG
"""

# To run this, you can install BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4

# Or download the file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

#Parte do código foi utilizado da base do curso Python for Everybody - https://www.py4e.com/

#Código para acessar um site, recuperar todos os seus links e retornar um dicionário com os domínios e suas frequencias.
#É necessáiro ainda fazer alguma funções para otimizar o código.

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import collections
from collections import OrderedDict
import ssl

# Ignore SSL certificate errors - Bom para evitar erros ao acessar links com protocolo de segurança "https"
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#Acessa um link e retorna todo o html deste link. Para acessar vários links, utilizar um loop acoplado à uma lista de links.
url = 'https://www.ufg.br/'
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retorna todas as tags âncora "a", e adiciona os kinks via "href" à uma lista cahamada "Links".
tags = soup('a')
links = list()
for tag in tags:
    links.append(tag.get('href', None))

#Usando o urlparse retira só os domínios dos links através de ".netloc" e adiciona à uma lista chamada "dominios".    
dominios = list()
for link in links:
    o = urlparse(link)
    dominio = o.netloc
    dominios.append(dominio)


#Remove espaços da lista de domínios (podia ter resolvido com um IF lá em cima)
domin = list()
for i in dominios:
    if i == '':
        continue
    elif i != '':
        domin.append(i)
        
#Calcula a frequencia dos itens do dicionário domin        
contagem = collections.Counter(domin)

#Gera um dict com os itens ordenados por valor (Desnecessário para uso em BD ou CSV)
contagemsort = OrderedDict(sorted(contagem.items(), key=lambda x: x[1], reverse=True))

#Apresenta os itens e as quantidades.
for k,l in contagemsort.items():
    print('Domínio: '+ k+ ' Quantidade: ' +str(l))

