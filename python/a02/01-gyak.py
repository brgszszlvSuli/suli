# 1.gy: Kérj be egy szót, és
# írsad ki minden 2. betűjét
# írasd ki a szó első, és utolsó betűit

szo = str(input("Addj meg egy szót: "))
print(szo[::2])
betu = 0

for i in szo:
    betu += 1
    if betu == 1 or betu == len(szo):
        print(i, end="")
