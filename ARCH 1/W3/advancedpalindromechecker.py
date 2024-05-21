#advancedpalindromechecker
def_punctuations = ''',.?!;'''
input_string = input("String: ")

stripped_string = input_string.strip()
cleaned_string = stripped_string.replace(" ", "")

for i in stripped_string:
    if i in def_punctuations:
        stripped_string = stripped_string.replace(i, "")

stripped_string = stripped_string.lower()

reversed_string = ""

for i in input_string:
    reversed_string = i + reversed_string


if (input_string == reversed_string):
    print(f"\"{input_string}\" is a palindrome")
else: 
    print(f"\"{input_string}\" is not a palindrome")
