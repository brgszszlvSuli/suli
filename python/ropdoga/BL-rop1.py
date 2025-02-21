# 1.fa
# Készítsd el a 'napok' listáját, melyben a hét minden napja sorrendben szerepeljen, majd írasd ki a következőket:
# az utolsó napot
# a hét 3.-5. napjáig a napokat
# fordítva a napokat

napok = ["hétfő", "kedd", "szerda", "csütörtök",
         "péntek", "szombat", "vasárnap"]

# 1.
print(*napok[len(napok)-1])

# 2.
print(*napok[2:5])

# 3.
napok.reverse()
print(*napok)
