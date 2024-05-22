def maximum(a, b, c):
    if a > b:
        aux = a
    else:
        aux = b
    if c > aux:
        return c
    else:
        return aux


print(maximum(1, 2, 3))
print(maximum(2, 1, 3))
print(maximum(3, 2, 1))
