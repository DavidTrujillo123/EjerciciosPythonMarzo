
def Imprimir(A):
    for i in range(len(A)):
        print("[",end="")
        for j in range(len(A)):
            print("%3s"%A[i][j],end="")
        print (" ]")

def comprobarGanador(tabla, simbolo):
    cont = 0
    cont2 = 0
    cont3 = 0
    for i in range(len(tabla)):
        cont = 0

        if(tabla[i].count(simbolo)==3):
            return True
        elif (tabla[i][i] == simbolo):
            cont2 += 1 

        for j in range(len(tabla)):
            if (tabla[j][i]== simbolo):
                cont+=1

            if(i+j == len(tabla)-1):
                if (tabla[i][j]== simbolo): 
                    cont3 +=1

        if cont == 3 or cont2 == 3 or cont3 == 3: return True           
    
    return False

tabla = [[" ","x","x"],
         [" "," "," "],
         [" ","x","x"]]

print(comprobarGanador(tabla,"x"))