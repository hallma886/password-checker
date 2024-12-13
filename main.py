# Matthew hall
# December 13, 2024
# Password Checker
password = input("Type your password: ")  
score = 0

# Check the password for specific characters  
lowercase = False
uppercase = False
number = False
punctuation = False
special_character = False  
for character in password:  
    if character in "abcdefghijklmnopqrstuvwxyz":  
        lowercase = True  
    elif character in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        uppercase = True
    elif character in "0123456789":
        number = True
    elif character in ".?!,:;_-[](){'}...":
        punctuation = True
    else:
        special_character = True
if lowercase == True:
    print("Your password contains lowercase characters.")
if uppercase == True:
    print("Your password contains uppercase characters.")
if number == True:
    print("Your password contains at least one number.")
if punctuation == True:
    print("Your password contains at least one punctuation sign.")
if special_character == True:
    print("Your password contains at least one special character.")

if lowercase == True and uppercase == True:
    score = score + 10
if number == True and (lowercase == True or uppercase == True):
    score = score + 10
if punctuation == True:
    score = score + 5
if special_character == True:
    score = score + 5
if len(password) >= 8:
    score = score + 5
    print("Your password is at least 8 characters long.")

print(f"Score: {score}")


















