# kő-papír-olló játék

import random
print("kő-papír-olló-játék")
kpo = ["kő", "papír", "olló"]
gep = en = kor = 0
hany = 3
while en != hany and gep != hany:
    kor += 1
    gepv = random.randint(0, 2)
    env = int(input("Te választásod (012-kpo): "))
    if (gepv+1 == env) or ((gepv == 2) and (env == 0)):
        en += 1
    elif gepv != env:
        gep += 1
    print(f"gép: {kpo[gepv]} - Te: {kpo[env]}. Állás: {gep}:{en}")

print(f"A végeredmény gép: {gep} - Te: {en} lett")
if gep > en:
    print(f"A gép nyert {kor} kör alatt")
else:
    print(f"Te nyertél {kor} kör alatt")
print("V É G E")
