from datetime import datetime

date_string = "2021-11-02"
date_object = datetime.strptime(date_string, "%Y-%m-%d")
formatted = date_object.strftime("%d-%m-%Y")

print(formatted)
