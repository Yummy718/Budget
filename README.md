# Budgeting Helper Application
README.txt

PROJECT NAME
------------
Budgeting Helper Application


PROJECT DESCRIPTION
-------------------
The Budgeting Helper Application is a Python-based program designed to
help users understand how their money flows over the course of a week.
It calculates the total cost of items a user wants to buy, checks whether
the user is within their budget, tracks leftover money, and applies a
weekly allowance on a specified day.

This project focuses on calculation logic rather than user interface,
making it easy to reuse in different environments such as command-line
programs, graphical applications, or games.


FEATURES
--------
- Calculates the total cost of each item (price × quantity)
- Calculates the subtotal of all items
- Applies tax to the subtotal
- Determines whether total spending is within budget
- Calculates remaining money or budget deficit
- Determines the current day of the week
- Adds a weekly allowance on the correct day
- Carries leftover money forward to the next week
- Keeps items in chronological order of purchase


REQUIREMENTS
------------
- Python 3.8 or newer
- No external libraries required
- Uses Python standard library only (datetime)

Optional:
- Git (for version control)
- VS Code or another Python editor


FILES INCLUDED
--------------
- budget_helper.py
  Contains all calculation logic and helper functions.

- README.txt
  Project documentation and setup instructions.


HOW THE PROGRAM WORKS (LOGIC OVERVIEW)
-------------------------------------
1. The program determines the current day of the week.
2. If today matches the user’s allowance day, the weekly allowance is
   added to the budget.
3. Each item’s total price is calculated using price × quantity.
4. All item totals are summed to get a subtotal.
5. Tax is calculated and added to the subtotal.
6. The total cost is compared to the budget.
7. Remaining money is calculated.
8. Any positive remaining money is carried over to the next week.
9. Items are stored in the order they were purchased.


DATA STRUCTURE EXAMPLES
-----------------------

Items are stored as a list of dictionaries:

items = [
    {
        "name": "Groceries",
        "price": 10.50,
        "quantity": 2,
        "day": "Monday"
    }
]

Budget-related values:

budget = 200.0
weekly_allowance = 50.0
allowance_day = "Monday"
tax_rate = 0.07


HOW TO RUN
----------
1. Make sure Python 3 is installed:
   python --version

2. Place all project files in the same folder.

3. Run the main Python file:
   python budget_helper.py

Note:
This project contains calculation logic only. Input and output can be
added separately if needed.


LIMITATIONS
-----------
- No graphical interface
- No persistent storage (data resets each run)
- Assumes valid data types are provided


POSSIBLE FUTURE IMPROVEMENTS
----------------------------
- Add user input handling
- Add error checking and validation
- Save transaction history to a file
- Add daily spending tracking
- Create a graphical interface (e.g., pygame or Tkinter)
- Convert into a mobile or web application


VERSION CONTROL
---------------
This project is designed to be used with Git and GitHub.
Recommended workflow:
- Commit changes frequently
- Use clear commit messages
- Push to GitHub regularly


AUTHOR
------
Student Project
Budgeting Helper Application


LICENSE
-------
This project is for educational purposes only.
