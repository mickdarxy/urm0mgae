dict_key_value = {}
encoded_values = []
decoded_values = []
default_key = "a_b?c9d6e1f4g!h:i<j|k{l0m@n7o+p~q2r+s/t=u^v3w]x(y-z>A*B8C;D%E#F}G5H)I[J$"


# This function encodes a string and returns the encoded string as a result
def encode_string(data: str, key: str = None) -> str:
    # Create an empty dict in which we store the key for encoding
    encoding_dict = dict()

    # First preform a check to see if there is a key given when the function was called.
    # If not, check if there is already a dict_key_value.
    # And if that one also isn't filled, then use the default_key value
    if key is None:
        if dict_key_value == {}:
            key = default_key
        else:
            key = "use_dict_value"

    # Second, we check if we need to use the dict_key_value,
    # if we don't need to use this, then we will loop through the given key
    if key != "use_dict_value":
        # Use 2 pos values to make it possible to loop through the key value and extract the required values
        pos1 = 0
        pos2 = 1
        for i in range(int(len(key) / 2)):
            # Extract the key and the value from the key string
            key_key = key[pos1]
            key_value = key[pos2]

            # Check if the key has already been created in our dict, if not then we add the key and its value
            if key_key not in encoding_dict:
                encoding_dict[key_key] = key_value

            # Move the 2 pos variables to the next position
            pos1 += 2
            pos2 += 2
    else:
        encoding_dict = dict_key_value

    # Create an empty string in which we are going to store our encoded string
    return_data = ""

    # Third, we encode the data (string)
    for i in data:
        if i not in encoding_dict:
            return_data += i
        else:
            return_data += encoding_dict[i]

    # After encoding, we add the encoded data to our encoded list and we return the result
    encoded_values.append(return_data)
    return return_data


# This function decodes a string and returns the decoded string as a result
def decode_string(data: str, key: str = None) -> str:
    # Create an empty dict in which we store the key for decoding
    decoding_dict = dict()

    # First preform a check to see if there is a key given when the function was called.
    # If not, check if there is already a dict_key_value.
    # And if that one also isn't filled, then use the default_key value
    if key is None:
        if dict_key_value == {}:
            key = default_key
        else:
            key = "use_dict_value"

    # Second, we check if we need to use the dict_key_value,
    # if we don't need to use this, then we will loop through the given key
    if key != "use_dict_value":
        # Use 2 pos values to make it possible to loop through the key value and extract the required values
        pos1 = 0
        pos2 = 1
        for i in range(int(len(key) / 2)):
            # Extract the key and the value from the key string
            key_key = key[pos1]
            key_value = key[pos2]

            # Check if the key has already been created in our dict, if not then we add the key and its value
            if key_key not in decoding_dict:
                decoding_dict[key_key] = key_value

            # Move the 2 pos variables to the next position
            pos1 += 2
            pos2 += 2
    else:
        decoding_dict = dict_key_value

    # Create an empty string in which we are going to store our decoded string
    return_data = ""

    # Third, we decode the data (string)
    for i in data:
        decode_value_found = False
        for e in decoding_dict:
            if i == decoding_dict[e]:
                decode_value_found = True
                return_data += e
        if not decode_value_found:
            return_data += i

    # After encoding, we add the encoded data to our encoded list and we return the result
    decoded_values.append(return_data)
    return return_data


# This function encodes a list and returns an encoded list as a result
def encode_list(data: list, key: str = None) -> list:
    # Create an empty return list
    return_list = []
    # Loop through the list and encode the value, after this add it to the return list
    for item in data:
        return_list.append(encode_string(item, key))
    # Return the list
    return return_list


# This function decodes a list and returns a decoded list as a result
def decode_list(data: list, key: str = None) -> list:
    # Create an empty return list
    return_list = []
    # Loop through the list and decode the value, after this add it to the return list
    for item in data:
        return_list.append(decode_string(item, key))
    # Return the list
    return return_list


