print("SZólétra játék")
print("Milyen hosszú legyen a szó?")
hossz = int(input())  # 4
print("Kérem a szót!")
elozoszo = input()  # alma
pont = 0
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
    pont += 1
print("Játék vége")

print(pont)
if 0 >= pont <= 3:
    print("Alap")
elif 4 >= pont <= 10:
    print("Közép")
else:
    print("Profi")
