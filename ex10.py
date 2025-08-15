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
    print("Região: Zona Centro")
elif area < "3000":
    print("Região: Zona Norte")  
elif area < "4000" or area >= "8000":
    print("Região: Zona Leste")
elif area < "4900":
    print("Região: Zona Sul")
elif area < "6000":
    print("Região: Zona Oeste")