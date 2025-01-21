# kérjünk be 3 számot (a,b,c), és írassuk ki a legnagyobbat

a = int(input("A: "))
b = int(input("B: "))
c = int(input("C: "))

if a > b:
    if a > c:
        print("A")
    else:
        print("C")
else:
    if b > c:
        print("B")
    else:
        print("C")