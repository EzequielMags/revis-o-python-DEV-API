salario = float(input("Digite o seu salario: "))
ano = 1996 

percentual = 1.5
aumento = (salario * percentual / 100 )
contador = 1

while contador > 0:
    ano += 1 
    percentual *= 2 
 
    aumento = (salario * percentual / 100 )
    salario_atualizado = salario + aumento

    print(f'no ano de {ano}, o salario aumentou para {salario_atualizado}')

    pergunta = str(input("Deseja passar mais um ano? s/n "))

    if pergunta == 's':
        contador = 1 
    
    elif pergunta == 'n':
        contador = -1