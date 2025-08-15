import requests 



cep = input("Digite o CEP: ")
url = f"https://viacep.com.br/ws/{cep}/json/"
response = requests.get(url)
dados = response.json()
print(f"Bairro: {dados['bairro']}, {dados['localidade']} - {dados['uf']}")

if dados["localidade"] != "São Paulo":
    print("CEP não é de São Paulo.")



area = cep[:5]
if area < "1600":
    print("Região: Sul")
elif area < "3000":
    print("Região: Norte")  
elif area < "6000":
    print("Região: Leste")
elif area < "8000":
    print("Região: Oeste")