import pandas as pd

dados = {}

while True:
    try:
        chave = str(input("Informe o nome do produto: ")).strip()
        valor = float(input("Informe o preço do produto: "))
    except ValueError:
        valor = float(input("Informe o preço do produto: "))
    break

print(chave)
print(valor)