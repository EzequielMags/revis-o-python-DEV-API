valores = []

while True:
    try:
        num = int(input("Digite um valor (-1 para sair): "))
        if num == -1:
            break
        valores.append(num)
    except ValueError:
        print("Por favor, digite um número inteiro válido.")

print(f"\nQuantidade de valores lidos: {len(valores)}")

print("Valores na ordem informada:", ' '.join(str(v) for v in valores))

print("Valores na ordem inversa:", ' '.join(str(v) for v in reversed(valores)))

soma = sum(valores)
print(f"Soma dos valores: {soma}")

media = soma / len(valores) if valores else 0
print(f"Média dos valores: {media:.2f}")

acima_media = sum(1 for v in valores if v > media)
print(f"Quantidade de valores acima da média: {acima_media}")