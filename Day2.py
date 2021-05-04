import math

# Day 2 Project
print("Welcome to the tip calculator")
total_bill = float(input("What was the total bill?\t"))
total_people = float(input("How many people to split the bill?\t"))
tip_percent = float(input("What percentage tip would you like to give 10, 12, or 15?\t"))/100

result = (total_bill + (total_bill*tip_percent)) / total_people

print(round(result,2))

