

def get_valid_input(prompt):
    valid = False
    while not valid:
        name = input(prompt)
        if name.isalpha and 2 <= len(name) <= 10 and name[0] == name[0].upper():
            return name
        else:
            print("Input error. Please enter valid name (2-10 characters, aplhabets only).")


def get_valid_job_title():
    valid = False
    while not valid:
        job_title = input("Enter job title (minimum 10 characters without numbers): ")
        temp_job_title = job_title.replace(" ", "")
        temp_job_title = temp_job_title.replace("-", "")

        if temp_job_title.isalpha() and len(temp_job_title) >= 10:
            return job_title
        else:
            print("Input error. Job title must be at least 10 characters long without numbers.")
            

def get_valid_salary():
    valid = False
    while not valid:
        try:
            salary = input("Enter annual salary (20.000,00 - 80.000,00): ")

            temp_salary = salary.replace(".", "")
            temp_salary = temp_salary.replace(",", ".")

            if 20000 <= float(temp_salary) <= 80000:
                valid = True
                return salary
            else:
                print("Input error. Salary must be between 20,000.00 and 80,000.00.")
        except ValueError:
            print("Input error. Please enter a valid floating-point number.")
            

def get_valid_date():
    while True:
        date_str = input("Enter starting date (YYYY-MM-DD): ")
        try:
            year, month, day = map(int, date_str.split("-"))
            if 2021 <= year <= 2022 and 1 <= month <= 12 and 1 <= day <= 31:
                return date_str
            else:
                print("Input error. Date must be in YYYY-MM-DD format, within 2021-2022.")
        except ValueError:
            print("Input error. Please enter a valid date (YYYY-MM-DD).")
            

def get_feedback():
    feedback = input("Include feedback? (yes/no): ").lower()
    if feedback == "yes":
        return input("Enter feedback statement: ")
    return ""


def generate_joboffer(frst_name, last_name, job_title, annu_slry, strt_date):
    result = []
    result += [f"Dear {frst_name} {last_name}"]
    result += [f"After careful evaluation of your application for the position of {job_title},"]
    result += [f"we are glad to offer you the job. Your salary will be {annu_slry} euro annually."]
    result += [f"Your start date will be on {strt_date}. Please do not hesitate to contact us with any questions."]
    result += ["Sincerely,"]
    result += ["HR Department of XYZ"]
    return result


def generate_rejection(frst_name, last_name, job_title, feedback):
    result = []
    result += [f"Dear {frst_name} {last_name}"]
    result += [f"After careful evaluation of your application for the position of {job_title},"]
    result += ["at this moment we have decided to proceed with another candidate."]
    # Check to see if there is any feedback, if so add that part, else don't add anything
    if feedback != "":
        result += ["Here we would like to provide you our feedback about the interview."]
        result += [f"{feedback}"]

    result += ["Sincerely,"]
    result += ["HR Department of XYZ"]
    return result


def main():
    running = True
    while running:
        more_letters = input("More Letters? (Yes or No) ").lower()
        if more_letters == "yes":
            offer_or_rejection = input("Job Offer or Rejection? ").lower()

            if offer_or_rejection == "job offer":
                first_name = get_valid_input("First Name?")
                last_name = get_valid_input("Last Name?")
                job_title = get_valid_job_title()
                annual_salary = get_valid_salary()
                start_date = get_valid_date()
                
                email_content = generate_joboffer(first_name, last_name, job_title, annual_salary, start_date)
                print("\nJob Offer Email Content:\n")

                for i in email_content:
                    print(i)
            elif offer_or_rejection == "rejection":
                first_name = get_valid_input("First Name?")
                last_name = get_valid_input("Last Name?")
                job_title = get_valid_job_title()
                feedback = get_feedback()

                email_content = generate_rejection(first_name, last_name, job_title, feedback)
                print("\nJob Offer Email Content:\n")

                for i in email_content:
                    print(i)
            else:
                print("Invalid input. Please choose 'Job Offer' or 'Rejection'.")
        elif more_letters == "no":
            running = False
        else:
            print("Invalid input. Please choose valid awnser")


main()
