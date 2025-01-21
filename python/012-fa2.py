# Határoztasd meg, két szám közötti összes szám összegét. A két számot kérje be a program.
# Határozd meg azt is, hogy hány számot adtunk össze.
# Ügyelj arra, hogy a kisebbtől a nagyobb számig számoljon, és mind2 szám legyen benne az összegben.
# Végül írasd ki: A 'a' és 'b' számok közötti 'db' szám összege: 'XXX'

a = int(input("Mennyi legyen az első szám? "))
b = int(input("Mennyi legyen az utolsó szám? "))
n = b - a + 1
osszeg = (n/2)*(a+b)
print(f"A(z) {a} és {b} számok közötti {n-1} szám összege: {osszeg}")