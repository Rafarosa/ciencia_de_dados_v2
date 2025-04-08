## URL - https://finance.yahoo.com/quote/%5EBVSP/history/

import requests
import pandas as pd
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.b3.com.br/pt_br/market-data-e-indices/indices/indices-amplos/indice-ibovespa-ibovespa-estatisticas-historicas.htm"
reponse = requests.get(url)
print(reponse.text[:600]) # verificando o texto da request

soup = BeautifulSoup(reponse.text, "html.parser")
print(soup.prettify()[:1000]) # verificando o HTML da página

print("Pandas: ") # verificando o título da página
url_dados =  pd.read_html(url)# lendo a tabela da página
print(url_dados[0].head(10)) # verificando os dados da página

#url = "https://jsonplaceholder.typicode.com/posts/1"
#response = requests.get(url)
##salvar o conteúdo da resposta em um arquivo JSON
#with open("dados.json", "w") as file:
#    file.write(response.text)
#print(response.json()) # verificando o texto da request