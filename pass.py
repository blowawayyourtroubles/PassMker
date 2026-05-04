import secrets
import string
import json
import os
from datetime import datetime

def contraseña():

    user_name = input("Insert your user: ")
    web_site = input("Insert the website: ")

    password = "pXPm2Bi0Pc6jEQlL!"

    lenght_ok = len(password) > 8

    has_letter = False
    has_number = False
    has_special = False


    for char in password:
        if char.isalpha():
            has_letter = True
        elif char.isdigit():
            has_number = True
        elif not char.isalnum():
            has_special = True

    if lenght_ok and has_letter and has_number and has_special:
        return f"Your user is {user_name}, website is {web_site}, and your password is {password}."
    else:
        print("Wrong password input.")


resultado = contraseña()
print(resultado)
