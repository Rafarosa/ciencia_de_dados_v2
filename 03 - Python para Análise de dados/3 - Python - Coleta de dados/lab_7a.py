### Extração e manipulação de dados - 01
'''
Vamos iniciar o nosso projeto de extração e manipulação de dados, utilizando inicialmente os dados do e-commerce books.toscrape.com. Este é um site para fins educativos para realizar web scraping de uma página fictícia de livraria. Vamos utilizar este site pois, se utilizássemos sites de e-commerce, poderíamos ser vistos como robôs que querem tentar invadir ou derrubar o site, afinal, muitos alunos acessariam o mesmo site e realizariam consultas.

Para este primeiro exercício faça o seguinte:

Mostre os primeiros 2000 caracteres do site https://books.toscrape.com/
Armazene a requisição na variável requisicao.
Use o print com a requisição para chegar no resultado. Utilize também a função prettify()

'''
import requests
from bs4 import BeautifulSoup
import pandas as pd
requests.packages.urllib3.disable_warnings()

url = 'https://books.toscrape.com/'
requisicao = requests.get(url)

extracao = BeautifulSoup(requisicao.text, 'html.parser')
 
print(extracao.prettify()[:2000])

