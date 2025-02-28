print("SZólétra játék")
print("Milyen hosszú legyen a szó?")
hossz = int(input())  # 4
print("Kérem a szót!")
elozoszo = input()  # alma

while True:
    if len(elozoszo) != hossz:
        print(f"Hosszhiba!")
        break
    print("Kérem a szót!")
    kovetkezoszo = input()
    if kovetkezoszo[0] != elozoszo[-1]:
        print("Létrahiba")
        break
    elozoszo = kovetkezoszo
print("Játék vége")
