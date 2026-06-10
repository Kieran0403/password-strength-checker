class PasswordChecker:
    def __init__(self,password):
        """Constructor to initialise the user's password to a variable

        Args:
            password (string): users password
        """
        self.password=password

    def check_length(self,password):
        """Method to find the length of a users password

        The longer the password is, the more secure they tend to be

        Args:
            password (string): users password
        """
        length=len(self.password)

