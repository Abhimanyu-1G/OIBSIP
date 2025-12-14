# BMI Calculator

This project is a desktop application created as part of my internship at **Oasis Infobyte**.

## Description

This desktop application, built with Python, allows users to calculate their Body Mass Index (BMI). It features a user-friendly graphical interface to input height and weight, view the calculated BMI, and track their historical data. The history is also visualized with a graphical plot.

## Features

*   Calculate BMI based on height (in cm) and weight (in kg).
*   User management to track BMI for different people.
*   View historical BMI records in a table.
*   Visualize BMI history with a Matplotlib chart.
*   Clear history for a selected user.
*   A clean and modern user interface.

## Technologies Used

*   **Core:** Python
*   **GUI:** PyQt6
*   **Data Storage:** SQLite
*   **Data Visualization:** Matplotlib

## Setup and Usage

1.  **Navigate to the project directory:**
    ```bash
    cd Task-2_bmi-calculator
    ```
2.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Run the application:**
    ```bash
    python main.py
    ```

## Folder Structure

```
Task-2_bmi-calculator/
├── bmi_calculator/
│   ├── database.py
│   ├── logic.py
│   └── ui/
│       ├── custom_widgets.py
│       ├── history_widget.py
│       ├── input_widget.py
│       └── main_window.py
├── bmi_data.db
├── main.py
├── requirements.txt
├── styles.qss
└── README.md
```

## Author

[Abhimanyu Singh Chouhan]
