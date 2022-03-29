from random import randint

def Imprimir(A):
    for fila in tabla:
        print("[",end="")
        for columna in fila:
            print("%3s"%columna,end="")
        print (" ]")

def llenar(n):
    tabla = []
    for i in range (n):
        tabla.append([])
        for j in range (randint(1,n)):
            tabla[i] += [randint(1,10)]
    return tabla

tabla = llenar(10)
Imprimir(tabla)
