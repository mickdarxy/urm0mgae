# define a function that checks whether string has only integers or not
def is_integer(unchecked: str) -> bool:
    #strip the string of any trailing whitespace
    cleaned_string = unchecked.strip()
    #if loop for validity check
    if cleaned_string.isdigit == True and len(cleaned_string) >= 1:
        cleaned_string = True
        print("Valid Integer")
    elif cleaned_string[0] == "-" or "+":
        cleaned_string = True
        print("Valid Integer")
    else:
        cleaned_string = False
        print("Invalid integer")
    return cleaned_string


#create a function that removes everything that isnt an integer
def remove_non_integer(unchecked: str) -> int:
    input_string = unchecked
    #unwanted characters
    remove_char = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    only_integer = "".remove(remove_char)
    only_integer = int(only_integer)
    return only_integer

#call main function
if __name__ == "__main__":
    input_integercheck = input()
    print(is_integer(input_integercheck))
