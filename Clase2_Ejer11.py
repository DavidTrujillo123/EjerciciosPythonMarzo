anioInicio = 1800
anioFin = 2022
print ("Los años bisiestos ente "+str(anioInicio)+" y "+str(anioFin)+" son: ")
for i in range(anioInicio, anioFin):
    if(i % 4 == 0 and i%100!=0) or i%400==0:
        print (i)
           

  

