lista1 = ["a","b","c","d","e"]
lista2 = ["c","e","f","t","g"]
listaTotal = lista1+lista2

solo1 = []
solo2 = []
ambas = []

for palabra in lista1:
    if(palabra in lista2):
        ambas = ambas + [palabra]
    else:
        solo1 = solo1 + [palabra]

for palabra in lista2:
    if (palabra not in lista1):
        solo2 = solo2 +[palabra]

print(lista1)
print(lista2)
print(ambas)
print(solo1)
print(solo2)

