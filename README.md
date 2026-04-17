# Password Strength Checker

This project checks the strength of a password based on different criteria such as length, uppercase letters, lowercase letters, digits, and special characters.

---

## 🧠 Concept

A strong password should include a combination of different character types.  
This program evaluates password strength using pattern matching and assigns a score.

---

## ⚙️ How it works

- Takes password input from the user  
- Checks for:
  - Minimum length (8 characters)  
  - Lowercase letters  
  - Uppercase letters  
  - Numbers  
  - Special characters  
- Assigns a score based on conditions  
- Displays password strength  

---

## 💻 Code

```python
import re

password = input("Enter your password: ")

strength = 0

if len(password) >= 8:
    strength += 1

if re.search("[a-z]", password):
    strength += 1

if re.search("[A-Z]", password):
    strength += 1

if re.search("[0-9]", password):
    strength += 1

if re.search("[@#$%^&*]", password):
    strength += 1

print("\nPassword Strength:")

if strength <= 2:
    print("Weak ❌")
elif strength == 3:
    print("Medium ⚠️")
else:
    print("Strong ✅")
```

---

## 🚀 Technologies Used

- Python  
- Regular Expressions (`re` module)  

---

## 📌 Future Improvements

- Provide suggestions to improve weak passwords  
- Add a graphical user interface (GUI)  
- Check against common or leaked passwords  
- Integrate with a web application for real-time use  

---
