dic = {}
indice = "Nombre"
valor = "David"

dic[indice] = valor
#dic.setdefault(indice, valor) Ambas formas funcionana para dar un indice y un valor

menu = True

while(menu):
    op = int(input("Digite una opcion:\n1.Agregar\n2.Salir\nOpcion: "))
    if (op == 1):
        indice = input("Ingrese el indice: ")
        valor = input("Ingrese el valor: ")
        dic[indice] = valor
        print(dic)
    elif(op == 2):
        menu = False
        print("\nSaliendo...")
    else: print("Ingrese una opcion valida...")

