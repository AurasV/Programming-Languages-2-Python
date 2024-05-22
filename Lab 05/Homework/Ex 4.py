import re

string = "Hello World! Goodbye World!"
regex = r'(\w+) (\w+)'
matches = re.findall(regex, string)
print("All matches:", matches)
for match in matches:
    print("Match in group 1:", match[0])
    print("Match in group 2:", match[1])
