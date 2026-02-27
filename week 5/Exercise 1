import string # Provides useful constants like string.ascii_uppercase, string.punctuation
import random # Useful for generating random elements, e.g., for hints or messages in Part C
# Part A: Individual Validation Functions
def check_min_length(password, min_len=8):
 """
 Check if password meets minimum length requirement.
 Args:
 password: The password string to validate
 min_len: Minimum required length (default: 8)
 Returns:
 Boolean indicating if password meets length requirement
 """
 return len(password) >= min_len
def has_uppercase(password):
 """
 Check if password contains at least one uppercase letter.
 Args:
 password: The password string to validate
 Returns:
 Boolean indicating presence of uppercase letters
 """
 # Demonstrates using string.ascii_uppercase for clarity
 return any(char in string.ascii_uppercase for char in password)
def has_lowercase(password):
 """
 Check if password contains at least one lowercase letter.
 Args:
 password: The password string to validate
 Returns:
 Boolean indicating presence of lowercase letters
 """
 # Demonstrates using string.ascii_lowercase for clarity
 return any(char in string.ascii_lowercase for char in password)
def has_digit(password):
 """
 Check if password contains at least one numeric digit.
 Args:
 password: The password string to validate
 Returns:
 Boolean indicating presence of digits
 """
 # Demonstrates using string.digits for clarity
 return any(char in string.digits for char in password)
def has_special_char(password):
 """
 Check if password contains at least one special character.
 Args:
 password: The password string to validate
 Returns:
 Boolean indicating presence of special characters
 """
 # Using string.punctuation for a comprehensive set of special characters
 return any(char in string.punctuation for char in password)
import string # Used for character sets like uppercase letters, punctuation, etc.
import random # Can be used for generating random elements (e.g., hints, future features)
# Part B: Master Validation Function
# Note: The individual validation functions (check_min_length, has_uppercase,
# has_lowercase, has_digit, has_special_char) are defined in the previous section.
# They implicitly use the 'string' module for character sets.
def validate_password(password):
 """
 Perform comprehensive password validation using all criteria.
 Args:
 password: The password string to validate
 Returns:
 Dictionary containing individual check results and overall validity
 """
 results = {
 'min_length': check_min_length(password),
 'has_uppercase': has_uppercase(password),
 'has_lowercase': has_lowercase(password),
 'has_digit': has_digit(password),
 'has_special': has_special_char(password)
 }
 # Overall validity requires all checks to pass
 results['is_valid'] = all(results.values())
 return results
# Part C: User Interface and Testing
def main():
 """
 Main program that tests password validation with user input.
 This function demonstrates basic input/output and conditional logic.
 """
 print("=" * 50)
 print("PASSWORD STRENGTH VALIDATOR")
 print("=" * 50)
 print("\nPassword Requirements:")
 print(" " Minimum 8 characters")
 print(" " At least one uppercase letter")
 print(" " At least one lowercase letter")
 print(" " At least one digit")
 print(" " At least one special character (!@#$%^&* etc.)") # Note: string.punctuation contains these
 print()
 # Get password from user using the built-in 'input()' function
 password = input("Enter password to validate: ")
 # Validate password by calling our 'validate_password' function
 results = validate_password(password)
 # Display results using 'print()' and f-strings for formatted output
 print("\n" + "=" * 50)
 print("VALIDATION RESULTS")
 print("=" * 50)
 # Individual criteria results
 # Using '7' and '' for clear visual feedback
 check_symbol = "7" if results['min_length'] else ""
 print(f"{check_symbol} Minimum length (8+ chars): {results['min_length']}")
 check_symbol = "7" if results['has_uppercase'] else ""
 print(f"{check_symbol} Contains uppercase: {results['has_uppercase']}")
 check_symbol = "7" if results['has_lowercase'] else ""
 print(f"{check_symbol} Contains lowercase: {results['has_lowercase']}")
 check_symbol = "7" if results['has_digit'] else ""
 print(f"{check_symbol} Contains digit: {results['has_digit']}")
 check_symbol = "7" if results['has_special'] else ""
 print(f"{check_symbol} Contains special char: {results['has_special']}")
 # Overall result
 print("\n" + "=" * 50)
 if results['is_valid']:
 print("7 PASSWORD IS STRONG!")
 else:
 print(" PASSWORD IS WEAK - Please address failed requirements")
 print("=" * 50)
 # The 'random' module (imported at the top) could be used here for
 # more advanced features, e.g., suggesting a random strong password component:
 # if not results['has_special']:
 # print(f"Hint: Try adding a special character like {random.choice(string.punctuation)}")
# Run the program only when the script is executed directly
if __name__ == "__main__":
 ma
