for num in range(20, 61):
    if all(num % i != 0 for i in range(2, num)):
        print(num)
