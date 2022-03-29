from random import randint


aciertos = 0

while(True):
    op = randint(1,3)
    num1 = randint(1,10)
    num2 = randint(1,10)

    if(op == 1):
        print (num1,"*",num2)
        res = num1*num2
        resUsuario = int(input("Ingrese su respuesta: "))
        if(res != resUsuario):
            print("Incorrecto la respuesta era:",res)
            break
        else: 
            print("Correcto...")
            aciertos +=1
    elif(op == 2):
        print (num1,"+",num2)
        res = num1+num2
        resUsuario = int(input("Ingrese su respuesta: "))
        if(res != resUsuario):
            print("Incorrecto la respuesta era:",res)
            break
        else: 
            print("Correcto...")
            aciertos +=1
    elif(op == 3):
        print (num1,"/",num2)
        res = num1//num2
        resUsuario = int(input("Ingrese su respuesta: "))
        if(res != resUsuario):
            print("Incorrecto la respuesta era:",res)
            break
        else: 
            print("Correcto...")
            aciertos +=1
    res = 0
    print()
   
print ("\nTotal de aciertos:",aciertos)
