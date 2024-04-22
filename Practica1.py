numero = 1
lista = []

while numero <= 100 :
    lista.append(numero)

    if (lista[numero]%2) != 0 and (lista[numero]%3) == 0:
        numero = numero * 2
        print (numero)
    elif (lista[numero]%2) != 0 and (lista[numero]%5) == 0:
        print
    else:
        print(numero)

    numero = numero + 1
print[lista]
