# Import string module

import string


# Store the digits, lowercase, uppercase and punctuation

List1 = list(string.ascii_uppercase)
List2 = list(string.ascii_lowercase)
List3 = list(string.punctuation)
List4 = list(string.digits)


# Ask the user to input the number of password characters

Num = input("Please, Enter the number of password characters you prefere\n")


# Test the input

while True:
    try:
        Num = int(Num)
        if Num < 6:
           Num = input("Please, Enter more than six\n")
        else:
            break
    except:
        Num = input("Please, Enter just numbers\n")


# import randam module

import random


# Shuffling List1, List2, List3 and List4

random.shuffle(List1)
random.shuffle(List2)
random.shuffle(List3)
random.shuffle(List4)


# Set the percentages

percentage1 = round(Num * (30/ 100))
percentage2 = round(Num * (20/ 100))


# Craete a password

Password = []
for i in range(percentage1):
    Password.append(List1[i])
    Password.append(List2[i])

for i in range(percentage2):
    Password.append(List3[i])
    Password.append(List4[i])


# Shuffling the password

random.shuffle(Password)


# Convert the password from list to str

Password = "".join(Password[0:])


# Print the password

print(Password)
