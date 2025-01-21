# a. Készíttess Lottó számgenerátort.
# b. Kérdezd meg, hány sorozatot készítsen.
# c. 5-ös, és 6-os lottót is tudjon készíteni! (5-ös: 1-90 számokból 5-öt, 6-os: 1-45 számokból 6-ot)

import random

a = input("Melyik feladat legyen? ")

if a == 'a':
    gen = random.randint(1,90)
    print(gen)
elif a == "b":
    sorozat = int(input("Hány sorozatot készítsek? "))
    for i in range(1, sorozat+1):
            gen = random.randint(1,90)
            print(gen)
else:     
    tipus =int(input("Ötös vagy hatos lottó legyen?"))
    if tipus == 5:
        for i in range(1, 6):
            gen = random.randint(1,90)
            print(gen)
    if tipus == 6:
        for i in range(1, 7):
            gen = random.randint(1,45)
            print(gen)




# while genSzam != sorozat:
#     genSzam += 1
#     gen = random.randint(1,90)
#     print(gen)