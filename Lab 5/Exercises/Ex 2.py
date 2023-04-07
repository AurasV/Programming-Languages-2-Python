import re

words = "car, cat, dog, pool, bath, cone, cube, ring, int"
pattern = re.compile(r"\b\w{4}\b")
matches = pattern.findall(words)

print(matches)
