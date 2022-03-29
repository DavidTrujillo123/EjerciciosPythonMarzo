nivel = 5
espacios = nivel

for i in range(nivel):
    for j in range (espacios+1):
        print("   ",end="")

    for k in range (2*i+1):
        print(" * ",end="")
    
    espacios -=1
    print("")
