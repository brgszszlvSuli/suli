# Minden program legyen "felhasználóbarát", azaz mindent írjon ki a képernyőre!
# A program kérje be egy kör sugarát, majd számolja ki annak kerületét és területét. (a pi=3.14 legyen)
# A két értéket 1 tizedesjegyre kerekítve írja ki!
# input, print, =, round
# terület: T = r2 ∙ π
# kerület: K = 2 ∙ r ∙ π
pi = 3.14

print("Számoljuk ki a kör területét és kerületét.")

sugar = int(input("Mekkora a kör sugara? "))
terulet = sugar*sugar*pi
kerulet = 2*sugar*pi

print(f"A kör területe: {round(terulet, 1)}\nA kör kerülete: {round(kerulet, 1)}")