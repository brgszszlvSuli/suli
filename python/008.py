# Átlagszámítás
print("Átlagszámoló program")
n = int(input("Hány jegyed van: "))
osszeg = 0
for i in range(1, n+1):
    kiir = "Add meg a " + str(i) + ". jegyed: "
    jegy = int(input(kiir))
    osszeg += jegy
atlag = round(osszeg / n, 2)
print("Az átlagod:", atlag)