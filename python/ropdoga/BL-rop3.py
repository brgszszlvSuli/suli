# 3.fa
# Készítsd el a 'szinek' listát, melyben 4-5 színt tárolj le.
# Ezek után, hajtsd végre a következő feladatokat:
# billentyűzetről kérj be 1 színt, ellenőrizd, hogy szerepel-e a listában, és ezt írasd ki.
# amennyiben nincs benne, akkor vedd fel a lista végére
# a színeket addig kérd be a billentyűről, míg '0' (Nulla) karaktert nem ütünk le. Ekkor listázza a színeket.

szinek = ["zöld", "kék", "piros", "barna", "narancs"]

1.
szin = input("Írj be egy színt: ")
if szin in szinek:
    print(szin)
else:
    print(szin)
    szinek.append(szin)
print(*szinek)

# 2.
while True:
    szin = input("Írj be egy színt: ")
    if szin in szinek:
        print(szin)
    else:
        szinek.append(szin)
    if szin == '0':
        szinek.remove("0")
        break
print(*szinek)
