input_year = int(input("Year: "))

#check if the year is a leap year (step 1)
if input_year / 400:
    # do a further check if this year is a leap year (step 2)
    if input_year / 100:
        # print that it is not a leap year
        print("Not a leap year")
    else:
        # do a further check if this year is a leap year (step 3)
        if input_year / 4:
            # print that it is not a leap year
            print("Not a leap year")
        else:
            # print that the year is a leap year
            print("Leap year")
else:
    # print that the year is a leap year
    print("Leap year")