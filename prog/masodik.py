import random
geptipp = random.randint(1,100)
print("Üdv aszámkitalálóban!")
print("Én a ", geptipp," számra gondoltam")
talalt = 0
while talalt == 0:
    print("Kérem a tippet")
    usertipp = int(input())
    print("Az ön tippje: ", usertipp)
    if usertipp > geptipp:
        print("Gondolt szám kisebb")
    if usertipp < geptipp:
        print("Gondolt szám nagyobb")
    if usertipp == geptipp:
        print("Talált")
        talalt = 1
print("VÉGE")
