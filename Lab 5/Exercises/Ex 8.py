import re


def check(x):
    pattern = re.compile(r"\d\b")
    if pattern.search(x):
        print("Ends With Number")
    else:
        print("Doesn't End With Number")


a = "1abc"
b = "abc1"

check(a)
check(b)
