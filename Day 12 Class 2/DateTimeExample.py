#Example 1: Get current Date and Time
import datetime

d = datetime.datetime.now()
print(d)

d2 = datetime.date.today()
print(d2)

print(dir(datetime))

#Example 3: Date object to represent a date.

d3 = datetime.date(2019,4,13)
print(d3)
# Also in another way:
from datetime import date
a = date(2019,4,13)
print(a)

#Example 4: Get current date
from datetime import date
today = date.today()
print("Current date =", today)

#Example 5: Get date from a timestamp