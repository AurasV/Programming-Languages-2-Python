import re


def check(x):
    pattern = re.compile(r"\d")
    if pattern.search(x):
        print("Contains Number")
    else:
        print("Doesn't Contain Number")


a = "1abc"
b = "abcd"

check(a)
check(b)
