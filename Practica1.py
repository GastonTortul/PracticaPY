lista = []
num = 1
while num <= 100:
    if(num%2==0):
        print(num)
    else:
        if(num%3==0):
            print(num*2)
        elif(num%5==0):
            lista.append(num)
    num+=1
    
print(lista)
