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

## 🛠️ Technical Architecture & Design Decisions

### Optimized Time Complexity with Python Sets
When checking if a password exists within the common passwords dataset, the application loads the file into a Python `set` rather than a standard `list`. 
* **List Lookup:** $O(n)$ time complexity, requiring a sequential scan through the file.
* **Set Lookup:** $O(1)$ average time complexity, utilizing a highly efficient hash table structure. This ensures that database lookups remain instantaneous, regardless of how large the password blacklist grows.

### Data Authenticity Note
> **Project Dataset Note:** The `1000-most-common-passwords.txt` file utilized by this application is an uncurated, empirically sourced dataset derived from real-world historical data breaches (such as the standard RockYou dataset). It contains authentic user-generated strings—including profanity and colloquialisms—reflecting genuine human password behaviors. Retaining this data unfiltered is vital for ensuring accurate, real-world security validation.

