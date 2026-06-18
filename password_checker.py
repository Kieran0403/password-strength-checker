import string,re
import requests,hashlib
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

    def check_pwned_api(self):
        """Method to check if passwrod involved in a data breach

        Returns:
            boolean: if password in a data breach
        """
        # Step 1: Hash the password using SHA-1
        sha1_password = hashlib.sha1(self.password.encode('utf-8')).hexdigest().upper()
        
        # Step 2: Split into 5-character prefix and the remaining suffix
        prefix = sha1_password[:5]
        suffix = sha1_password[5:]

        # Step 3: Query the API with ONLY the prefix
        url = f"https://api.pwnedpasswords.com/range/{prefix}"

        try:
            # Setting a user-agent header is a standard requirement for APIs
            headers = {'User-Agent': 'Student-Project'}
            response = requests.get(url, headers=headers, timeout=5)
            
            if response.status_code != 200:
                print(f"Error fetching data from API: Status code {response.status_code}")
                return False
                
            # Step 4: Parse the response. The API returns lines of "SUFFIX:COUNT"
            hashes = (line.split(':') for line in response.text.splitlines())
            
            # Step 5: Check if our suffix matches any in the returned list
            for target_suffix, count in hashes:
                if target_suffix == suffix:
                    return int(count)  # Found a match! Return breach count.
            
            return False  # Password was not found in any data breaches
        except requests.RequestException as e:
            print(f"API connection error: {e}")
            return False

    def calculate_score(self):
        """Method to calcuate the score, if password common or pwned, immediatley very weak

        Returns:
            string: strength of the password
        """

        # 1. Local Check if it's a blacklisted common password
        if not self.check_common_passwords():
            return "Very weak"

        # 2. Check the API result
        leak_result = self.check_pwned_api()

        # If leak_result is an integer count greater than 0, it has been compromised
        if leak_result:  
            return f"Very Weak (Compromised in {leak_result:,} data breaches!)"

        
            
        # 3. Sum up the points from individual criteria
        score = 0
        score += self.check_length()
        score += int(self.check_uppercase())
        score += int(self.check_lowercase())
        score += int(self.check_numbers())
        score += int(self.check_special_characters())
        
        # 4. Determine strength classification (Max possible score is 6)
        if score <= 2:
            return "Weak"
        elif score <= 4:
            return "Fair"
        elif score == 5:
            return "Strong"
        else:
            return "Very Strong"

def main():
    test_cases = [
        # 1. Local File Check (Triggers first, skips the API call entirely)
        ("qwerty", "Should be 'Very weak' (Caught locally in <1ms)"),
        
        # 2. API Leaked Check (Passes local file, caught by the internet)
        ("Password123!", "Should be 'Very Weak' (Caught by HIBP API)"),
        
        # 3. API Low-Leak Check (Passes local file, caught by the internet)
        ("python123", "Should be 'Very Weak' (Caught by HIBP API)"),
        
        # 4. Clean Passwords (Passes both, calculates score criteria)
        ("abc", "Should be 'Weak' (Too short)"),
        ("P@ss1", "Should be 'Fair' (Under 8 chars)"),
        ("YorkComputerScience2026!", "Should be 'Very Strong' (Hits 16+ character bonus)"),
        ("Correct-Horse-Battery-Staple-2026!", "Should be 'Very Strong'")
    ]
    
    print("=" * 85)
    print(" PASSWORD CHECKER INTEGRATION TEST SUITE ")
    print("=" * 85)
    print(f"{'Password Tested':<40} | {'Expected Classification':<25} | {'Actual Result'}")
    print("-" * 85)
    
    for pwd, expectation in test_cases:
        checker = PasswordChecker(pwd)
        result = checker.calculate_score()
        
        print(f"{pwd:<40} | {expectation:<25} | {result}")
        print("-" * 85)

if __name__ == "__main__":
    main()