numero = 0
lista = []

while numero < 101 :
    lista.append(numero)
    if (lista[numero]%2) != 0 and (lista[numero]%5) == 0:
        lista.append(numero)
    elif (lista[numero]%2) != 0 and (lista[numero]%3) == 0:
        numero = numero * 2
        print (numero)
    else:
        print(numero)
        
    numero = numero + 1
