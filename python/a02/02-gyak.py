# 2.gy: Legyen az alábbi mondat, a mondat változó értéke
# engem nem lehet elfelejteni
# Készíts programot, ami csak az e betű utáni betűket írja ki
# pl.: engem nem lehet elfelejteni -> nmmhtlljn

mondat = "engem nem lehet elfelejteni"
# hossz = len(mondat)

# for i in range(0, hossz):
#     if mondat[i] == 'e':
#         print(mondat[i+1], end=" ")

for i in range(len(mondat)):
    if mondat[i] == 'e':
        print(mondat[i+1], end=" ")
