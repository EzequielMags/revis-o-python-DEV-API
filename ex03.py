n1 = float(input("Digite sua nota:"))
n2 = float(input("Digite sua nota:"))

m = (n1 + n2)/2
c = ""

def conceito():
    
    if m >= 9 and m <= 10:
        c = "A"

    elif m >= 7.5 and m < 9:
        c = "B"

    elif m >= 6 and m < 7.5:
        c = "C"

    elif m >= 4 and m < 6:
        c = "D"

    elif m >= 0 and m < 4:
        c = "E"

    return c

if conceito() == "A" or conceito() == "B" or conceito() == "C":
    print("Aprovado com conceito:", conceito())

elif conceito() == "D" or conceito() == "E":
    print("Reprovado com conceito:", conceito())
