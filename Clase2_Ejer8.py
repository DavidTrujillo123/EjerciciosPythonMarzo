horasTrabajador = 49
jornada = 48
pagoHora = 2
pagoExtra = 3.5

if horasTrabajador <= jornada:
    salario = horasTrabajador*pagoHora
else:
    salario = (jornada*pagoHora)+((horasTrabajador-jornada)*pagoExtra)

print ("Su salario es:",salario)