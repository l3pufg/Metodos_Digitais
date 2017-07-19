# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 19:01:15 2017

@author: eduardo
"""
# assim como próprio python esse script apresenta erros em relação #
# a caracteres especiais como â, ã, ç, ê... entre outros a não ser #
# que salve o arquivo que for utilizado em ANSCI ao invés de UTF-8 #

import numpy as np # importa o numpy
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt # biblioteca para gráficos
from wordcloud import WordCloud # biblioteca que cria nuvens de palavras

# Abre o arquivo (nuvem3.txt) e lê, como esté sendo usado o pandas ele lê automáticamente
f = open('nuvem3.txt', "rt")
text = f.readlines()

# Cria um data frame com o pandas e dá o título
df = pd.DataFrame({'palavras_texto':text})

# Em caso de textos separado por linhas com (enter) ele apresenta as 5 primeiras
# Em caso de paragráfo apresenta só uma parte da primeira linha
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
