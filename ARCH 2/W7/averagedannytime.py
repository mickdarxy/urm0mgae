# ----------------------------------------------------------------------------------------------------------
# These functions are the required functions for this problem

# This function will load the text file and turn the text file into a usable list
def load_txt_file():
    # Open the file in READ mode
    file = open("../../../OneDrive/Desktop/NLAMSTDM.txt", "r")
    # Retrieve the content from the file
    file_content = file.readlines()
    # Close the file as it won't be needed for processing anymore
    file.close()

    # Create an empty list in which we will store the cleaned file content
    cleaned_file_content = []
    # For-loop through the file's content
    for line in file_content:
        # Strip the line from spaces in the front and back
        line = line.strip()
        # Split the line based on spaces and store this in a temporary list
        temp_list_line = line.split(" ")
        # Create an empty list in which we will store the valid data
        list_line = []

        # Loop through the temporary list and only add the valid data into the empty list we created above
        for item in temp_list_line:
            # Check if the item in the list is not an empty string
            if item != '':
                # Append the valid item to the empty list
                list_line.append(item)

        # Add the cleaned line to the cleaned file content list
        cleaned_file_content.append(list_line)

    # Loop through our cleaned file content and turn it into dict in which we are going to
    # store the data based on the following format: {year: {month: [temp, temp, temp, ...]}, ...}
    dict_file_data = dict()
    for line in cleaned_file_content:
        # Retrieve the month, day, year and average temperature from the line
        line_data_month = int(line[0])
        line_data_year = int(line[2])
        line_data_temp = float(line[3])

        # Check if the year is already in the main dictionary in which we store our data.
        # If it does not exist, create it and put an empty dictionary in it
        if line_data_year not in dict_file_data:
            dict_file_data[line_data_year] = dict()

        # Check if the month is already in the year dictionary in which we store our data
        # If it does not exist, create it and put an empty list in it
        if line_data_month not in dict_file_data[line_data_year]:
            dict_file_data[line_data_year][line_data_month] = list()

        # Add the temperature for that line into the list based on its year and month
        dict_file_data[line_data_year][line_data_month].append(line_data_temp)

    # Return the data in the required format
    return dict_file_data


# This function will turn a Fahrenheit temperature (float) into a valid Celsius temperature (float)
def fahrenheit_to_celsius(fahrenheit: float):
    # In this return, we preform a calculation for turning a Fahrenheit temperature into a Celsius temperature
    return (fahrenheit - 32) / 1.8


# This function will return a list of tuples containing the average temperature per month based on the inputted dict
def average_temp_per_month(temperatures_per_year: dict):
    # Create an empty list in which we will store our return data
    return_data = list()

    # Loop through the months in the dict given
    for month in temperatures_per_year:
        # Retrieve the list with temps for that month
        months_temp_data = temperatures_per_year[month]

        # # Create two variables in which we are going to store a
        # # sum of the temperature per day in a month and the days in that month
        sum_days_temp = 0.0
        days = 0

        # Loop through the temps in the month's temperature data list
        for temp in months_temp_data:
            # Add the temp to the sum
            sum_days_temp += temp
            # Add a day to the days for this month
            days += 1

        # After doing this, we can preform a calculation to see what the average temp was for that month and
        # add that data to our return data list
        return_data.append((month, sum_days_temp / days))

    # Return the data
    return return_data


