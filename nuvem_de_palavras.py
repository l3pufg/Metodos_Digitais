# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 19:01:15 2017

Script que gera nuvem de palavras retirando as stopwords

@author: eduardo
"""
import numpy as np # importa o numpy
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt # biblioteca para gráficos
import nltk # importa o nltk
import string
from nltk.corpus import stopwords # bilbioteca de stopwords dos corpus do nltk
from wordcloud import WordCloud # biblioteca que cria nuvens de palavras

# Abre o arquivo e verifica as Stopwords, caso identifique são retiradas
# com o NLTK e o pacote de lingua portuguesa
with open('your_file.txt', 'r') as f, open('your_new_file_without_stopwords.txt','w') as outnew:
	for line in f.readlines():
	    print(" ".join([word for word in line.lower().translate(str.maketrans('', '', string.punctuation)).split() 
        	if len(word) >=4 and word not in stopwords.words('portuguese')]), file=outnew)

# Abre o novo arquivo gerado e cria um dataframe com o pandas
infile = open('your_new_file_without_stopwords.txt', 'r')
text = infile.readlines()
df = pd.DataFrame({'palavras_texto':text})

# Em caso de textos separado por linhas com (enter) ele apresenta as 5 primeiras
# em caso de paragráfo apresenta só uma parte da primeira linha
print(df.head(5))

# gera uma figura de tamanho 12 por 12 cm, para plotar as palavras
plt.subplots(figsize=(12,12))

# Configura a apresentação, em uma imagem com fundo branco
# com tamanho de 1024x768
wordcloud = WordCloud(
                          background_color='white',
                          width=1024,
                          height=768
                         ).generate(" ".join(df['palavras_texto']))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis('off')
# apresenta a imagem gerada
plt.show()
# existe uma infinidade de variações #
# fonte/source: https://github.com/amueller/word_cloud #
