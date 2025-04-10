import pandas as pd
import random
from faker import Faker

faker = Faker('pt_BR')

dados_pessoais = []

for _ in range(10):
    nome = faker.name()
    cpf = faker.cpf()
    idade = random.randint(18, 80)
    data_nascimento = faker.date_of_birth(minimum_age=18, maximum_age=80).strftime("%d/%m/%Y")
    altura = round(random.uniform(1.50, 2.00), 2)
    endereco = faker.address()
    estado = faker.state()
    cidade = faker.city()
    pais = 'Brasil'

    dados_pessoais.append({
        "nome": nome,
        "idade": idade,
        "cpf": cpf,
        "altura": altura,
        "endereco": endereco,
        "data_nascimento": data_nascimento,
        "cidade": cidade,
        "estado": estado,
        "pais": pais
    })

print(f'Dados pessoais: \n{dados_pessoais}')

print('------------------------------------------------------')

# Gerando um DataFrame com os dados pessoais

df= pd.DataFrame(dados_pessoais)
print(f'DataFrame: \n{df}')

pd.set_option('display.max_columns', None)  # Exibir todas as colunas
pd.set_option('display.max_rows', None)  # Exibir todas as linhas
pd.set_option('display.width', None)  # Ajustar a largura da exibição
pd.set_option('display.max_colwidth', None)  # Exibir o conteúdo completo das colunas

print(df.to_string())

df.to_csv('assets/dados_pessoais.csv')

