saldo = 300.45
opcion = 1

while(opcion != 3):
    print("Saldo Actual:",saldo)

    opcion = int(input("Digite una opcion: \n1. Deposito\n2. Retiro\n3. Salir\nOpcion:"))

    if(opcion<0 and opcion >3):
        print("Digite una opcion valida")
        continue

    if(opcion==1): 
        deposito = float(input("Digite la cantidad: "))
        saldo+=deposito
    elif(opcion == 2):
        retiro = float(input("Digite la cantidad: "))
        if(retiro>saldo): print("No puede retirar esa cantidad...")
        else:
            saldo -= retiro
            print("Retiro exitoso...")    
    elif(opcion == 3):
        print("Saldo Total:",saldo)
        print("Saliendo...")
    print()