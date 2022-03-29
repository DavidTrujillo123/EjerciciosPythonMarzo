resCorrectas = int (input ("Digite las respuestas correctas: "))
resIncorrectas = int (input ("Digite las respuestas correctas: "))

total = resCorrectas+resIncorrectas

pCorrecto = (100/total)*resCorrectas
pErrores = (100/total)*resIncorrectas

print("Su puntaje final es: "+str(resCorrectas)+"/"+str(total))
print ("Porcentaje correctos: %.2f"%pCorrecto,"%")
print ("Porcentaje incorrectos: %.2f"%pErrores,"%")