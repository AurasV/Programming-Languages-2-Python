import re


def uppercase_lowercase(string):
    regex = r'^[A-Z]+_[a-z]+$'
    return bool(re.match(regex, string))


print(uppercase_lowercase("MARO_maro"))
print(uppercase_lowercase("MARO maro"))
