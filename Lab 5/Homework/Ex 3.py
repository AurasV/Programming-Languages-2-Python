import re

hw4 = "rectangle square sphere triangle cone cube cylinder"


def print_re_le_words(text):
    pattern = r'\b\w+(?:le|re)\b'
    matches = re.findall(pattern, text)
    for match in matches:
        print(match)


print_re_le_words(hw4)
