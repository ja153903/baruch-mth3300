"""
Create a small program that receives a string `name` and two `float` numbers `monthly_salary` and `monthly_expenses` from the user.

Find out how much money this person has left and output the following: `<name> has $<remaining_amount> left for this month`.
"""

name = input("What is your name? ")

monthly_salary = input("How much do you earn per month? ")
monthly_salary = float(monthly_salary)

monthly_expenses = input("How much do you spend per month? ")
monthly_expenses = float(monthly_expenses)

print(f"{name} has ${monthly_salary - monthly_expenses} left for this month")
