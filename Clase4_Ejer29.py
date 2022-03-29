
def Imprimir (dic):
    for indice in dic:
        print("Key:",indice,"Valor:",dic[indice])
    print("")

dic = {}
dic ["pan"]=0.12

total = 0
menu = True
while(menu):
    op = int(input("Digite una opcion:\n1.Agregar producto \n2.Factura \n3.Salir \nOpcion: "))
    if (op == 1):
        indice = input("Ingrese el indice: ")
        valor = float(input("Ingrese el valor: "))
        dic[indice] = valor
        print(dic,"\n")
    elif(op == 2):
        
        factura = True
        Imprimir(dic)
        while(factura):
            print ("Elija una opcion\n1.Agregar Factura\n2. Finalizar\nOpcion:",end="")
            opf = int(input())

            if (opf == 1):
                indice = input("Ingrese el indice: ")
                cantidad = int (input("Ingrese el valor: "))

                if(dic.get(indice)is None):
                    print("Producto no encontrado...\n")
                else:
                    total += dic.get(indice)*cantidad
                    print ("El totale es:",total,"\n")

            else:
                factura = False
                total = 0
            
    elif(op == 3):
        menu = False
        print("\nSaliendo...")
    else: print("Ingrese una opcion valida...")