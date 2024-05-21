import os
import sys

#creating two lists that each store whether the input is valid or corrupt
valid_lines = []
corrupt_lines = []

#create a function to organize and check all the data given by input
def validate_data(line):
    student_number_valid = True
    index = 0 #empty index to store
    studentnumber, firstname, lastname, birthdate, studyprogram = line.split(',')
    for element in line.split(','):
        if index == 0:
            student_number = element
    if len(student_number) > 0:
        csv_studnum = student_number[0]
        csv_studnum2 = student_number[1]
        if csv_studnum == '0' and csv_studnum2 == '8' or '9':
            valid_lines.append(studentnumber)
        else:
            corrupt_lines.append(studentnumber)
    else:
        corrupt_lines.append(studentnumber)

    if len(firstname) > 0:
        if firstname.isalpha() == True:
            valid_lines.append(firstname)
        else:
            corrupt_lines.append(firstname)
    else:
        corrupt_lines.append(firstname)

    if len(birthdate.split()) == 3:
        year1, month1, day1 = birthdate.split("-")
        year1 = int(year1)
        valid_months = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
        valid_days = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10","11", "12", "13",
        "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31"]
        thirty_days = ["04", "06", "09", "11"]
        if not year1 in range(1960, 2004 + 1):
            birthdate = (f"{year1}-{month1}-{day1}")
            corrupt_lines.append(birthdate)
        if not month1 in valid_months:
            birthdate = (f"{year1}-{month1}-{day1}")
            corrupt_lines.append(birthdate)
        if month1 == "02":
            valid_days.remove("31")
            valid_days.remove("30")
            valid_days.remove("29")
            if not day1 in valid_days:
                birthdate = (f"{year1}-{month1}-{day1}")
                corrupt_lines.append(birthdate)
        if month1 in thirty_days:
            valid_days.remove("31")
            if not day1 in valid_days:
                birthdate = (f"{year1}-{month1}-{day1}")
                corrupt_lines.append(birthdate)
        else:
            birthdate = (f"{year1}-{month1}-{day1}")

        if len(studyprogram) > 1:
            if studyprogram == "INF" or "TINF" or "CMD" or "AI":
                valid_lines.append(studyprogram)
            else:
                corrupt_lines.append(studyprogram)
        else:
            corrupt_lines.append(studyprogram)

def main(csv_file):
    with open(os.path.join(sys.path[0], csv_file), newline ='') as csv_file:
        # skip header line
        next(csv_file)

        for line in csv_file:
            validate_data(line.strip())

    print('### VALID LINES ###')
    print("\n".join(valid_lines))
    print('### CORRUPT LINES ###')
    print("\n".join(corrupt_lines))


if __name__ == "__main__":
    main('studentscsvcsv.csv')