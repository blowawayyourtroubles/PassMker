# PssMker

### Definition

A minimal command-line password manager written in Python. Generates cryptographically secure passwords and stores them locally in a JSON file.

### Features

Generates secure 12-character passwords using letters, numbers, and special characters
Guarantees no repeated characters in any generated password
Stores credentials locally in passwords.json
Detects duplicate entries (same username + website) and prompts before overwriting
No external dependencies — standard library only

### Usage

#### The program will prompt you for:

Username or email — the account identifier
Website or app — where the password will be used

A password is then generated automatically and saved to passwords.json in the same directory.
If an entry with the same username and website already exists, you will be asked whether you want to replace it.

## Storage
Credentials are saved locally in a passwords.json file with the following structure:

```json
[
    {
        "username": "example@email.com",
        "website": "github.com",
        "password": "aB3$kL9!mZ2@",
        "created_at": "2026-05-12"
    }
]
```
