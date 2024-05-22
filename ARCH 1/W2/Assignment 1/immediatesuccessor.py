#input from the user 
get_date = input()

#invalidity
incorrect = ["_", "/", ".", ",", "|"]

#the if statements
if any(x in get_date for x in incorrect):
    print("Error: Correct Format: YYYY-MM-DD")
else: 

    if len(get_date.split("-")) == 3:
        separated_date = get_date.split("-")
        year = int(separated_date[0])
        month = int(separated_date[1])
        day = int(separated_date[2])

        if len(str(year)) == 4:
            if 0 < int(month) <= 12:
                if month == 2:
                    date_valid = False 

                    if int(day) > 28:
                        date_valid = False
                    elif int(day) == 28:
                        month = 3
                        day = 1
                        date_valid = True
                    else:
                        day += 1
                        date_valid = True

                    if date_valid:
                        if len(str(month)) == 1:
                            month = f"0{month}"
                        if len(str(day)) == 1:
                            date_day = f"0{day}"
                        print(f"Next date: {year}-{month}-{day}")
                    else:
                        print("Input format ERROR. Correct Format: YYYY-MM-DD")    
                
                elif int(month) == 12:
                    date_valid = False
                    if int(day) == 31:
                        year += 1
                        month = 1
                        day = 1
                        date_valid = True
                    else:
                        day += 1
                        date_valid = True

                    if date_valid:
                        if len(str(month)) == 1:
                            date_month = f"0{month}"
                        if len(str(day)) == 1:
                            date_day = f"0{day}"
                        print(f"Next Date: {year}-{month}-{day}")
                    else:
                        print("Input format ERROR. Correct Format: YYYY-MM-DD")
                else:
                    date_valid = False
                    if int(month) % 2:
                        if int(day) > 30:
                            date_valid = False
                        elif int(day) == 30:
                            month += 1
                            day = 1
                            date_valid = True
                        else:
                            day += 1
                            date_valid = True
                    else:
                        if int(day) > 31:
                            date_valid = False
                        elif int(day) == 31:
                            month += 1
                            date_day = 1
                            date_valid = True
                        else:
                            day += 1
                            date_valid = True
                    if date_valid:
                        if len(str(month)) == 1:
                            date_month = f"0{month}"
                        if len(str(day)) == 1:
                            date_day = f"0{day}"
                        print(f"Next Date: {year}-{month}-{day}")
                    else:
                        print("Input format ERROR. Correct Format: YYYY-MM-DD")
            else:
                print("Input format ERROR. Correct Format: YYYY-MM-DD")
        else:
            print("Input format ERROR. Correct Format: YYYY-MM-DD")
    else:
        print("Input format ERROR. Correct Format: YYYY-MM-DD")
