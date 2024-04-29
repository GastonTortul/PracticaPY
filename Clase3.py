lista = [1, "Texto", 3.8, True, 5, 6, 7, 8, 9, 10] #lista de 1 al 10, lista = array
texto = "Texto"
#print(lista)
#print(lista[2])
#print (texto[2]) # [i] trae el valor del indice
#print(texto[0:2]) #[i:x] el valor X no incluye
#print(texto [2:]) #[x:] desde X hasta el final
#print(texto[::2]) # [::x] silce, salta de 2 en 2 en este caso
numero = 0

lista2 = []
while numero < 16 :
    lista2.append(numero)
    
#print(lista2)
    if ((lista2[numero]%3) == 0) and ((lista2[numero]%5) == 0):
            print ("FizzBuzz")
    elif (lista2[numero]%3) == 0:
        print ("Fizz")
    elif (lista2[numero]%5) == 0:
        print ("Buzz")
    else: print (lista2[numero])
    numero = numero + 1 