# számoljuk ki jegyeink átlagát, akkor végzünk ha '0'-t írunk be
jegy = 1
osszeg = n = 0
while (jegy != 0):
    jegy = int(input("Jegyed: "))
    osszeg += jegy
    n += 1
n -= 1
atlag= round(osszeg/n, 2)
print("Átlag:", atlag)