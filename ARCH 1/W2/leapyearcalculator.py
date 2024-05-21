#leapyearcalculator

#input
input_year = int(input("Year: "))

#check if the year is a leapyear step 1 
if input_year / 400:
    #also
    if input_year / 100:
        print("not a leap year")
    else: 
        #if it also is a leapyear
        if input_year / 4:
            print("not a leapyear")
        else:
            #print leapyear
            print("is a leapyear")
else: 
    #print leapyear
    print("is a leapyear")
    
    