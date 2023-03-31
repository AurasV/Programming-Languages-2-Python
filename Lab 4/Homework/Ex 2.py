import datetime

date_str = "31 March 2023"
date = datetime.datetime.strptime(date_str, "%d %B %Y")
week_number = date.isocalendar()[1]

print(str(date_str) + " is in the " + str(week_number) + "th week of the year")