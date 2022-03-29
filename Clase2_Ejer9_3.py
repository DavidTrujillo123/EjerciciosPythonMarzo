hora = 20
min = 59
seg = 59

print(str(hora)+"h "+str(min)+"min "+str(seg)+("seg"))

if(seg==59):
    seg = 0
    if(min==59):
        min = 0
        if(hora == 23):
            hora = 0
        else: hora+=1
    else: min+=1
else: seg+=1

print(str(hora)+"h "+str(min)+"min "+str(seg)+("seg"))