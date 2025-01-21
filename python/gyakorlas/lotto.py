# készíttess LOTTÓ számokat (1-90-ből 5 szám)

import random
for _ in range(1, 6):
    szam = random.randint(1, 90)
    print(szam, end=" ")
