import os
import sys
import json

with open('contacts.json') as json_file:
    data = json.load(json_file)
'''
print all contacts in the following format:
======================================
Position: <position>
First name: <firstname>
Last name: <lastname>
Emails: <email_1>, <email_2>
Phone numbers: <number_1>, <number_2>
'''



'''
return list of contacts sorted by first_name or last_name [if blank then unsorted], direction [ASC (default)/DESC])
'''

from operator import itemgetter
def list_contacts(addressbook):
    count = 0
    for key, value in data.items():
        count += 1
        print(f'''
        position: {value["id"]}
        First name: {value["first_name"]} 
        Last name: {value["last_name"]}
        Emails: {value["emails"]}
        Phone Numbers: {value["phone_numbers"]}
        ''')
    data_list = json.loads(open('addressbook.json').read())
    def custom_sort(item):
        return len(item["first_name"])
    sorted_list = json.dumps(sorted(data_list, key=itemgetter('first_name')))
    return sorted_list



'''
add new contact:
- first_name
- last_name
- emails = {}
- phone_numbers = {}
'''


def add_contact():
    new_contact_first_name = input("Enter new contact first name: ")
    new_contact_last_name = input("Enter new contact last name: ")
    new_contact_email = input("Enter new contact email: ")
    new_contact_phone_number = int(input("Enter new contact phone number\t"))

    data[str(len(data.keys()) + 1)] = {
        "first_name": new_contact_first_name,
        "last_name": new_contact_last_name,
        "emails": new_contact_email,
        "phone_numbers": new_contact_phone_number
    }
    with open('addressbook.json', 'w') as fileWrite:
        fileWrite.write(json.dumps(data))
print("Contact added successfully")




'''
remove contact by ID (integer)
'''


def remove_contact(func):
    flag, positionKey = func
    if flag:
        user_input = int(input("Enter # of the contact you want to remove\n"))
        data.pop(positionKey[user_input - 1])
        with open('addressbook.json', 'w') as fileWrite:
            fileWrite.write(json.dumps(data))
        print("Contact removed successfully")


'''
merge duplicates (automated > same fullname [firstname & lastname])
'''


def merge_contacts():
    data = json.loads("contacts.json")
    merge_dict = {}
    for contact in data:
        key = (contact["first_name"], contact["last_name"])
        if key not in merge_dict:
            merge_dict[key] = contact
        else:
            for email in contact["emails"]:
                if email not in merge_dict[key]["emails"]:
                    merge_dict[key]["emails"].append(email)
            for phone_number in contact["phone_numbers"]:
                if phone_number not in merge_dict[key]["phone_numbers"]:
                    merge_dict[key]["phone_numbers"].append(phone_number)
            if contact["id"] < merge_dict[key]["id"]:
                merge_dict[key]["id"] = contact["id"]
    data = list(merge_dict.values())
    with open("contacts.json", "w") as outfile:
        outfile.write(json.obj)

    #check if two objects have same first and last name
    #email phone number should be added to the highest position object
    #delete the old json objects
    #return new json object
    #print merge succesfully



'''
read_from_json
Do NOT change this function
'''


def read_from_json(filename) -> list:
    addressbook = list()
    # read file
    with open(os.path.join(sys.path[0], filename)) as outfile:
        json_data = json.load(outfile)
        # iterate over each line in data and call the add function
        for contact in json_data:
            addressbook.append(contact)

    return addressbook


'''
write_to_json
Do NOT change this function
'''


def write_to_json(filename, addressbook: list) -> None:
    json_object = json.dumps(addressbook, indent=4)

    with open(os.path.join(sys.path[0], filename), "w") as outfile:
        outfile.write(json_object)


'''
main function:
# build menu structure as following
# the input can be case-insensitive (so E and e are valid inputs)
# [L] List contacts
# [A] Add contact
# [R] Remove contact
# [M] Merge contacts
# [Q] Quit program
Don't forget to put the contacts.json file in the same location as this file!
'''


def main(json_file):
    addressbook = read_from_json(json_file)
    print("Welcome to the addressbook menu!")
    print("[L] List contacts")
    print("[A] Add contact")
    print("[R] Remove contact")
    print("[M] Merge Contacts")
    print("[Q] Quit Program")

    user_input = input("Select any of the options above:\t")
    if user_input == "L":
        print("-----List contacts-----")
        list_contacts()
    elif user_input == "A":
        print("-----Add contact-----")
        add_contact()
    elif user_input == "R":
        print("-----Remove contact-----")
        remove_contact()
    elif user_input == "M":
        print("-----Merge contacts-----")
        merge_contacts()
    elif user_input == "Q":
        print("-----Quit Program-----")
        sys.exit()
    else:
        print("-----No such option! Try again-----")



'''
calling main function: 
Do NOT change it.
'''
if __name__ == "__main__":
    main('contacts.json')
