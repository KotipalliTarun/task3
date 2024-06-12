import random
import string

# User input for number of passwords and password length
number_of_passwords = int(input("How many passwords do you want to generate? "))
password_length = int(input("Provide the password length: "))

# Define characters (letters, digits, and punctuation)
characters = string.ascii_letters + string.digits + string.punctuation

# Generate multiple passwords
for password_index in range(number_of_passwords):
    password = ""
    for index in range(password_length):
        password += random.choice(characters)
    print(f"Password {password_index + 1}: {password}")