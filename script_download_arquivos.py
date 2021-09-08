# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 09:35:03 2021

@author: Afonso Feliciano
"""

import zipfile
import requests
from io import BytesIO
import os
from datetime import date
from datetime import datetime
import time


# Criando diretorio para armazenar o conteúdo do portal da transparência
diretorio = './arquivos'

#deleta o diretório caso esteja vazio
os.system('rmdir "%s"' % diretorio)


#se nao existir, cria o diretorio
if not os.path.exists(diretorio):
    os.makedirs(diretorio)


#setando ano inicial e descobrindo ano atual para criação do loop
ano_inicial = 2011
data_atual  = date.today()
ano_atual = data_atual.year


#define a url e cria loop para concatenar os anos
url_parcial = "http://portaltransparencia.gov.br/download-de-dados/viagens/"

for x in range(ano_inicial, ano_atual + 1):
    
    #cria url com ano
    url_final = url_parcial + str(x)
    
    print( " Realizando o download do conteudo da URL: " + url_final + " às " + datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
    
    #realiza o get na url final e armazena no formato de bytes
    filebytes = BytesIO( requests.get(url_final).content )
    
    #utiliza a bilioteca zipfile para armazenar o arquivo bytes de maneira comptactada
    myzip = zipfile.ZipFile(filebytes)
    print("Descompactando o conteudo da URL: " + url_final + " às " + datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "\n")
    
    #descompacta o arquivo
    myzip.extractall("./arquivos")
    
    #aguarda 1 segundo para um novo loop
    time.sleep(1)
print("Downloads finalizados")
