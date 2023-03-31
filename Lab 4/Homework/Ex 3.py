import datetime

date1_str = "20 March 2023"
date2_str = "31 March 2023"
date1 = datetime.datetime.strptime(date1_str, "%d %B %Y").date()
date2 = datetime.datetime.strptime(date2_str, "%d %B %Y").date()

diff = date2 - date1
print(f"There are {diff.days} days between {date1_str} and {date2_str}")
