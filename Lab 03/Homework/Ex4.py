def fibonacci(a):
    n0 = 0
    n1 = 1
    if a == 1:
        print(0)
        return
    if a == 2:
        print(0)
        print(1)
        return
    print(n0)
    print(n1)
    for i in range(2, a):
        n2 = n0 + n1
        n0 = n1
        n1 = n2
        print(n2)


print(fibonacci(15))
