import re

a = "rectangle"
b = "square"
c = "sphere"
d = "triangle"
e = "cone"
f = "cube"
g = "cylinder"

pattern = re.compile("^[cs].+e$")

for var in [a, b, c, d, e, f, g]:
    if pattern.match(var):
        print(var)
