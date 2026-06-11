import string,re
class PasswordChecker:
    def __init__(self,password):
        """Constructor to initialise the user's password to a variable

        Args:
            password (string): users password
        """
        self.password=password

    def check_length(self,password):
        """Method to find the length of a users password

        The longer the password is, the more secure they tend to be, so more points scored

        Args:
            password (string): users password
        """
        length=len(self)
        if length >= 16:
            return 2  # bonus point for very long passwords
        elif length >= 8:
            return 1
        else:
            return 0

    def check_special_chars(self):
        """Checks if the password contains any special characters

        Returns:
            boolean: if contains special chars
        """
        special_chars=string.punctuation #All the special chars from import
        return special_chars in self.password
            

    def check_uppercase(self):
        return bool(re.search(r'[A-Z]', self.password))
    def check_lowercase(self):
        return bool(re.search(r'[a-z]', self.password))
    def check_numbers(self):
        return 