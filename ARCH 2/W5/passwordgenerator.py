import random
import string

def generate_random_password(): #create a function to generate a random password
    length = random.randint(7,10) #gives a random length of password between 7 and 10 characters
    password = "" #empty string to store the password into
    for _ in range(length): #for loop that puts a random character in every digit slot for the randomized length
        password += ''.join(chr(random.randint(33,126)))
    return password

random_password = generate_random_password() #variable for output
print(f"Random Password: {random_password}") #clean output with an f string