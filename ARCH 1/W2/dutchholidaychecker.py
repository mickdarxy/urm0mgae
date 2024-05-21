#this program is based upon the 2024 calendar 


#assigning an integer and input to create holidays for the day and month
day = int(input("Day: "))
month = int(input("Month:"))
input
#create an if statement 
if day == 1 and month == 1:
    print("New Years Day")
elif day == 29 and month == 3:
    print("Good Friday")
elif day == 31 and month == 3 or day == 1 and month == 4:
    print ("Easter")
elif day == 27 and month == 4:
    print("King's Day")
elif day == 5 and month == 5: 
    print("Liberation Day")
elif  day == 9 and month == 5:
    print("Ascension Day")
elif day == 19 and month == 5 or day == 20 and month == 5:
    print("Pentecost")
elif day == 25 and month == 12:
    print("Christmas Day")
elif day == 26 and month == 12:
    print("Boxing Day")
else:
    print("No Holiday Found On Given Input")