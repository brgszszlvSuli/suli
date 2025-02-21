# 2.fa
# A 'mondat' nevű változóban tárold el a következő mondatot:
# "A vakegér nem látja mit csinál a macska, ezért nyugodtan sétál bele a szájába."
# írasd ki, hány karaktert tartalmaz a mondat
# külön változóba számold meg, összesen hány kis+nagy "a" és "á" betű van a mondatban, és írasd ki formázottan

mondat = "A vakegér nem látja mit csinál a macska, ezért nyugodtan sétál bele a szájába."

# 1.
print(len(mondat))

# 2.

a = A = á = Á = 0

for i in mondat:
    if i == 'a':
        a += 1
    elif i == 'A':
        A += 1
    elif i == 'á':
        á += 1
    elif i == 'Á':
        Á += 1

print(
    f'"a" betűk száma: {a}\n"A" betűk száma: {A}\n"á" betűk száma: {á}\n"Á" betűk száma: {Á}')
