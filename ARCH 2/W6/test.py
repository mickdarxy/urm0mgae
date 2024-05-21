# Create two dictionaries that contain the translation for characters to morse code
# and from morse code to standard characters
to_morse_code_dict = {"a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f": "..-.", "g": "--.", "h": "....",
                      "i": "..", "j": ".---", "k": "-.-", "l": ".-..", "m": "--", "n": "-.", "o": "---", "p": ".--.",
                      "q": "--.-", "r": ".-.", "s": "...", "t": "-", "u": "..-", "w": ".--", "v": "...-", "x": "-..-",
                      "y": "-.--", "z": "--..", ",": "--..--", ".": ".-.-.-", "?": "..--..", "!": "-.-.--"}
from_morse_code_dict = {".-": "a", "-...": "b", "-.-.": "c", "-..": "d", ".": "e", "..-.": "f", "--.": "g", "....": "h",
                        "..": "i", ".---": "j", "-.-": "k", ".-..": "l", "--": "m", "-.": "n", "---": "o", ".--.": "p",
                        "--.-": "q", ".-.": "r", "...": "s", "-": "t", "..-": "u", ".--": "w", "...-": "v", "-..-": "x",
                        "-.--": "y", "--..": "z", "--..--": ",", ".-.-.-": ".", "..--..": "?", "-.-.--": "!"}


# This function translates a message into a morse code string
def message_to_morse(message):
    # Create an empty list variable
    char_list = list()
    # Loop through the message and put every character into the list variable
    for char in message:
        char_list += char.lower()

    # Create an empty string in which we are going to store the morse code translation
    morse_code = ""
    # Loop through the characters of the message we are going to translate
    for char in char_list:
        # If the character is a space, put 3 spaces in that location
        if char == " ":
            morse_code += "   "
        # If the character is in the morse code dictionary
        elif char in to_morse_code_dict:
            # Retrieve the corresponding translation
            translated_char = to_morse_code_dict[char]

            # If the morse_code string is empty, then only add the translated character to the string
            if morse_code == "":
                morse_code += translated_char
            # Else put the character in string with a space in front of it
            else:
                morse_code += f" {translated_char}"
        # If it isn't possible to translate character then give a error message
        else:
            morse_code = f"Can't convert char {char} to morse code"
            break

    return morse_code


# This function translates a morse code string into a message
def morse_to_message(morse):
    # Split the morse code message
    splitted_morse = morse.split(" ")
    # Create an integer variable to see how many empty strings there are
    emptys = 0
    # Create an empty string variable that will store our message
    message = ""
    # Loop through the splitted morse code message
    for part in splitted_morse:
        # If the part is empty add 1 to the emptys integer
        if part == "":
            emptys += 1
            # If there are 3 empty's then add a space to the message
            if emptys == 3:
                message += " "
                emptys = 0
        # If the part is in our morse code dictionary then add the translated letter to our message
        if part in from_morse_code_dict:
            translated_char = from_morse_code_dict[part]
            message += translated_char

    return message


# This function will detect if an inputted text is a morse code message or a regular text message
# and the call the required function to translate it
def translate_text(text):
    is_morse = False
    for char in text:
        # If the first charter is a part of a more code then set the is_morse boolean to
        # true and then break out of the loop
        if char == "-" or char == ".":
            is_morse = True
            break
        elif char in to_morse_code_dict:
            break

    # If it is a morse code message, then translate it from morse code to a regular text message
    if is_morse:
        return morse_to_message(text)
    # If it is a normal message, then translate it into a morse code message
    else:
        return message_to_morse(text)


if __name__ == "__main__":
    input_message = input("Enter an message to translate: ")
    print(translate_text(input_message))