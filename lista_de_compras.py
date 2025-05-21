import pandas as pd

dados = {}

while True:
    try:
        chave = str(input("Informe o nome do produto: ")).strip()
        valor = float(input("Informe o preço do produto: "))
    except ValueError:
        print("O tipo de valor está incorreto. Tente novamente.")