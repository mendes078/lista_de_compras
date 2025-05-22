import pandas as pd

dados = {}

while True:
    chave = str(input("Informe o nome do produto: ")).strip()
    try:
        valor = float(input("Informe o preço do produto: R$"))
    except ValueError:
        print("O tipo de valor inserido não foi aceito!")
        valor = float(input("Informe o preço do produto corretamente: R$"))

    dados[chave] = valor
    print(f"O item {chave} custando R${valor} reais foi adicionado a lista com sucesso!")

    continuar = str(input("Deseja continuar? Digite S (Sim) ou N (Não): ")).strip()[0]
    if continuar in "Nn":
        break

    while continuar not in "SsNn":
        continuar = str(input("O valor inserido está incorreto! Digite S (Sim) ou N (Não): ")).strip()[0]
        if continuar == "Nn":
            break
print(dados)