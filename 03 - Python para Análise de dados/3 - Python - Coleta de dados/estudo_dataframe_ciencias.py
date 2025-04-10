# Estudo dataframe
# Importando as bibliotecas necessárias
import pandas as pd

#lista: uma coleção ordenada de elementos que podem ser de qualquer tipo
lista_nomes = ["Lucas", "Ana", "Carlos", "Maria"]
print(f'Lista de nomes: \n{lista_nomes}')
print(f'Primeiro elemento da lista: {lista_nomes[0]}')

# Dictionary: uma coleção não ordenada de pares chave-valor
dicionario_pessoa = {
    "nome": "Lucas",
    "idade": 30,
    "altura": 1.75,
    "cidade": "São Paulo"
}

print(f'Dicionário de pessoa: \n{dicionario_pessoa}')
print(f'Nome da pessoa: {dicionario_pessoa.get("nome")}')

#Lista de dicionários: uma coleção ordenada de dicionários
dados = [
    {"nome": "Lucas", "idade": 30, "altura": 1.75, "cidade": "São Paulo"},
    {"nome": "Ana", "idade": 25, "altura": 1.65, "cidade": "Rio de Janeiro"},
    {"nome": "Carlos", "idade": 35, "altura": 1.80, "cidade": "Belo Horizonte"},
    {"nome": "Maria", "idade": 28, "altura": 1.70, "cidade": "Curitiba"}
]

# Dataframe: uma estrutura de dados bidimensional, semelhante a uma tabela, que pode conter dados de diferentes tipos (números, strings, etc.)
df = pd.DataFrame(dados)
print(f'Dataframe: \n{df}')


# selecionando uma coluna do dataframe
print(f'Coluna nome: \n{df["nome"]}')


# selecioando varias colunas
print(f'Colunas nome e idade: \n{df[["nome", "idade"]]}')
print('------------------------------------------------------')

# selecionando uma linha do dataframe pelo seu indice
print(f'Linha 0: {df.iloc[0]}')
print(f'Linha 1: {df.iloc[1]}')


# Adicionando uma nova coluna ao dataframe
df['Salario'] = [1000, 2000, 3000, 4000]
print(f'Dataframe com nova coluna: \n{df}')
print('------------------------------------------------------')

# criando novo registro
df.loc[len(df)] = ["João", 40, 1.85, "Salvador", 5000]
print(f'Dataframe com novo registro: \n{df}')
print('------------------------------------------------------')


#removendo uma coluna do dataframe
df.drop(labels='Salario', axis=1, inplace=True)


#Filtrando pessoas com mais de 29 anos
filtro_idade = df[df['idade'] > 29]
print(f'Pessoas com mais de 29 anos: \n{filtro_idade}')
print('------------------------------------------------------')

#Salvando o dataframe em um arquivo CSV
df.to_csv('assets/dados_pessoas.csv', index=False)

#Lendo o arquivo CSV
df_lido = pd.read_csv('assets/dados_pessoas.csv')
print(f'Dados lidos do arquivo CSV: \n{df_lido}')