# create a function that given an encoded value, decoded value and a key (optional) checks if the values are correct,
# the return value should be a boolean value (True if values match, False if they don't match)
def validate_values(encoded: str, decoded: str, key: str = None) -> bool:
    # Create an empty dict in which we store the key for decoding
    decoding_dict = dict()

    # First preform a check to see if there is a key given when the function was called.
    # If not, check if there is already a dict_key_value.
    # And if that one also isn't filled, then use the default_key value
    if key is None:
        if dict_key_value == {}:
            key = default_key
        else:
            key = "use_dict_value"

    # Second, we check if we need to use the dict_key_value,
    # if we don't need to use this, then we will loop through the given key
    if key != "use_dict_value":
        # Use 2 pos values to make it possible to loop through the key value and extract the required values
        pos1 = 0
        pos2 = 1
        for i in range(int(len(key) / 2)):
            # Extract the key and the value from the key string
            key_key = key[pos1]
            key_value = key[pos2]

            # Check if the key has already been created in our dict, if not then we add the key and its value
            if key_key not in decoding_dict:
                decoding_dict[key_key] = key_value

            # Move the 2 pos variables to the next position
            pos1 += 2
            pos2 += 2
    else:
        decoding_dict = dict_key_value

    # Create an empty string in which we are going to store our decoded string
    decoded_data = ""

    # Third, we decode the data (string)
    for i in encoded:
        decode_value_found = False
        for e in decoding_dict:
            if i == decoding_dict[e]:
                decode_value_found = True
                decoded_data += e
        if not decode_value_found:
            decoded_data += i

    # Then we check if the inputted decoded string is the same as the decoded string
    if decoded_data == decoded:
        return True
    else:
        return False


# give the option to input a hashvalue to be used/converted to a key
# each oneven character is the Key of the Dict, each even character is the coresponding Value
# you should validate if the given input is an even input, otherwise show the error: Invalid hashvalue input
# example: a@b.c>d#eA will become: {'a': '@', 'b': '.', 'c': '>', 'd', '#', 'e': 'A'}
def set_dict_key(key: str) -> None:
    pos1 = 0
    pos2 = 1
    for i in range(int(len(key) / 2)):
        # Extract the key and the value from the key string
        key_key = key[pos1]
        key_value = key[pos2]

        # Check if the key has already been created in our dict, if not then we add the key and its value
        if key_key not in dict_key_value:
            dict_key_value[key_key] = key_value

            # Move the 2 pos variables to the next position
            pos1 += 2
            pos2 += 2


# build menu structure as following
# the input can be case-insensitive (so E and e are valid inputs)
# [E] Encode value to hashed value
# [D] Decode hashed value to normal value
# [P] Print all encoded/decoded values
# [V] Validate 2 values against eachother
# [Q] Quit program
def print_menu():
    print("[E] Encode value to hashed value")
    print("[D] Decode hashed value to normal value")
    print("[P] Print all encoded/decoded values")
    print("[V] Validate 2 values against eachother")
    print("[Q] Quit program")


def main():
    con = True
    # First, we request a default key, Then we while first try and validate it.
    # If this can't be done, we are going to give an error message and request a valid one.
    # If the user doesn't provide one, we are going to use a predefined one
    input_key = input("Key: ")
    if input_key != "":
        if len(input_key) / 2 != round(len(input_key) / 2):
            con = False
            print("Invalid hashvalue input")
        else:
            set_dict_key(input_key)
    else:
        set_dict_key(default_key)

    if con:
        while True:
            print_menu()
            input_menu_choice = input("Enter your choice: ").upper()
            if input_menu_choice == "Q":
                print("Exiting program, See you next time!")
                break
            elif input_menu_choice == "E":
                input_data = input("Enter a string for encoding: ")

                multi = False
                # Detect if there are multiple values to be encoded (Separated by comma)
                for char in input_data:
                    if char == ",":
                        multi = True

                if multi:
                    list_input_data = input_data.replace(" ", "").split(",")
                    print(encode_list(list_input_data))
                else:
                    print(encode_string(input_data))

            elif input_menu_choice == "D":
                input_data = input("Enter a string for decoding: ")

                multi = False
                # Detect if there are multiple values to be encoded (Separated by comma)
                for char in input_data:
                    if char == ",":
                        multi = True

                if multi:
                    list_input_data = input_data.replace(" ", "").split(",")
                    print(decode_list(list_input_data))
                else:
                    print(decode_string(input_data))

            elif input_menu_choice == "P":
                print("Encoded values:")
                for i in encoded_values:
                    print(i)
                print("Decoded values:")
                for i in decoded_values:
                    print(i)
            elif input_menu_choice == "V":
                input_encoded_value = input("Enter an encoded string: ")
                input_decoded_value = input("Enter an decoded string: ")
                print(validate_values(input_encoded_value, input_decoded_value))
            else:
                print("Invalid input, please select an option.")


# Create an unittest for both the encode and decode function (see test_namehasher.py file for boilerplate)
if __name__ == "__main__":
    main()