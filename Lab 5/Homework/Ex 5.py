from datetime import datetime


def convert_date(date_string):
    dt = datetime.strptime(date_string, '%y-%m-%d')
    month_name = dt.strftime('%B')
    new_date_string = dt.strftime('%d-%B-%y')
    return new_date_string


date_str = '21-12-01'
new_date_str = convert_date(date_str)
print(new_date_str)
