def Imprimir(A):
    for i in range(len(A)):
        print("[",end="")
        for j in range(len(A)):
            print("%3s"%A[i][j],end="")
        print (" ]")

def llenarVacio(n):
    tabla = []
    for i in range (n):
        tabla.append([])
        for j in range (n):
            tabla[i] += [""]
    return tabla

def asteriscos (tabla, simbolo):
    for i in range(len(tabla)):
        for j in range(len(tabla)):
            if (i == len(tabla)//2) or (j == len(tabla)//2) or (i==j) or (i+j == len(tabla)-1):
                tabla[i][j] += simbolo 

n = 2001
if (n % 2 == 0 ):
    print("La longitud debe ser impar")
else :
    tabla = llenarVacio(n)
    asteriscos(tabla,"*")
    Imprimir(tabla)