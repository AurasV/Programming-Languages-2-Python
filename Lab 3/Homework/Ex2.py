def cmmdc(a, b):
    while b:
        r = a % b
        a = b
        b = r
    return a


def cmmmc(a, b):
    return (a * b) / cmmdc(a, b)


print(cmmmc(3, 5))
print(cmmmc(15, 241))
