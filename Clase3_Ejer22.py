from random import randint

def LlenarseSec(n):
    lista = []
    for i in range(1,n+1):
        lista += [i]

    return lista

def llenarAlea(n):
    lista = []
    num = randint(1,n)
    lista +=[num]
    
    for i in range(n-1):
        while(num in lista):
            num = randint(1,n)
        lista += [num]
    return lista

n = 10000
listaA = LlenarseSec(n)
listaB = llenarAlea(n)

for i in range(n):
    print("La persona:",listaA[i], "le toca con:",listaB[i])


