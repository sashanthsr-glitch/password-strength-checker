# Password Strength Checker

import re

password = input("Enter your password: ")

strength = 0

# Length check
if len(password) >= 8:
    strength += 1

# Lowercase check
if re.search("[a-z]", password):
    strength += 1

# Uppercase check
if re.search("[A-Z]", password):
    strength += 1

# Digit check
if re.search("[0-9]", password):
    strength += 1

# Special character check
if re.search("[@#$%^&*]", password):
    strength += 1

# Result
print("\nPassword Strength:")

if strength <= 2:
    print("Weak ❌")

elif strength == 3:
    print("Medium ⚠️")

else:
    print("Strong ✅")

