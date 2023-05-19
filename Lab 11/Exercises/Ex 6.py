import re

the_string = "My friend is 30 years old, being born 20-01-1993   ---90 /89"

if __name__ == '__main__':
    a = re.findall(r'-?\d+', the_string)
    a = list(map(int, a))
    print([i for i in filter(lambda x: x > 0, a)])
