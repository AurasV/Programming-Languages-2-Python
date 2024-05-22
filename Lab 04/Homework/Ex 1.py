import os

os.mkdir("New Folder")
with open("New Folder/Text File.txt", "w") as f:
    f.write("Line 1\n")
    f.write("Line 2\n")
    f.write("Line 3\n")

with open("New Folder/Text File.txt", "r") as f:
    lines = f.readlines()

for line in (lines[:2]):
    print(line)
