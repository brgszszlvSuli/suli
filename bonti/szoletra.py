# bekérni egy számot
# annyi betűs szavat kell csinálni
# tovább a játék

szam = int(input("Hány betűsek legyenek a szavak? "))

utolsoBetu = ""
elsoBetu = ""
forFutas = 0
szo = input(f"Adj meg egy {szam} jegyű szót: ")

while True:
    szo = input(f"Adj meg egy {szam} jegyű szót: ")
    for _ in szo:
        forFutas += 1
        if forFutas == 1:
            elsoBetu = _
            print(elsoBetu)
    forFutas = 0

    if len(szo) != szam:
        print(f"A hossza nem {szam}. Kiestél")
        break
    elif elsoBetu != utolsoBetu:
        print(f"Az első betűd nem egyezik az utolsó betűddel.")
        break
    else:
        for i in szo:
            forFutas += 1
            if forFutas == len(szo):
                utolsoBetu = i
                print(utolsoBetu)
