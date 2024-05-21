import random
import string
#create a function to generate a random password
def generate_random_password():
    length = random.randint(7,10) #gives a random length of password between 7 and 10 characters
    password = ''.join(chr(random.randint(33,126))) #chooses random characters on the ASCII scale
    for _ in range(length):
        return password

random_password = generate_random_password()
print(random_password)
