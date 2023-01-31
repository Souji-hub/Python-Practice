#wap to find the day using enum and switch case

from enum import Enum

class DayOfWeek(Enum):
    MONDAY = "Monday"
    TUESDAY = "Tuesday"
    WEDNESDAY = "Wednesday"
    THURSDAY = "Thursday"
    FRIDAY = "Friday"
    SATURDAY = "Saturday"
    SUNDAY = "Sunday"


dayip = DayOfWeek(input("Enter a day of the week: "))
print(dayip)
print(dayip.name) 
print(dayip.value)


if dayip == DayOfWeek.MONDAY:
    print("It's Monday, the week is just starting.")
elif dayip ==DayOfWeek.TUESDAY :
    print("It's Tuesday, halfway through the week.")
elif dayip == DayOfWeek.WEDNESDAY:
    print("It's Wednesday, the week is halfway done.")
elif dayip == DayOfWeek.THURSDAY:
    print("It's Thursday, only a few more days to go.")
elif dayip == DayOfWeek.FRIDAY:
    print("It's Friday, the week is almost over!")
elif dayip == DayOfWeek.SATURDAY:  
    print("It's Saturday, Saturday is holiday!")
elif dayip == DayOfWeek.SUNDAY:
    print("It's the weekend, time to relax!")
else:
    print("Invalid day of the week.")






## Alternative-----------
# def get_message(day):
#     messages = {
#         DayOfWeek.MONDAY: "It's Monday, the week is just starting.",
#         DayOfWeek.TUESDAY: "It's Tuesday, halfway through the week.",
#         DayOfWeek.WEDNESDAY: "It's Wednesday, the week is halfway done.",
#         DayOfWeek.THURSDAY: "It's Thursday, only a few more days to go.",
#         DayOfWeek.FRIDAY: "It's Friday, the week is almost over!",
#         DayOfWeek.SATURDAY: "It's Saturday, Saturday is holiday!",
#         DayOfWeek.SUNDAY: "It's the weekend, time to relax!"
#     }
#     return messages.get(day,'invalid dayip of the week')

#day = DayOfWeek(input("Enter a day of the week: "))
# print(get_message(day))
