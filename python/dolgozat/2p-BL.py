import random

szo1 = str(input("1. szó: "))
szo2 = str(input("2. szó: "))
szo3 = str(input("3. szó: "))

szam = random.randint(1, 9)

for i in range(1, szam+1):
    print(szo1, end=" ")
print(end=None)
for i in range(1, szam+1):
    print(szo2, end=" ")
print(end=None)
for i in range(1, szam+1):
    print(szo3, end=" ")
