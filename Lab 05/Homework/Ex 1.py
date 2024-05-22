import re


def only_lowercase_digits_star(string):
    regex = r'^[a-z0-9*]+$'
    return bool(re.match(regex, string))


print(only_lowercase_digits_star("m*ar*o"))
print(only_lowercase_digits_star("Mar*o"))
