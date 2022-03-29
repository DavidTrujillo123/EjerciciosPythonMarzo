def Imprimir(A):
    for indice in A:
        print("Key:",indice,"Value:",A[indice],",Promedio->",Promedio(A[indice][1]))
    print()  

def AgregarEstudiante(dic,codigo,nombre):
    dic[codigo] = []
    dic[codigo].append(nombre)
    dic[codigo].append([])

def AgregarNotas(dic,codigo,nota):
    dic[codigo][1] += [nota]

def Promedio(lista):
    suma = 0
    for item in lista:
        suma+=item
    return suma/len(lista)

dic = {}
# Imprimir(dic)
AgregarEstudiante(dic,"123","kevin")
AgregarNotas(dic,"123",10)
AgregarNotas(dic,"123",8)
Imprimir(dic)


while(True):
    opcion = int( input("Digite una opcion: \n1.Agregar Estudiante \n2.Agregar Notas \n3.Consultar Informacion \n4.Salir \nOpcion:"))
    print()
    if(opcion == 1):
        codigo = input("Digite el nuevo codigo del estudiante:")
        nombre = input("Digite el nombre del nuevo estudiante:")
        AgregarEstudiante(dic,codigo,nombre)
        print("Estudiante agregado...\n")
    elif(opcion == 2):
        while(True):
            opf = int(input("\nDigite una opcion \n1.Agregar Notas Nuevamente \n2.Salir \nOpcion: "))
            print()
            if(opf == 1):
                    codigo = input("Digite el codigo del estudiante: ")
                    while(True):
                        nota = int(input("Digite la nota del estudiante o -1 para salir: "))
                        if (nota == -1): break
                        AgregarNotas(dic,codigo,nota)
            elif (opf == 2): break
    elif(opcion == 3):
        Imprimir(dic)
    elif(opcion == 4):
        break
 