# This function will return a list of tuples containing the average temperature per year based on the inputted dict
def average_temp_per_year(temperatures: dict):
    # Create an empty list in which we will store our return data
    return_data = list()

    # Loop through the years to see which years are available
    for year in temperatures:
        # Retrieve the year's data from the dict
        year_data = temperatures[year]

        # Create two variables in which we are going to store a
        # sum of the temperature per day in a month and the days in that month
        sum_month_temp = 0.0
        months = 0

        # Loop through the year's data to see the available months
        for month in year_data:
            # Retrieve the list with temps for that month
            months_temp_data = year_data[month]

            # Create two variables in which we are going to store a
            # sum of the temperature per day in a month and the days in that month
            sum_days_temp = 0.0
            days = 0
            # Loop through the temp data for the month
            for temp in months_temp_data:
                # Add the temp to the sum
                sum_days_temp += temp
                # Add a day to the days for this month
                days += 1

            # After doing this, we can preform a calculation to see what the average temp was for that month
            month_average_temp = sum_days_temp / days

            # Add the average temp for that month to the sum average temp for the corresponding year
            sum_month_temp += month_average_temp
            # Add a month to the months for this month
            months += 1

        # After doing the calculations per month, divide the sum of the average temperature per month
        # and add a tuple to the return list
        return_data.append((year, sum_month_temp / months))

    # Return the data
    return return_data


# ----------------------------------------------------------------------------------------------------------
# These functions are for the choices on the program menu
def print_menu():
    print("[1] Print the average temperatures per year (fahrenheit)")
    print("[2] Print the average temperatures per year (celsius) Hint: Use built-in map() function.")
    print("[3] Print the warmest and coldest year as tuple based on the average temperature")
    print("[4] Print the warmest month of a year based on the input year of the user (full month name)")
    print("[5] Print the coldest month of a year based on the input year of the user (full month name)")
    print("[6] Print a list of tuples where the first element of each tuple is the year and")
    print("    the second element of the tuple is a dictionary with months as the keys and")
    print("    the average temperature (in Celsius) of each month as the value")


def option1():
    # get the data from the file
    file_data = load_txt_file()
    # get the average temp data based on the data from the file
    average_temp_data = average_temp_per_year(file_data)

    # Loop through the rows
    for row in average_temp_data:
        # Retrieve the year and average temp from the tuple row
        data_year = row[0]
        data_temp = row[1]
        # Print the results
        print(f"{data_year}: {data_temp}")


def option2():
    # get the data from the file
    file_data = load_txt_file()
    # get the average temp data based on the data from the file
    average_temp_data = average_temp_per_year(file_data)

    # Loop through the rows
    for row in average_temp_data:
        # Retrieve the year and average temp from the tuple row
        data_year = row[0]
        data_temp = float(row[1])
        # Convert the temp into Celsius
        data_temp_celsius = fahrenheit_to_celsius(data_temp)
        # Print the results
        print(f"{data_year}: {data_temp_celsius}")


def option3():
    # get the data from the file
    file_data = load_txt_file()
    # get the average temp data based on the data from the file
    average_temp_data = average_temp_per_year(file_data)

    # Create four variables that will be used to see which year was the warmest and the coldest
    warm_year = 0
    warm_temp = 0.0
    cold_year = 0
    cold_temp = 300.0

    # Loop through the rows
    for row in average_temp_data:
        # Retrieve the year and average temp from the tuple row
        data_year = row[0]
        data_temp = float(row[1])

        # Check if the temp is higher than the current warmest year
        if data_temp > warm_temp:
            warm_year = data_year
            warm_temp = data_temp

        # Check if the temp is lower than the current coldest year
        if data_temp < cold_temp:
            cold_year = data_year
            cold_temp = data_temp

    print((warm_year, warm_temp))
    print((cold_year, cold_temp))


