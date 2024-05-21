input_string = input("String: ")

reversed_string = ""
for i in reversed(input_string):
    reversed_string += i

if reversed_string == input_string:
    print(f"\"{input_string}\" is a palindrome")
else:
    print(f"\"{input_string}\" is not a palindrome")