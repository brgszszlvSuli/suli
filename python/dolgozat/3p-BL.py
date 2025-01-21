szam = int(input("Adj meg egy egyjegyű számot: "))

hiba = ["kicsi", "nagy"]
if szam > 9:
    print(f"Túl {hiba[1]} a szám!")
elif szam <= 0:
    print(f"Túl {hiba[0]} a szám!")

futas = szamolas = 0
while 0 < szam <= 9 and futas != szam:
    futas += 1
    szamolas += futas
    if futas == szam:
        print(futas, end="=")
        print(szamolas)
        break
    print(futas, end="+")
