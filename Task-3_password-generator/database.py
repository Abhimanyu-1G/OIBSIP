import json
import os
from cryptography.fernet import Fernet
import base64

class PasswordDatabase:
    def __init__(self, db_file="passwords.json", key_file="key.key"):
        self.db_file = db_file
        self.key_file = key_file
        self.key = self.load_key()
        self.cipher = Fernet(self.key)
        self.passwords = self.load_passwords()

    def load_key(self):
        if os.path.exists(self.key_file):
            with open(self.key_file, "rb") as f:
                return f.read()
        else:
            key = Fernet.generate_key()
            with open(self.key_file, "wb") as f:
                f.write(key)
            return key

    def load_passwords(self):
        if os.path.exists(self.db_file):
            with open(self.db_file, "r") as f:
                try:
                    encrypted_data = json.load(f)
                    decrypted_data = {}
                    for site, data in encrypted_data.items():
                        password = self.cipher.decrypt(base64.b64decode(data["password"])).decode()
                        decrypted_data[site] = {"password": password, "username": data.get("username")}
                    return decrypted_data
                except (json.JSONDecodeError, KeyError):
                    return {}
        return {}

    def save_passwords(self):
        encrypted_data = {}
        for site, data in self.passwords.items():
            encrypted_password = base64.b64encode(self.cipher.encrypt(data["password"].encode())).decode()
            encrypted_data[site] = {"password": encrypted_password, "username": data.get("username")}

        with open(self.db_file, "w") as f:
            json.dump(encrypted_data, f, indent=4)

    def add_password(self, site, password, username=None):
        self.passwords[site] = {"password": password, "username": username}
        self.save_passwords()

    def get_password(self, site):
        return self.passwords.get(site)

    def get_all_passwords(self):
        return self.passwords

    def delete_password(self, site):
        if site in self.passwords:
            del self.passwords[site]
            self.save_passwords()
