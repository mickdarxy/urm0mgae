import sqlite3
if __name__ == "__main__":
    school = sqlite3.connect('school.sqlite')
    #school.close()

#tell a query to ask the database what to select
# 3 quotes like docstrings
#kinda like a coffee machine or a soda dispenser
query = '''SELECT name, date_of_birth FROM students'''
students = school.execute(query)
#loop to show retrieved information
for student in students:
    print(student)
