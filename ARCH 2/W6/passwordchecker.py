'''In an application a valid password must be a combination of digits,
uppercase and lowercase letters  and only four symbols * @ ! ?.
Implement a Python program that asks the password of the user and checks if it is a valid password.

Criteria:
-------------------------------------------------------------------------------------------------
The length of the password must not be less than 8 characters and must not be more than 20 characters.
In case the password is not valid, the user can try maximum three times to validate the password.
Print Valid on a validated password and Invalid on a unvalidated password.
Use sets and set operations to solve this problem.
-------------------------------------------------------------------------------------------------

Input example:
=================================================================================================
Password: B4s3c4p
=================================================================================================

Output example:
=================================================================================================
Password is invalid
================================================================================================='''
import random

def password_checker(password):
    #if password is shorter than 8 characters and longer than 20 discontinue the loop
    if len(password) < 8 and len(password) > 20:
        return False
    #use sets
    #output is invalid or valid
#if password is invalid return the input and give user 3 more times to validate

    sets = set()
    allowed_symbols = {'*', '@', '!', '?'}
    used_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
    small_letters = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'}
    big_letters = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'}


