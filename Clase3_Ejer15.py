
def Vasos(vasoUsado, factor):
    total = 0
    while(vasoUsado >= factor):
        reciclado = vasoUsado//factor
        sobran = vasoUsado % factor
        total += reciclado
        print ("Vasos Usados:",vasoUsado," Reciclados:",reciclado," Sobran:",sobran," Total reciclados:",total)
        vasoUsado = reciclado + sobran
    return total

vasoUsado = 60
factor = 8

Vasos(vasoUsado, factor)
