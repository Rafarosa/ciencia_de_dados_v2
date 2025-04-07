#funcao para imprimir uma mensagem de boas-vindas

def boas_vindas():
    nome = input('Qual o seu nome? ')
    print('Olá', nome, 'seja bem-vindo(a) ao curso de Python!')

# chamada da função
# modulo principal
if __name__ == '__main__':
    boas_vindas()
    print('Esse é o módulo principal.')
    print('O nome desse módulo é:', __name__)
    print('O nome do módulo que está sendo executado é:', __file__)