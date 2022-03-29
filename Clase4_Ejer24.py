def Imprimir(A):
    for i in range(len(A)):
        print("[",end="")
        for j in range(len(A)):
            print("%3s"%A[i][j],end="")
        print (" ]")

def llenarSecuencial(n):
    tabla = []
    cont = 1
    for i in range (n):
        tabla.append([])
        for j in range (n):
            tabla[i] += [cont] 
            cont +=1
    return tabla

tabla = llenarSecuencial(5)
Imprimir(tabla)

