import re

my_list = ["square", "triangle", "cube", "sphere", "circle", "pentagon",
           "hexagon", "rectangle", "parallelogram", "trapezoid"]
geo = "A square has 4 sides, a triangle has 3, a pentagon has " \
      "5, a hexagon has 6. While a square has 4 equal sides, a triangle can have 0, 2 or 3 equal sides."

pattern = "|".join(my_list)
matches = re.findall(pattern, geo)
digits = " ".join(re.findall("\d", geo))
non_digits = "".join(re.findall("\D", geo))

print(matches)
print(digits)
print(non_digits)
