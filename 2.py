fibonnaci=[]
fibonnaci_even=[]

x,y = 0,1
while y<4000000:
    fibonnaci.append(y)
    x,y = y,x+y

for number in fibonnaci:
    if number % 2 == 0:
        fibonnaci_even.append(number)
    
print(sum(fibonnaci_even))