import re

link = "https://www.newyorker.com/magazine/2021/11/" \
       "01/the-book-of-form-and-emptiness-the-war-for-gloria" \
       "-read-until-you-understand-and-the-end-of-bias"

pattern = re.compile(r"/(\d{4})/(\d{2})/(\d{2})/")
match = pattern.search(link)
year = match.group(1)
month = match.group(2)
date = match.group(3)

print("Year:", year)
print("Month:", month)
print("Date:", date)
