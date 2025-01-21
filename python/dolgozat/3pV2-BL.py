szam = int(input("Adj meg egy egyjegyű számot: "))

hiba = ["kicsi", "nagy"]
if szam > 9:
    print(f"Túl {hiba[1]} a szám!")
elif szam <= 0:
    print(f"Túl {hiba[0]} a szám!")

szamolas = 0
for i in range(1, szam+1):
    szamolas += i
    if i == szam:
        print(i, end="=")
        print(szamolas)
        break
    print(i, end="+")
