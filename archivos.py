archivo = open ("Persona.txt", "w") #si no existe el archivo lo crea
archivo.write("Agus Tortul")
archivo.close()

archivo_escrito = open('Persona.txt', 'r')
texto_del_archivo_escrito = archivo_escrito.read() #.read() para leer el archivo
archivo_escrito.close()
#print (texto_del_archivo_escrito) 


archivo2 = open ("HolaMundo.txt", "w")
archivo2.write('Hola Mundo!')
archivo2.close()

archivo2 = open ("HolaMundo.txt", "r")
#print (archivo2.read())
archivo2.close()


a3 = open ('archivotexto.txt', 'a', encoding= 'utf-8') #'a' si no existe el archivo tambien lo crea
                                                       # encoding= 'utf-8' para que se vean las tildes1
while True:
    print ("------------------------------")
    print("\n1. Ingrese un nuevo nombre")
    print("2 Para salir\n")
    print ("------------------------------")
    op = input('Ingrese una opcion: ')
    print ("------------------------------")
    if op == '2':
        break
    
    nombre = input("\nIngrese el nombre de la persona: ")
    a3.write(f"{nombre} \n")

a3.close()

