import re


def check(x):
    pattern = re.compile(r"\b\d")
    if pattern.search(x):
        print("Starts With Number")
    else:
        print("Doesn't Start With Number")


a = "1abc"
b = "abc1"

check(a)
check(b)
