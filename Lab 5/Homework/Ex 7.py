import re


def match_hi(text):
    pattern = r'^hiii?$'
    match = re.match(pattern, text)
    return bool(match)


print(match_hi('hi'))
print(match_hi('hii'))
print(match_hi('hiii'))
print(match_hi('hihi'))
print(match_hi('hiiii'))
