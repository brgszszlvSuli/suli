a=2
b=3
print("a:",a,"b:",b)
# Cseréljük meg a két változó értékét !!!

c=a
a=b
b=c

print("a:",a, "b:",b)

a,b = b,a

print("a:",a, "b:",b)