def option4():
    print("Available years:")
    print("-------------------")
    file_data = load_txt_file()
    # Loop through the years to see which years are available
    for year in file_data:
        print(year)
    print("-------------------")
    # Request an input from the user to select a year
    input_year = int(input("Select a year: "))

    # Create a dict in which we store the month's number to name conversion
    month_dict = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June", 7: "July", 8: "August",
                  9: "September", 10: "October", 11: "November", 12: "December"}

    # Create two variables in which we are going to store the
    # warmest month and associated average temperature for that month
    warmest_month = 0
    warmest_temp = 0

    # Loop through the years to see which years are available
    for year in file_data:
        # Retrieve the year's data from the dict
        year_data = file_data[year]

        # Loop through the year's data to see the available months
        for month in year_data:
            # Retrieve the list with temps for that month
            months_temp_data = year_data[month]

            # Create two variables in which we are going to store a
            # sum of the temperature per day in a month and the days in that month
            sum_days_temp = 0.0
            days = 0
            # Loop through the temp data for the month
            for temp in months_temp_data:
                # Add the temp to the sum
                sum_days_temp += temp
                # Add a day to the days for this month
                days += 1

            # After doing this, we can preform a calculation to see what the average temp was for that month
            month_average_temp = sum_days_temp / days

            if month_average_temp > warmest_temp:
                warmest_temp = month_average_temp
                warmest_month = month

    # Print the result
    print(month_dict[warmest_month])


def option5():
    print("Available years:")
    print("-------------------")
    file_data = load_txt_file()
    # Loop through the years to see which years are available
    for year in file_data:
        print(year)
    print("-------------------")
    # Request an input from the user to select a year
    input_year = int(input("Select a year: "))

    # Create a dict in which we store the month's number to name conversion
    month_dict = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June", 7: "July", 8: "August",
                  9: "September", 10: "October", 11: "November", 12: "December"}

    # Create two variables in which we are going to store the
    # warmest month and associated average temperature for that month
    coldest_month = 0
    coldest_temp = 300

    # Loop through the years to see which years are available
    for year in file_data:
        # Retrieve the year's data from the dict
        year_data = file_data[year]

        # Loop through the year's data to see the available months
        for month in year_data:
            # Retrieve the list with temps for that month
            months_temp_data = year_data[month]

            # Create two variables in which we are going to store a
            # sum of the temperature per day in a month and the days in that month
            sum_days_temp = 0.0
            days = 0
            # Loop through the temp data for the month
            for temp in months_temp_data:
                # Add the temp to the sum
                sum_days_temp += temp
                # Add a day to the days for this month
                days += 1

            # After doing this, we can preform a calculation to see what the average temp was for that month
            month_average_temp = sum_days_temp / days

            if month_average_temp < coldest_temp:
                coldest_temp = month_average_temp
                coldest_month = month

    # Print the result
    print(month_dict[coldest_month])


def option6():
    # get the data from the file
    file_data = load_txt_file()

    # Create a list in which we will store the final data
    data_list = list()

    # Loop through the years to see which years are available
    for year in file_data:
        # Retrieve the year's data from the dict
        year_data = file_data[year]

        # Create an empty dict in which we are going to store the average temp per month
        year_data_dict = dict()

        # Loop through the year's data to see the available months
        for month in year_data:
            # Retrieve the list with temps for that month
            months_temp_data = year_data[month]

            # Create two variables in which we are going to store a
            # sum of the temperature per day in a month and the days in that month
            sum_days_temp = 0.0
            days = 0
            # Loop through the temp data for the month
            for temp in months_temp_data:
                # Add the temp to the sum
                sum_days_temp += temp
                # Add a day to the days for this month
                days += 1

            # After doing this, we can preform a calculation to see what the average temp was for that month
            month_average_temp = sum_days_temp / days

            if month not in year_data_dict:
                year_data_dict[month] = month_average_temp

        # After getting the average temperatures per month for a year,
        # we are going to create a tuple and add them to the list
        data_list.append((year, year_data_dict))

    # Print the results
    print(data_list)

# ----------------------------------------------------------------------------------------------------------
# This will only be run when the .py file gets run directly
if __name__ == "__main__":
    # Print the menu
    print_menu()
    # Request a choice from the user
    input_choice = int(input("Enter your choice: "))
    # Check which choice was selected
    if input_choice == 1:
        option1()
    elif input_choice == 2:
        option2()
    elif input_choice == 3:
        option3()
    elif input_choice == 4:
        option4()
    elif input_choice == 5:
        option5()
    elif input_choice == 6:
        option6()