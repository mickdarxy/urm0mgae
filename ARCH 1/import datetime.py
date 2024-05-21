import datetime
import calendar
import holidays

input_holiday = input("date: ")

day = int(input("Day: "))
month = int(input("Month: "))

if day == 1 and month == 1:
    print("New Years Day")
elif day == 29 and month == 3:
    print("Good Friday")
elif day ==