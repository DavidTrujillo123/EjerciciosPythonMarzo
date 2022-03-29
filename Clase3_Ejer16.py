import random
from random import randint

def Imprimir (op):
    if (op == 1):
        r = "Piedra"
    elif (op == 2):
        r = "Papel"
    elif (op == 3):
        r = "Tijera"    
    return r

ganadas = 0
ganaMaquina = 0
while(ganadas<3 and ganaMaquina<3):
    opUser = int (input("Digite una opcion:\n1.-Piedra\n2.-Papel\n3.-Tijera\nOpcion:"))
    opMaquina = randint(1,3)

    if (opUser >3 or opUser<1):
        print("Digite una opción valida")
        continue #Nos regresa al inicio del ciclo saltandose la el resto del codigo

    print ("Usted eligio: "+Imprimir(opUser))
    print ("La maquina eligió: "+Imprimir(opMaquina))

    if(opUser == 1 and opMaquina == 3) or (opUser == 2 and opMaquina==1) or (opUser == 3 and opMaquina==2):
        print ("Gana el usuario")
        ganadas +=1
        
    elif(opUser == opMaquina):
        print("Es un empate")
    else:
        print ("Gana la maquina")
        ganaMaquina+=1
    print("Ganadas Usuario:",ganadas,"\nGanadas Maquina:",ganaMaquina,"\n")
    

