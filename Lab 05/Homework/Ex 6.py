import re


def m_n_three_chars(string):
    regex = r'^m\w{3}n$'
    return bool(re.match(regex, string))


print(m_n_three_chars("maaan"))
print(m_n_three_chars("maan"))
