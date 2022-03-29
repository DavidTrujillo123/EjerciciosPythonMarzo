from random import Random


import random
from random import randint

zonaUsuario = int(input ("¿En que zona desea disparar?: "))
zonaPortero = randint(1,6)
#random()   numero aleatorio entre 0 y 1
#random(inicio, fin)    numero aleatorio entre "inicio" y "fin"
#randorange(inicio,fin,paso)    numero aleatorio entre "inicio" y "fin" con un paso 
#uniform(inicio,fin)  numero aleatorio de tipo flotante ente "inicio" y "fin"

print("Zona portero:",zonaPortero)
if(zonaUsuario == zonaPortero):
    print ("No ha sido gol") 
else: print ("Goool")
