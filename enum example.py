#enum example

from enum import Enum

class DayOfWeek(Enum):
    MONDAY = "Monday"
    TUESDAY = "Tuesday"
    WEDNESDAY = "Wednesday"
    THURSDAY = "Thursday"
    FRIDAY = "Friday"
    SATURDAY = "Saturday"
    SUNDAY = "Sunday"

day = DayOfWeek.MONDAY
print(day)  # prints "DayOfWeek.MONDAY"
print(day.name)  # prints "MONDAY"
print(day.value)  # prints "Monday"

ip = DayOfWeek(input('Enter day of week'))
if ip in DayOfWeek:
        print("valid")
else:
        print ('invalid')