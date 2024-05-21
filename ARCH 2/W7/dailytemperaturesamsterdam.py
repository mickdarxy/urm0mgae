import os
import sys


def load_txt_file(file_path):
    file = open("NLAMSTDM.txt", "r")
    file_content = file.readlines()
    file.close()

    clean_file_content = []
    for line in file_content:
        line = line.strip()
        temp_list_line = line.split(" ")
        list_line = []

        for item in temp_list_line:
            if item != '':
                list_line.append(item)
        clean_file_content.append(list_line)

    dict_file_data = dict()
    for line in clean_file_content:
        line_data_month = int(line[0])
        line_data_year = int(line[2])
        line_data_temp = float(line[3])

        if line_data_month not in dict_file_data:
            dict_file_data[line_data_year] = dict()

        if line_data_month not in dict_file_data[line_data_year]:
            dict_file_data[line_data_year][line_data_month] = list()

        dict_file_data[line_data_year][line_data_month].append(line_data_temp)

    return dict_file_data

def fahrenheit_to_celsius(fahrenheit: float) -> float:
    return (fahrenheit - 32) * 5 / 9

def average_temp_per_month(temperatures_per_year: dict) -> list:
    return_data = list()

    for month in temperatures_per_year:
        months_temp_data = temperatures_per_year[month]
        sum_days_temp = 0.0
        days = 0
        for day in months_temp_data:
            sum_days_temp += temp
            days += 1

        return_data.append((month, sum_days_temp / days))

    return return_data

def average_temp_per_year(temperatures: dict) -> list:
    return_data = list()

    for year in temperatures:
        year_data = temperatures[year]
        sum_days_temp = 0.0
        months = 0

        for month in year_data:
            months_temp_data = year_data[month]
            sum_days_temp = 0.0
            days = 0

            for temp in months_temp_data:
                sum_days_temp += temp
                days += 1

            month_average = sum_days_temp / days
            sum_month_temp += month_average_temp
            months += 1
        return_data.append((year, sum_month_temp / months))
    return_data

def main_menu():
    print("[1] Print the average temperatures per year (fahrenheit)")
    print("[2] Print the average temperatures per year (celsius) Hint: Use built-in map() function.")
    print("[3] Print the warmest and coldest year as tuple based on the average temperature")
    print("[4] Print the warmest month of a year based on the input year of the user (full month name)")
    print("[5] Print the coldest month of a year based on the input year of the user (full month name)")
    print("[6] Print a list of tuples where the first element of each tuple is the year and")
    print("    the second element of the tuple is a dictionary with months as the keys and")
    print("    the average temperature (in Celsius) of each month as the value")

def option1():
    file_path = load_txt_file()
    average_temp_data = average_temp_per_year(file_data)
    for row in average_temp_data:
        data_year = row[0]
        data_temp = row[1]
        print(f"{data_year} - {data_temp}")

def option2():
    file_path = load_txt_file()
    average_temp_data = average_temp_per_year(file_data)
    for row in average_temp_data:
        data_year = row[0]
        data_temp = float(row[1])
        data_temp_celsius = fahrenheit_to_celsius(data_temp)
        print(f"{data_year} - {data_temp_celsius}")

def option3():
    file_path = load_txt_file()
    average_temp_data = average_temp_per_year(file_data)
    warm_year = 0
    warm_temp = 0.0
    cold_year = 0
    cold_temp = 300.0

    for row in average_temp_data:
        data_year = row[0]
        data_temp = float(row[1])

        if data_temp > warm_temp:
            warm_year = data_year
            warm_temp = data_temp

        if data_temp < cold_temp:
            cold_year = data_year
            cold_temp = data_temp

    print((warm_year, warm_temp))
    print((cold_year, cold_temp))

def option4():



