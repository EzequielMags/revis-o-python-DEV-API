menu = {
    100: ("Cachorro Quente", 1.20),
    101: ("Bauru Simples", 1.30),
    102: ("Bauru com ovo", 1.50),
    103: ("Hambúrguer", 1.20),
    104: ("Cheeseburguer", 1.30),
    105: ("Refrigerante", 1.00)
}

while True:
    try:
        codigo = int(input("Digite o código do item (ou 0 para sair): "))
        if codigo == 0:
            break
        if codigo not in menu:
            print("Código inválido. Tente novamente.")
            continue
        
        quantidade = int(input(f"Quantidade de {menu[codigo][0]}: "))
        if quantidade < 0:
            print("Quantidade não pode ser negativa. Tente novamente.")
            continue
        
        preco_total = menu[codigo][1] * quantidade
        print(f"Total: R$ {preco_total:.2f}")
    
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro válido.")