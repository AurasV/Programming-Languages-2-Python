def cmmdc(a, b):
    while b:
        r = a % b
        a = b
        b = r
    return a


print(cmmdc(15, 30))
print(cmmdc(7, 24))
