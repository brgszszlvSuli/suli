# 1. beírt szó hosszának meghatározása
# 2. a szó kiíratása szóközekkel
# 3. sorbarendezni a lista elemeit
# 4. alakítsuk át "szögediesre" (e -> ö)
# 4.a palóc (a->á)
# 5. megszamoljuk az a és e betűket

# szo = str(input("Adj meg egy szót: "))
szo = "elmentem a piacra es vettem kenyeret"
hossz = len(szo)
# print(f"A(z) {szo} szó {hossz} betűből áll.")
# print(szo[0:4])
# print(szo[4:10])
print(szo[::-1])


for b in szo:
    if b == 'e' or b == 'a':
        if b == 'e':
            b = 'ö'
        else:
            b = 'á'
    print(b.upper(), end="")

rend = sorted(szo, reverse=True)
# print("\n", rend)
a = szo.count("a")
e = szo.count("e")
print()
print(szo.upper())
print(f"{a} db 'a' betű és {e} db 'e' betű van a szóban")
