# Hozd létre a "városok1" listát, és másold bele a következő elemeket:
# "Pécs", "Eger", "Nyúl", "Ajka", "Hencida", "Ozora", "Doboz", "Tinnye", "Kocs", "Napkor"
# Hozd létre a "városok2" listát, és másold bele a következő elemeket:
# "Salföld", "Sarud", "Som", "Sé", "Sonkád", "Sima", "Ajka"
# !!!!Először csak a "városok1" listával dolgozunk!!!!!
# 1.fa: Listázd ki az első 5 városnevet
# 2.fa: Szúrd be a végére "Budapest"-et
# 3.fa: Szúrd be Eger után "Mezőtúr"-t
# 4.fa: Rendez a listát növekvő sorba
# 5.fa: A "városok2"-t rendezd csökkenő sorba
# 6.fa: Bővítsd a "városok1" listát a "városok2"-vel
# 7.fa: Bővítsd a listát adatbevitellel, 3 további városnévvel
# 8.fa: Írasd ki a "városok2" lista elemeit ","-vel elválasztva egymás mellé,
#       alá pedig a "városok1" lista utolsó 10 elemét

varosok1 = ["Pécs", "Eger", "Nyúl", "Ajka", "Hencida",
            "Ozora", "Doboz", "Tinnye", "Kocs", "Napkor"]
varosok2 = ["Salföld", "Sarud", "Som", "Sé", "Sonkád", "Sima", "Ajka"]

# 1fa
print(*varosok1[0:5])

# 2fa
varosok1.append("Budapest")

# 3fa
varosok1.insert(2, "Mezőtúr")

# 4fa
varosok1.sort()

# 5fa
varosok2.sort(reverse=True)

# 6fa
varosok1 += varosok2

# 7fa
for i in range(3):
    bev = input("Városnév: ")
    varosok1.append(bev)

# 8fa

print(*varosok2, end=" ")
print(*varosok1[len(varosok1)-10:len(varosok1)])
