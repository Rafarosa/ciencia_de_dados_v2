import requests

def enviar_arquivo():
    # Camanho do arquivo a ser enviado
    arquivo = "assets\produtos_informatica.xlsx"

    # enviar o arquivo para a API
    requisição = requests.post(
        url="https://httpbin.org/post",
        files={"file": open(arquivo, "rb")}
    )