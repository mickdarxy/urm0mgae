class PasswordManager:
    current_password = ""
    old_password = []



    def get_password(self):
        return self.current_password

    def set_password(self, new_password):
        self.old_password += self.current_password
        self.current_password = new_password
        return True

    def is_correct(self, attempt):
        if attempt == self.current_password:
            return True
        return False

#retrieves string and returns boolean depending on whether the string is equal to the current password
# the double check like on type in your password again
#just duplicate or take the string from get password

#The last item of the list old_passwords is the user’s current password.
#The set_password method should only change the password if the attempted-
# password is different from all the user’s past passwords.