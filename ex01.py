def contaParaGasolina():
    litroGasolina = float(input("Digite a quantidade de litros: "))

    if litroGasolina <= 20:
        preco = 2.50 * litroGasolina  
        precoComDesconto =  preco - (preco * 4 / 100)
        print(f"preco com desconto: {precoComDesconto}")

    if litroGasolina > 20:
        preco = 2.50 * litroGasolina  
        precoComDesconto =  preco - (preco * 6 / 100)
        print(f"preco com desconto: {precoComDesconto}")


def contaParaAlcool():
    litroAlcool = float(input("Digite a quantidade de litros: "))

    if litroAlcool <= 20:
        preco = 1.90 * litroAlcool  
        precoComDesconto =  preco - (preco * 3 / 100)
        print(f"preco com desconto: {precoComDesconto}")

    if litroAlcool > 20:
        preco = 1.90 * litroAlcool  
        precoComDesconto =  preco - (preco * 5 / 100)
        print(f"preco com desconto: {precoComDesconto}")


print("1 - Gasolina, 2 - Alcool")

escolha = int(input("Digite aqui: "))

if escolha == 1:
    contaParaGasolina()

if escolha == 2:
    contaParaAlcool()

