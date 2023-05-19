def multiply4(a):
    return a * 4


if __name__ == '__main__':
    numbers = [1, 2, 3]
    result = map(multiply4,numbers)
    print(list(result))
