import string,re
class PasswordChecker:
    def __init__(self,password):
        """Constructor to initialise the user's password to a variable

        Args:
            password (string): users password
        """
        self.password=password

    def check_length(self):
        """Method to find the length of a users password

        The longer the password is, the more secure they tend to be, so more points scored

        Args:
            password (string): users password
        """
        length=len(self.password)
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
        """Checks if the string contains uppercase characters

        Returns:
            boolean: if uppercase detected
        """
        return bool(re.search(r'[A-Z]', self.password))
    def check_lowercase(self):
        """Checks if the string contains lowercase characters

        Returns:
            boolean: if lowercase detected
        """
        return bool(re.search(r'[a-z]', self.password))
    def check_numbers(self):
        """Checks if the string contains numbers

        Returns:
            boolean: if numbers detected
        """
        return bool(re.search(r'[0-9]', self.password))
    
    def check_special_characters(self):
        """Checks if the string contains special chars

        Returns:
            boolean: if special chars detected
        """
        return bool(re.search(r'[!"#$%&\'()*+,\-./:;<=>?@[\]^_`{|}~]', self.password))
    
    def check_common_passwords(self):
        """CHecks text file of 1000 most common passwords and checks if user password is in that list

        Returns:
            boolean: returns if the password is NOT in the list
        """
        try:
            with open("1000-most-common-passwords.txt") as f:
                common_passwords = set(f.read().splitlines())
            return self.password.lower() not in common_passwords
        except FileNotFoundError:
            # Fallback if the text file isn't in the directory
            return True

    def calculate_score(self):
        # 1. Check if it's a blacklisted common password
        if not self.check_common_passwords():
            return "Very weak"
            
        # 2. Sum up the points from individual criteria
        score = 0
        score += self.check_length()
        score += int(self.check_uppercase())
        score += int(self.check_lowercase())
        score += int(self.check_numbers())
        score += int(self.check_special_characters())
        
        # 3. Determine strength classification (Max possible score is 6)
        if score <= 2:
            return "Weak"
        elif score <= 4:
            return "Fair"
        elif score == 5:
            return "Strong"
        else:
            return "Very Strong"

def main():
    # Testing with actual examples from your common passwords list, 
    # plus some secure variations to verify all scoring tiers.
    test_cases = [
        # Should be caught by your text file (Very Weak)
        ("123456", "Should be 'Very weak' (Matches the list)"),
        ("password", "Should be 'Very weak' (Matches the list)"),
        ("qwerty", "Should be 'Very weak' (Matches the list)"),
        
        # Testing length and character types (Not in your list)
        ("abc", "Should be 'Weak' (Too short, only lowercase)"),
        ("P@ss1", "Should be 'Fair' (Has variety, but under 8 characters)"),
        ("YorkUni2026!", "Should be 'Strong' (Meets length and character variety)"),
        ("Correct-Horse-Battery-Staple-2026!", "Should be 'Very Strong' (Hits the 16+ character bonus length)")
    ]
    
    print("=" * 70)
    print(" PASSWORD CHECKER PERFORMANCE TEST ")
    print("=" * 70)
    print(f"{'Password Tested':<40} | {'Expected Classification':<25} | {'Actual Result'}")
    print("-" * 70)
    
    for pwd, expectation in test_cases:
        checker = PasswordChecker(pwd)
        result = checker.calculate_score()
        
        # Prints everything in a clean, aligned table format
        print(f"'{pwd}':<40 | {expectation:<25} | {result}")

if __name__ == "__main__":
    main()