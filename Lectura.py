a = open ('archivotexto.txt', 'r', encoding= 'utf-8')
texto = a.read()
a.close()

lista_de_nombres = texto.split ("\n") #.split() para pasar a una lista
buscador = input ("Quien desea saber si esta en la lista?: ")
#print (lista_de_nombres)
existe = False
"""
No considiera las mayusculas o minusculas
"""
for nombre in lista_de_nombres:
    if nombre.lower() == buscador.lower():
        existe = True

if existe:
    print ("* Si esta en la lista")
else:
    print("* No esta en la lista")

"""
Tiene en cuenta las mayusculas y minusculas
"""
#if buscador in lista_de_nombres:
#    print("* Si esta en la lista")
#else:
#    print("No esta en la lista")




#print (lista_de_nombres) #se puede llamar por campo con [].

