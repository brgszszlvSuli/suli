# addig kérjük be a számokat amíg 0-t nem ütünk és írjuk ki a legnagyobbat
leg = 0
szam = -1
while szam != 0:
    szam = int(input("Szám = "))
    if szam > leg:
        leg = szam

print(f"A legnagyobb szám a(z) {leg} volt.")
