# Assignment description
# Create a program that can convert a name/string to the hashed representation of that value.
#
# Menu structure (case insensitive):
# [E] Encode value to hashed value
# [D] Decode hashed value to normal value
# [P] Print all encoded/decoded values
# [V] Validate 2 values against eachother
# [Q] Quit program
# Criteria:
# Create a function that given the input string converts it to the encoded/decoded equivalent based on the provided or already set key.
# Make sure to only convert values that are in the key, if the value is not present, use its own value:
#
# encode_string(data: str, key: str = None) -> str:
# decode_string(data: str, key: str = None) -> str:
# Create a function that given a list of inputs converts the complete list to the encoded/decoded equivalent based on the key.
# You can use the already created encode/decode function when looping through the list. Tip! Make use of the map function within Python with a lambda to call the internal function with all elements [element, key] as a return value, you should return a list with the converted values:
#
# encode_list(data: list, key: str = None) -> list:
# decode_list(data: list, key: str = None) -> list:
# Create a function that given a encoded value, decoded value and a key (optional) checks if the values are correct the return value should be a boolean value (True if values match, False if they don't match):
#
# validate_values(encoded: str, decoded: str, key: str = None) -> bool:
# Create a function that given a key, converts to a key (Dict) to be used for converting:
#
# each oneven character is the Key of the Dict, each even character is the coresponding Value
# you should validate if the given input is an even input, otherwise show the error: Invalid hashvalue input
# example: a@b.c>d#eA will become: {'a': '@', 'b': '.', 'c': '>', 'd', '#', 'e': 'A'}
# set_dict_key(conversion_string: str) -> None:
# Extra:
# For ease of use, you can use the following string as a default key to use within your program:
# a_b?c9d6e1f4g!h:i<j|k{l0m@n7o+p~q2r+s/t=u^v3w]x(y-z>A*B8C;D%E#F}G5H)I[J$
# To test your functions, use the provided unit test file.
# Input example:
# Key: A%B&C(D)E*F+G-H/I0J<K=L1M!N9O?P>Q7R#S5T;U:V[W]X~Y$Z@
# E
# PETER
# P
# Q
# Output example:
# >*;*#


import sys

dict_key_value = {}
encoded_values = []
decoded_values = []
default_key = "a_b?c9d6e1f4g!h:i<j|k{l0m@n7o+p~q2r+s/t=u^v3w]x(y-z>A*B8C;D%E#F}G5H)I[J$"

# create a function that given the input string converts it to the encoded equivalent based on the provided or already set key/hashmap
# make sure to only convert values that are in the key, if the value is not present, use its own value
def encode_string(data: str, key: str = None) -> str:
    encoding_dict = dict()


# create a function that given the input string converts it to the decoded equivalent based on the provided or already set key/hashmap
# make sure to only decode values that are in the key, if the value is not present, use its own value
def decode_string(data: str, key: str = None) -> str:


# create a function that given a list of inputs converts the complete list to the encoded equivalent based on the key/hashmap
# you can use the already created encode function when looping through the list
# tip! make use of the map function within python with a lambda to call the internal function with all elements
# as a return value, you should return a list with the converted values
def encode_list(data: list, key: str = None) -> list:


# create a function that given a list of inputs converts the complete list to the encoded equivalent based on the key/hashmap
# you can use the already created decode function when looping through the list
# tip! make use of the map function within python with a lambda to call the internal function with all elements
# as a return value, you should return a list with the converted values
def decode_list(data: list, key: str = None) -> list:


# create a function that given a encoded value, decoded value and a key (optional) checks if the values are correct
# the return value should be a boolean value (True if values match, False if they don't match)
def validate_values(encoded: str, decoded: str, key: str = None) -> bool:


# give the option to input a hashvalue to be used/converted to a key
# each oneven character is the Key of the Dict, each even character is the coresponding Value
# you should validate if the given input is an even input, otherwise show the error: Invalid hashvalue input
# example: a@b.c>d#eA will become: {'a': '@', 'b': '.', 'c': '>', 'd', '#', 'e': 'A'}
def set_dict_key(key: str) -> None:


# build menu structure as following
# the input can be case-insensitive (so E and e are valid inputs)
# [E] Encode value to hashed value
# [D] Decode hashed value to normal value
# [P] Print all encoded/decoded values
# [V] Validate 2 values against eachother
# [Q] Quit program
def main():
    print("Welcome to the namehasher directory!")
    print("[E] Encode value to hashed value")
    print("[D] Decode hashed value to normal value")
    print("[P] Print all encoded/decoded values")
    print("[V] Validate 2 values against eachother")
    print("[Q] Quit program")
    user_input = input("Select any of the options above:\t")
        if user_input == "E":
            print("-----Encode value-----")
            encode_string()
        elif user_input == "D":
            print("-----Decode value to normal-----")
            decode_string()
        elif user_input == "P":
            print("-----Print all decoded/encoded values-----")
            print("decoded values: \n", decoded_values)
            print("encoded values: \n", encoded_values)
        elif user_input == "V":
            print("-----Validate 2 values-----")
            validate_values()
        elif user_input == "Q":
            print("-----Quit Program-----")
            sys.exit()
        else:
            print("-----No such option! Try again-----")
            sys.exit()

# Create a unittest for both the encode and decode function (see test_namehasher.py file for boilerplate)
if __name__ == "__main__":
    main()