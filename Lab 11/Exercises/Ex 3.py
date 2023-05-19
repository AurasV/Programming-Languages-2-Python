def deconcatenate(a):
    new_string = []
    for i in range(0, len(a)):
        new_string.append(a[i])
    return new_string


if __name__ == '__main__':
    old_string = ["red", "blue"]
    result = map(deconcatenate, old_string)
    print(list(result))
    