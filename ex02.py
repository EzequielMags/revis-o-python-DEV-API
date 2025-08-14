def calcularNotas(valor):
    notas = []
    total = 0 
    i = 0
    k = 0 
    while i == 0:
        while total < valor:
            cem = 100
            cinquenta = 50 
            dez = 10 
            cinco = 5 
            um = 1

            if total + cem <= valor:
                
                total += cem
                notas.append(cem)

            elif total + cem > valor:
                if total + cinquenta <= valor:
                    total += cinquenta
                    notas.append(cinquenta)

                elif total + cinquenta > valor:
                    if total + dez <= valor:
                     total += dez
                     notas.append(dez)

                    elif total + dez > valor:
                        if total + cinco <= valor:
                            total += cinco
                            notas.append(cinco)
                        
                        elif total + cinco > valor:
                            if total + um <= valor:
                             total += um
                             notas.append(um)


         
        
        i = -1   
    print(notas)


valorDoSaque = int(input("Digite o valor do saque: "))


if valorDoSaque >= 10 and valorDoSaque <= 600:
    calcularNotas(valorDoSaque)