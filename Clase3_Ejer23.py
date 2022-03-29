A = [80,34,80,23,70]

mayor = 0 
k = 150
for i in range(len(A)):
    for j in range (i+1,len(A)):
        suma = A[i]+A[j]

        if(suma <= k):
            print(A[i],"+",A[j],"->",suma)
            if (mayor < suma):
                mayor = suma
print ("El paso mayor es:",mayor)
