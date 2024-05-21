def is_integer(unchecked: str) -> bool:
    input_is_integer = input("Check validity: unchecked()")
    cleaned_string = unchecked.strip()
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



def remove_non_integer(unchecked: str) -> int:
    input_string = input(unchecked)
    remove_char = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    only_integer = "".remove(remove_char)
    only_integer = int(only_integer)
    return only_integer



