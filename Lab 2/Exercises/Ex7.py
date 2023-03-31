a = int(input())
if a < 100:
    a *= 3
    a -= 200
    print(a)
elif a > 100:
    a /= 2
    a += 20
    print(a)
else:
    print("It's 100!")
