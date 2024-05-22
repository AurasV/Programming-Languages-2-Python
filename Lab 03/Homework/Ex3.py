def listings(a):
    listEven = []
    listOdd = []
    for i in a:
        if i % 2 == 0:
            listEven.append(i)
        else:
            listOdd.append(i)
    return listEven, listOdd


a = [1, 2, 3, 4, 5, 6]
print(listings(a))

