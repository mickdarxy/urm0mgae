# Import the required modules
import csv


def validate_data(value):
    state = True

    if value == "" or value is None:
        state = False

    return state


def studentnumber_check(studentnumber):
    state = False

    if studentnumber.isnumeric():
        if len(studentnumber) == 7:
            if studentnumber[0] == "0":
                if studentnumber[1] == "8" or studentnumber[1] == "9":
                    state = True

    return state


def name_check(name):
    state = False

    if name.isalpha():
        state = True

    return state


def dateofbirth_check(dateofbirth):
    state = False

    valid_format = True
    valid_year = False
    valid_month = False
    valid_day = False

    string_year = dateofbirth[0:4]
    string_month = dateofbirth[5:7]
    string_day = dateofbirth[8:10]

    for e in string_year:
        if valid_format:
            if e == "-":
                valid_format = False

    int_year = int(string_year)
    int_month = int(string_month)
    int_day = int(string_day)

    if 1960 <= int_year <= 2004:
        valid_year = True

    if 1 <= int_month <= 12:
        valid_month = True

    if 1 <= int_day <= 31:
        valid_day = True

    if valid_year and valid_month and valid_day:
        state = True

    return state


def studyprogram_check(studyprogram):
    state = False

    if studyprogram == "INF" or studyprogram == "TINF" or studyprogram == "CMD" or studyprogram == "AI":
        state = True

    return state


# Open the extenal CSV file
file_studentcsv = open('students.csv')

# Read the CSV file with the CSV Reader
csvreader_studentcsv = csv.reader(file_studentcsv)

# Create a list variable that will hold all the csv rows
list_studentcsv = []

# preform a for-loop over the csvreader and store the csv rows in the list_studentcsv variable
for row in csvreader_studentcsv:
    list_studentcsv.append(row)

# After retrieving the required data, we close the CSV file
file_studentcsv.close()

# Now that we have the data, we are going to preform some checks to see which rows are correct and which weren't
# To show which lines were correct and which weren't, we are going to need 2 new list variables
list_correct = []
list_incorrect = []

# Loop through the list_studentcsv and preform the checks to see if the lines are valid or invalid
for student in list_studentcsv:
    try:
        student_studentnumber = student[0]
        student_firstname = student[1]
        student_lastname = student[2]
        student_birthday = student[3]
        student_studyprogram = student[4]

        nocorr_studentnumber = validate_data(student_studentnumber)
        nocorr_firstname = validate_data(student_firstname)
        nocorr_lastname = validate_data(student_lastname)
        nocorr_birthday = validate_data(student_birthday)
        nocorr_studyprogram = validate_data(student_studyprogram)

        if nocorr_studentnumber and nocorr_firstname and nocorr_lastname and nocorr_birthday and nocorr_studyprogram:
            valid_studentnumber = studentnumber_check(student_studentnumber)
            valid_firstname = name_check(student_firstname)
            valid_lastname = name_check(student_lastname)
            valid_birthday = dateofbirth_check(student_birthday)
            valid_studyprogram = studyprogram_check(student_studyprogram)

            if valid_studentnumber and valid_firstname and valid_lastname and valid_birthday and valid_studyprogram:
                list_correct.append(student)
            else:
                invalid_parts = []
                if not valid_studentnumber:
                    invalid_parts.append(student_studentnumber)
                if not valid_firstname:
                    invalid_parts.append(student_firstname)
                if not valid_lastname:
                    invalid_parts.append(student_lastname)
                if not valid_birthday:
                    invalid_parts.append(student_birthday)
                if not valid_studyprogram:
                    invalid_parts.append(student_studyprogram)

                student.append(invalid_parts)

                list_incorrect.append(student)
        else:
            list_incorrect.append(student)
    except NameError:
        list_incorrect.append(student)

# After preforming the loop, print the final results
print("### VALID LINES ###")
for i in list_correct:
    print(f"{i[0]},{i[1]},{i[2]},{i[3]},{i[4]}")
print("### CORRUPT LINES ###")
for i in list_incorrect:
    print(f"{i[0]},{i[1]},{i[2]},{i[3]},{i[4]} => INVALID DATA: {i[5]}")