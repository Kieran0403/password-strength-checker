# password-strength-checker

A Python tool that analyses and scores the strength of a password using object-oriented programming principles.

## How It Works 🔧

The `PasswordChecker` class analyses a given password across multiple criteria and returns a strength score and rating.

Criteria checked ✅:
- Length — longer passwords score higher
- Uppercase and lowercase characters
- Numbers
- Special characters
- Checked against a list of commonly used passwords
- Checked against HaveIBeenPwnedAPI for data breaches

## 🛠️ Technical Architecture & Design Decisions

### Optimized Time Complexity with Python Sets
When checking if a password exists within the common passwords dataset, the application loads the file into a Python `set` rather than a standard `list`. 
* **List Lookup:** $O(n)$ time complexity, requiring a sequential scan through the file.
* **Set Lookup:** $O(1)$ average time complexity, utilizing a highly efficient hash table structure. This ensures that database lookups remain instantaneous, regardless of how large the password blacklist grows.

### Secure Remote Hashing via k-Anonymity API
To check if a password has been compromised in historical data breaches without exposing the user's actual credentials to the internet, the application implements the **Have I Been Pwned REST API** using a mathematical privacy technique called **k-Anonymity**:
1. **Local Hashing:** The application generates a 40-character hexadecimal SHA-1 hash of the password locally on the machine.
2. **The 5-Character Prefix:** The code extracts only the first 5 characters of this hash (the prefix) and sends them to the API endpoint. The remaining 35 characters (the suffix) never leave the local environment.
3. **Local Suffix Matching:** The API responds with a list of all known compromised password suffixes matching that prefix. The application then performs an internal look-up loop to see if the user's specific suffix is present, capturing the breach count dynamically.

To check if a password has been compromised in historical data breaches without exposing the user's actual credentials to the internet, the application implements the **Have I Been Pwned REST API** using a mathematical privacy technique called **k-Anonymity**:


### Data Authenticity Note
> **Project Dataset Note:** The `1000-most-common-passwords.txt` file utilized by this application is an uncurated, empirically sourced dataset derived from real-world historical data breaches (such as the standard RockYou dataset). It contains authentic user-generated strings—including profanity and colloquialisms—reflecting genuine human password behaviors. Retaining this data unfiltered is vital for ensuring accurate, real-world security validation.

---

## 📦 Project Structure & Workflow

```text
├── PasswordChecker.py              # Main class containing regex filters & scoring algorithms
└── 1000-most-common-passwords.txt  # Fast local O(1) dictionary lookup file
