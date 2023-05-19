def powerplay(a, b):
    return a ** b


if __name__ == '__main__':
    list1 = [5, 2, 3]
    list2 = [1, 2, 3]
    result = map(powerplay, list1, list2)
    print(list(result))
    