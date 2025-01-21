# kérjünk be 5 számot, és írassuk ki a legnagyobbat!

x = int(input("Hány számod van: "))
for _ in range(1, x+1):
    sz = int(input("Szám= "))
    leg = 0
    if sz > leg:
        leg = sz
print(f"A legnagyobb szám a(z) {leg} volt")
