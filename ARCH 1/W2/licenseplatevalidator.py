#licenseplatevalidator

input_licenseplate = input("License: ")

if len(input_licenseplate) == 8:
    splitinput_licenseplate = input_licenseplate.split("-")

    if len(splitinput_licenseplate) < 0 or len(input_licenseplate) > 3:
        print("Invalid")
    else:
        list_parts_type = []
        list_parts_char_num = []
        invalid_parts = 0
        part = 0 

        for i in splitinput_licenseplate:
            if len(i) <= 3 and part != 1:

                if i.isalpha():
                    part += 1
                    list_parts_typen += "a"
                elif i.isnumeric():
                    part += 1
                    list_parts_type += "n"
                else:
                    invalid_parts += 1
                    part += 1
                
                list_parts_char_num.append(len(i))
            elif part == 1 and len(i) != 1:
                if i.isalpha():
                    part += 1
                    list_parts_type += "a"
                elif i.isnumeric():
                    part += 1
                    list_parts_type += "n"
                else: 
                    invalid_parts += 1
                    part += 1

                list_parts_char_num.append(len(i))
            else:
                invalid_parts += 1
                part += 1
        if invalid_parts == 0:
            check_validity = False

            print(f"list_parts_type: {list_parts_type}")
            print(f"list_parts_char_num: {list_parts_char_num}")

            if list_parts_type == ["a", "n", "n"] and list_parts_char_num == [2,2,2]:
                check_validity = True
            elif list_parts_type == ["n", "n", "a"] and list_parts_char_num == [2,2,2]:
                check_validity = True
            elif list_parts_type == ["n", "a", "n"] and list_parts_char_num == [2,2,2]:
                check_validity = True
            elif list_parts_type == ["a", "n", "a"] and list_parts_char_num == [2,2,2]:
                check_validity = True
            elif list_parts_type == ["a", "a", "n"] and list_parts_char_num == [2,2,2]:
                check_validity = True
            elif  list_parts_type == ["n", "a", "a"] and list_parts_char_num == [2,3,1]:
                check_validity = True
            elif  list_parts_type == ["n", "a", "n"] and list_parts_char_num == [1,3,2]:
                check_validity = True
            elif  list_parts_type == ["n", "a", "n"] and list_parts_char_num == [2,3,1]:
                check_validity = True
            elif list_parts_type == ["a", "n", "a"] and list_parts_char_num == [1,3,2]:
                check_validity = True
            elif list_parts_type == ["a", "n", "a"] and list_parts_char_num == [3,2,1]:
                check_validity = True
            elif  list_parts_type == ["n", "a", "n"] and list_parts_char_num == [1,2,3]:
                check_validity = True
            else:
                check_validity = False
            
            if check_validity:
                print("Valid")
            else:
                print("Invalid")
        else:
            print("Invalid")
else:
    print("Invalid")


    