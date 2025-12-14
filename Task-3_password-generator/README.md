# Password Generator

This project is a desktop utility created as part of my internship at **Oasis Infobyte**.

## Description

A desktop application that generates strong, customizable passwords to enhance security. The user can specify the password length and choose to include different character sets (uppercase, lowercase, numbers, symbols). The generated password can be easily copied to the clipboard, and the application also features the ability to securely save the passwords.

## Features

*   Generate strong, random passwords of a user-defined length.
*   Option to include uppercase letters, lowercase letters, numbers, and symbols.
*   Copy the generated password to the clipboard with a single click.
*   Securely save generated passwords for future reference.
*   View saved passwords.
*   User-friendly and intuitive interface.

## Technologies Used

*   **Core:** Python
*   **GUI:** PyQt6
*   **Security:** `cryptography` library for encryption
*   **Clipboard:** `pyperclip` library

## Setup and Usage

1.  **Navigate to the project directory:**
    ```bash
    cd Task-3_password-generator
    ```
2.  **Install the dependencies:**
    ```bash
    pip install -r reqirement.txt
    ```
3.  **Run the application:**
    ```bash
    python main.py
    ```

## Folder Structure

```
Task-3_password-generator/
├── database.py
├── generator.py
├── gui.py
├── main.py
├── passwords_window.py
├── reqirement.txt
├── styles.py
├── test_generator.py
└── README.md
```

## Author

[Abhimanyu Singh Chouhan]
