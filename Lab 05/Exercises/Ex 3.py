import re

my_list = ["square", "triangle", "cube", "sphere", "circle", "pentagon", "hexagon", "rectangle",
           "parallelogram", "trapezoid"]
pattern = re.compile(r"re$")

for word in my_list:
    if pattern.search(word):
        print(word)
