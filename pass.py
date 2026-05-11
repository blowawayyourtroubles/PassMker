import secrets
import string
import json
import os
from datetime import datetime


def main():
    result = password()
    print(result)


def password():

    user_name = input("Insert your user: ")
    web_site = input("Insert the website: ")

    while True:
        password = input("Insert your password: ")

        lenght_ok = len(password) >= 8
        has_letter = False
        has_number = False
        has_special = False

        for c in password:
            if c in string.ascii_letters:
                has_letter = True
            elif c in string.digits:
                has_number = True
            elif c in string.punctuation:
                has_special = True

        if lenght_ok and has_letter and has_number and has_special and  len(set(password)) == len(password):
            print(f"Your user is {user_name}, website is {web_site}, and your password is {password}")
        print("Wrong password input, try again.")

if __name__ == "__main__":
    main()
