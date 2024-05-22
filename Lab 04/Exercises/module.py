import datetime
import random


def greetings(name):
    print("Hello", name)
    a = datetime.datetime.now()
    a = a.strftime('%A')
    print("Today is:", a)
    b = ""
    for i in range(1, 5):
        b = b + str(random.randrange(40, 71)) + " "
    print("Your lucky numbers for today are:", b)

