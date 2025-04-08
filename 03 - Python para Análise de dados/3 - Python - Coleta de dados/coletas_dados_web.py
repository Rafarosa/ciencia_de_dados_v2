import requests
import pandas as pd
from bs4 import BeautifulSoup

url = "https://www.cnnbrasil.com.br/economia/mercado/bolsas-dos-eua-perdem-us-10-trilhoes-desde-posse-de-trump/"
requisicao = requests.get(url)
extracao = BeautifulSoup(requisicao.text, features="html.parser")

# Exibir o texto da requisição
#print(extracao.text.strip())

# Filtrar a exibição pela tag h2
#for linha_texto in extracao.find_all("h2"):
#    titulo = linha_texto.text.strip()
#    print(f'titulo: {titulo}')

'''
Desafio
Filtar tags ['h2', 'p']
Contar quantos h2 e quantos p existem na página (linha_texto.name == tag)
'''
contator_titulo = 0
contator_paragrafo = 0

#for linha_texto in extracao.find_all(["h2", "p"]):
#    if linha_texto.name == "h2":
#        contator_titulo += 1
#    elif linha_texto.name == "p":
#        contator_paragrafo += 1

#print(f"Quantidade de h2: {contator_titulo}")
#print(f"Quantidade de p: {contator_paragrafo}")

'''
Exiba somente o texto das tags h2 e p
'''
#for linha_texto in extracao.find_all(["h2", "p"]):
#    if linha_texto.name == "h2":
#        print(f'titulo: {linha_texto.text.strip()}')
#    elif linha_texto.name == "p":
#        print(f'paragrafo: {linha_texto.text.strip()}')

'''
Exibir tag Aninhadas
'''
for titulo in extracao.find_all("h2"):
    print(f'\n titulo: {titulo.text.strip()}')
    for link in titulo.find_all_next("p"):
        for a in link.find_all("a", href=True):
            print(f'texto do link: {a.text.strip()} | URL: {a["href"]}')