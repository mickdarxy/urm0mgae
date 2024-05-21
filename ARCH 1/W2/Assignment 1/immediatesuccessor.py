#input from the user 
input_date = input()

#invalidity
def_incorrect_input = ["_", "/", ".", ",", "|"]

#the if statements
if any(x in input_date for x in def_incorrect_input):
    print("Error: Correct Format: YYYY-MM-DD")
else: 

    if len(input_date.split("-")) == 3:
        separated_input_date = input_date.split("-")

        date_year = int(separated_input_date[0])
        date_month = int(separated_input_date[1])
        date_day = int(separated_input_date[2])

        if len(str(date_year)) == 4:
            if 0 < int(date_month) <= 12:
                if date_month == 2:
                    date_valid = False 

                    if int(date_day) > 28:
                        date_valid == False

                    elif int(date_day) == 28:
                        date_month = 3
                        date_day = 1
                        date_valid = True
                    else:
                        date_day += 1 
                        date_valid = True

                    if date_valid:
                        if len(str(date_month)) == 1:
                            date_month = f"0{date_month}"

                        if len(str(date_day)) == 1:
                            date_day = f"0{date_day}"
                            
                        print(f"Next date: {date_year}-{date_month}-{date_day}")
                    else:
                        print("Input format ERROR. Correct Format: YYYY-MM-DD")    
                
                elif  int(date_month) == 12:
                    date_valid = False 

                    if int(date_day) == 31:
                        date_year += 1
                        date_month = 1
                        date_day = 1
                        date_valid = True
                    else:
                        date_day += 1 
                        date_valid = True

                    if date_valid:
                        if len(str(date_month)) == 1:
                            date_month = f"0{date_month}"

                        if len(str(date_day)) == 1:
                            date_day = f"0{date_day}"

                        print (f"Next Date: {date_year}-{date_month}-{date_day}")
                    else:
                        print("Input format ERROR. Correct Format: YYYY-MM-DD")
                else:
                    date_valid = False

                    if int(date_month) % 2:
                        if int(date_day) > 30:
                            date_valid = False
                        elif int(date_day) == 30:
                            date_month += 1 
                            date_day = 1
                            date_valid = True
                        else:
                            date_day += 1
                            date_valid = True
                    else:
                        if int(date_day) > 31:
                            date_valid = False
                        elif int(date_day) == 31:
                            date_month += 1
                            date_day = 1
                            date_valid = True
                        else:
                            date_day += 1
                            date_valid = True
                    if date_valid:
                        if len(str(date_month)) == 1:
                            date_month = f"0{date_month}"

                        if len(str(date_day)) == 1:
                            date_day = f"0{date_day}"

                        print(f"Next Date: {date_year}-{date_month}-{date_day}")
                    else:
                        print("Input format ERROR. Correct Format: YYYY-MM-DD")
            else:
                print("Input format ERROR. Correct Format: YYYY-MM-DD")
        else:
            print("Input format ERROR. Correct Format: YYYY-MM-DD")
    else:
        print("Input format ERROR. Correct Format: YYYY-MM-DD")

                    


                    

