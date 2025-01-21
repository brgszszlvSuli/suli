# a gép "gondol" számot és mi kitaláljuk
# "gondolás" = véletlen számmal történik
# Hányadik próbára találod ki?
import random

print("A gép gondol egy 1 és 10 közti számra. Találd ki!")

x = random.randint(1, 10)
megvan = False
proba = 0

while not megvan:
    proba += 1
    tipp = int(input("Mire gondoltam? "))
    if x == tipp:
        print(f"Megvan! {proba}. próbára kitaláltad, hogy {x}-re gondoltam.")
        megvan = True
    elif x < tipp:
        print("Kisebb")
    else:
        print("Nagyobb")