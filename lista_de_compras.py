import pandas as pd

dados = {}

while True:
    chave = str(input("Informe o nome do produto: ")).strip()

    try:
        valor = float(input("Informe o preço do produto: R$"))
    except:
        while type(valor) != float:
            valor = float(input("Informe o preço do produto: R$"))
    dados[chave] = valor

    continuar = str(input("Continuar: "))
    if continuar in "Nn":
        break

print(dados)