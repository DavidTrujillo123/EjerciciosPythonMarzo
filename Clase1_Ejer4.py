peso = float (input ("Digite su peso en kg: "))
altura = float(input("Digite su altura: "))

imc = peso / altura**2

print("Su imc es: %3.2f"%imc, altura, peso)
