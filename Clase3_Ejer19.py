lista = [1,"Hola",3.5,False]

while len(lista)>0:
    print(lista)
    elem = int(input("Ingrese la posision del elemento a eliminar: "))
    if(elem>len(lista)-1):
        print("El elemento esta fuera del rango\n")
        continue
    del(lista[elem])
    print("Elemento eliminado\n")

