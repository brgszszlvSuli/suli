a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

# if a > b:
#     if a > c:
#         print('A legnagyobb szám:', a)
#     if a < c:
#         print('A legnagyobb szám:', c)
# elif b > a:
#     if b > c:
#         print('A legnagyobb szám:', b)
#     if b < c:
#         print('A legnagyobb szám:', c)
# else:
#         print('A legnagyobb szám:', c)

if a>b:
    n=a
else:
    n=b
if n<c:
    n=c

print("A legnagyobb szám:",n)