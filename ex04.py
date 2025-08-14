notas = []
alunos = 0 
gabarito = {
    1: 'b',
    2: 'a',
    3: 'd',
    4: 'c',
    5: 'a',
    6: 'b',
    7: 'd',
    8: 'a',
    9: 'b',
    10: 'b'
}


def questoes():
    nota = 0
    j = 1  

    for _ in range (1,11):
        resposta = str(input(f"pergunta {j}, Digite sua resposta: "))
        if resposta == gabarito[j]:
            nota +=1
        
        j += 1 

    
    
    notas.append(nota)



a = 1

while a > 0:
    pergunta = str(input("Ainda tem aluno? s/n "))

    if pergunta == "s":
        alunos += 1
        questoes()

    elif pergunta == "n":
        a = -1

menor = 10
maior = 0 


for notaDoAluno in notas:

    if notaDoAluno < menor: 
        menor = notaDoAluno  



    if notaDoAluno > maior: 
        maior = notaDoAluno 



print(f"as notas são: {notas}")
print(f"a menor nota é: {menor}")
print(f"a maior nota é: {maior}")
print(f'a quantidade de alunos é: {alunos}')