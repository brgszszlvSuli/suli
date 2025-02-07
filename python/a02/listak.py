diakok = ["Anna", "Barna", "Cili", "Dani", "Elek"]
# diakok.append("Béla")
# # diakok += diakok
# diakok.remove("Barna")
# diakok.insert(2, "Zoli")
# print(*diakok)
# print(diakok[2])
# bővítsd a listát bevitellel amíg 'V' betűt nem írsz be

while True:
    bevitel = input('Írj be egy szót, "v"-vel vége: ')
    if bevitel != 'v':
        diakok.append(bevitel)
    else:
        print(*diakok)
        break


# diakok.sort()
# print(*diakok)
# diakok.sort(reverse=True)
# # diakok.reverse()
# print(*diakok)
