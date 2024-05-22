import re


def match_q(word):
    pattern = r'\Bq\B'
    match = re.search(pattern, word)
    return bool(match)


print(match_q('quit'))
print(match_q('inquiry'))
print(match_q('aq'))
print(match_q('liquid'))
