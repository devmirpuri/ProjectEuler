factors=[]
prime_factors=[]

for number in range(1,775146):
    if 600851475143 % number == 0:
        factors.append(number)

for num in factors:
    y = 1
    for x in range(2,num):
        if num % x == 0:
            y = 0
            break
    if y == 1:
        prime_factors.append(num)

print(max(prime_factors))