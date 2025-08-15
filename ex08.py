from os import name
import requests

pais = str(input("Digite o nome do país: "))
url = f"https://restcountries.com/v3.1/name/{pais}"
response = requests.get(url)
dados = response.json()


for pais in dados:
    
    nome_do_pais = pais["name"]["common"]
    pegandoAlingua= list(pais["languages"])[0]
    lingua_do_pais = pais["languages"][pegandoAlingua]
    regiao_do_pais = pais['region']
    subregiao_do_pais = pais["subregion"]
    capital_do_pais = pais["capital"]
    sigla_da_moeda = list(pais["currencies"])
    codigo_moeda = list(pais["currencies"])[0]
    name_true_pais = pais["currencies"][codigo_moeda]["name"]
    simbolo_da_moeda = pais["currencies"][codigo_moeda]["symbol"]
    paises_fronteira = pais["borders"]
    

    print(name_true_pais)

    print(f"nome do país: {nome_do_pais}")
    print(f"lingua do país: {lingua_do_pais}")
    print(f'regiao do país: {regiao_do_pais}')
    print(f'subregiao do país: {subregiao_do_pais}')
    print(f'capital do pais: {capital_do_pais}')
    print(f'sigla da moeda: {sigla_da_moeda}')
    print(f'name: {name_true_pais}')
    print(f'simbolo da moeda: {simbolo_da_moeda}')
    print(f'países que fazem fronteira: {paises_fronteira}')

