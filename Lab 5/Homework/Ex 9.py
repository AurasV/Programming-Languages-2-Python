import re


def replace_ai(text):
    text = re.sub(r'a', 'u', text)
    text = re.sub(r'i', 'e', text)
    return text


print(replace_ai('aeiou'))
