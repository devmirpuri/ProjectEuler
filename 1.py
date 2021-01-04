multiples_3_list=[]
multiples_5_list=[]
multiples_15_list=[]

for multiples_3 in range(0,1000):
    if (multiples_3 % 3 == 0):
        multiples_3_list.append(multiples_3)
x = sum(multiples_3_list)

for multiples_5 in range(0,1000):
    if (multiples_5 % 5 == 0):
        multiples_5_list.append(multiples_5)
y = sum(multiples_5_list)

for multiples_15 in range(0,1000):
    if (multiples_15 % 15 == 0):
        multiples_15_list.append(multiples_15)
z = sum(multiples_15_list)

print(x + y - z)
