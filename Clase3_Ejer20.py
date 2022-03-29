A = [1,3,5,7,1,8,5,8,1,1,3,3]

for i in range (len(A)-1,-1,-1):
    print (A)
    if(A[i] in A[:i]): # lista [inicio : fin]
        del(A[i])
        