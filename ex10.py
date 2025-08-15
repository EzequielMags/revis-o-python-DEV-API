import requests 

zonas_sp = {
    "norte": ["Santana", "Tucuruvi", "Jaçanã", "Tremembé", "Casa Verde", "Limão", "Freguesia do Ó", "Brasilândia"],
    "sul": ["Campo Limpo", "Capão Redondo", "Jardim Ângela", "Jardim São Luís", "Grajaú", "Parelheiros", "Marsilac"],
    "leste": ["Itaquera", "Penha", "São Mateus", "Guaianases", "Cidade Tiradentes", "Mooca", "Brás"],
    "oeste": ["Pinheiros", "Butantã", "Lapa", "Perdizes", "Vila Leopoldina", "Vila Madalena", "Barra Funda"],
    "centro": ["Sé", "Liberdade", "República", "Santa Cecília", "Consolação", "Bela Vista", "Vila Buarque"]
}


cep = input("Digite o CEP: ")
url = f"https://viacep.com.br/ws/{cep}/json/"
response = requests.get(url)
dados = response.json()
print(f"Bairro: {dados['bairro']}, {dados['localidade']} - {dados['uf']}")

if dados["localidade"] != "São Paulo":
    print("CEP não é de São Paulo.")

for zona in zonas_sp:
    if dados["bairro"] in zonas_sp[zona]:
        print(f"O bairro {dados['bairro']} pertence à zona {zona}.")
        break