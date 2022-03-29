dias = int (input ("Digite los dias: "))
anio = dias // 365
meses = (dias % 365)//30
semanas = (dias - (anio*365 + meses*30))//7
dias2 = dias - (anio*365+meses*30+semanas*7)
print(dias2,"dias",semanas,"semanas",meses,"meses",anio,"años")