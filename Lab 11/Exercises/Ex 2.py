if __name__ == '__main__':
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    list3 = [7, 8, 9]
    x = lambda a, b, c: a + b + c
    print(list(map(x, list1, list2, list3)))
