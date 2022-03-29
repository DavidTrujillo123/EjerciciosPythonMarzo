n = 100

print ("Numero:",n)
for i in range (1,n+1,1):
    if(i % 3 == 0 and i % 5 == 0): print(i,"FizzBuzz")
    elif (i%3==0): print(i,"Fizz")
    elif (i%5==0): print(i,"Buzz")

