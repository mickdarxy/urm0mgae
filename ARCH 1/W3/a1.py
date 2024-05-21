

def get_valid_input(prompt):
    while True:
        name = input(prompt)
        if name.isalpha and 2 <= len(name) <= 10:
            return name
        else:
            print("Input error. Please enter valid name (2-10 characters, aplhabets only).")

def get_valid_job_title():
    while True:
        job_title = input("Enter job title (minimum 10 characters without numbers): ")
        if job_title.isalpha() and len(job_title) >= 10:
            return job_title
        else:
            print("Input error. Job title must be at least 10 characters long without numbers.")

def get_valid_salary():
    while True:
        try:
            salary = float(input("Enter annual salary (20,000.00 - 80,000.00): "))
            if 20000 <= salary <= 80000:
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
    result += f"Dear {frst_name} {last_name}"
    result += f"After careful evaluation of your application for the position of {job_title},"
    result += f"we are glad to offer you the job. Your salary will be {annu_slry} euro annually."
    result += f"Your start date will be on {strt_date}. Please do not hesitate to contact us with any questions."
    result += "Sincerely,"
    result += "HR Department of XYZ"
    return result

def generate_rejection(frst_name, last_name, job_title, feedback):
    result = []
    result += f"Dear {frst_name} {last_name}"
    result += f"After careful evaluation of your application for the position of {job_title},"
    result += "at this moment we have decided to proceed with another candidate."
    #Check to see if there is any feedback, if so add that part, else don't add anything
    if feedback != "":
        result += "Here we would like to provide you our feedback about the interview."
        result += f"{feedback}"

    result += "Sincerely,"
    result += "HR Department of XYZ"
    return result



def main():
    while True:
        more_letters = input("More Letters? (Yes or No) ").lower()
        if more_letters != "yes":
            break

        offer_or_rejection = input("Job Offer or Rejection? ").lower()

        if offer_or_rejection == "job offer":
            first_name, last_name, job_title, annual_salary, start_date = generate_joboffer()
            email_content = generate_joboffer(first_name, last_name, job_title, annual_salary, start_date)
            print("\nJob Offer Email Content:\n")
            print(email_content)
        elif offer_or_rejection == "rejection":
            first_name, last_name, job_title, annual_salary, start_date = generate_rejection()
            email_content = generate_rejection(first_name, last_name, job_title, annual_salary, start_date)
            print("\nJob Offer Email Content:\n")
            print(email_content)
        else:
            print("Invalid input. Please choose 'Job Offer' or 'Rejection'.")



