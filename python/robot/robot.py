# EEEKDKEKDKEKDDNN

# 1. fa
szo = "EEEKDKEKDKEKDDNN"
print(szo)

# 2. fa
eszam = szo.count("E")
kszam = szo.count("K")
dszam = szo.count("D")
nszam = szo.count("N")
print(
    f"E betűk száma: {eszam}\nK betűk száma: {kszam}\nD betűk száma: {dszam}\nN betűk száma: {nszam}")

# 3. fa
ek = eszam-dszam
dk = dszam-eszam
kk = kszam-nszam
nk = nszam-kszam
# print(f"Legrovidebb parancs: ", end="")

# if ek > 0:
#     print("E"*ek, end="")
# elif ek < 0:
#     print("D"*dk, end="")
# if kk > 0:
#     print("K"*kk, end="")
# else:
#     print("E"*ek, end="")

kiir = "E"*ek+"D"*dk+"N"*nk+"K"*kk
print(f"Legrovidebb parancs: {kiir}")
