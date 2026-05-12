import secrets
import string
import json
import os
from datetime import datetime


def main():
    result = password()
    print(f"Stored: {result}")


def password():

    user_name = input("Insert your user: ")
    web_site = input("Insert the website: ")

    chars: str = string.ascii_letters + string.digits + string.punctuation
    length = 12

    while True:

        password: str = ''.join(secrets.choice(chars) for _ in range(length))

        has_letter = False
        has_number = False
        has_special = False
        
        is_unique = len(set(password)) == len(password)

        for c in password:
            if c in string.ascii_letters:
                has_letter = True
            elif c in string.digits:
                has_number = True
            elif c in string.punctuation:
                has_special = True

        if has_letter and has_number and has_special and is_unique:
            print(
                f"Success! User: {user_name}, Website: {web_site}"
            )
            return password

        print("Generated password did not meet criteria, retrying...")


def save_to_json():
    ...
    date = {}


if __name__ == "__main__":
    main()
