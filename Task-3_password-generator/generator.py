
import random
import string

class PasswordGenerator:
    def __init__(self):
        self.words = [
            "apple", "banana", "cherry", "dog", "elephant", "frog", "grape",
            "horse", "ice", "jelly", "kite", "lemon", "monkey", "noodle",
            "orange", "penguin", "queen", "robot", "snake", "tiger", "unicorn",
            "violin", "whale", "xylophone", "yacht", "zebra"
        ]

    def generate(self, length, use_upper, use_lower, use_digits, use_symbols):
        chars = ""
        if use_upper:
            chars += string.ascii_uppercase
        if use_lower:
            chars += string.ascii_lowercase
        if use_digits:
            chars += string.digits
        if use_symbols:
            chars += string.punctuation

        if not chars:
            return "Error: Select at least one character type"

        password = ''.join(random.choice(chars) for _ in range(length))
        return password

    def generate_memorable(self, num_words=4, separator="-"):
        password_words = random.sample(self.words, num_words)
        return separator.join(password_words)

    def check_strength(self, password):
        length = len(password)
        has_upper = any(c.isupper() for c in password)
        has_lower = any(c.islower() for c in password)
        has_digit = any(c.isdigit() for c in password)
        has_symbol = any(c in string.punctuation for c in password)
        
        score = 0
        if length >= 12:
            score += 2
        elif length >= 8:
            score += 1

        if has_upper:
            score += 1
        if has_lower:
            score += 1
        if has_digit:
            score += 1
        if has_symbol:
            score += 1
        
        if score >= 6:
            return "Strong", "#89b4fa"
        elif score >= 4:
            return "Good", "#a6e3a1"
        elif score >= 2:
            return "Okay", "#fab387"
        else:
            return "Weak", "#f38ba8"
