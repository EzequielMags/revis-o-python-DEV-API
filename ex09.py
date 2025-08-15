import requests
primeira_moeda = str(input("Digite a sigla da primeira moeda: ")).upper()
segunda_moeda = str(input("Digite a sigla da segunda moeda: ")).upper()

url = f"https://api.exchangerate-api.com/v4/latest/{primeira_moeda}"
response = requests.get(url)
dados = response.json()

todas_as_moedas = dados["rates"]

for moeda in todas_as_moedas.items():
    if moeda[0] == segunda_moeda:
        print(f"A cotação de {primeira_moeda} para {segunda_moeda} é: {moeda[1]}")