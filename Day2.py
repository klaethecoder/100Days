import math

# Day 2 Project
print("Welcome to the tip calculator")
total_bill = float(input("What was the total bill?\t"))
total_people = float(input("How many people to split the bill?\t"))
tip_percent = float(input("What percentage tip would you like to give 10, 12, or 15?\t"))/100

result = (total_bill + (total_bill*tip_percent)) / total_people

print(round(result,2))


# Coding Exercise Day 2.1 
# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇
d1 = two_digit_number[0]
d2 = two_digit_number[1]

print(int(d1)+int(d2))


# Day 2.2 Exercise: BMI Calculator
# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
print(type(height))

print(round(float(weight)/(float(height)**2),2))

# Day 2.3 Exercise: Time Left 

# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
age = int(age)
years_left = 90-age
weeks_left = years_left*52
months_left = years_left*12
days_left = weeks_left*7


print(f"Based on living to 90 Years Old: You have {days_left} days left, {weeks_left} weeks left, and {months_left} months left. ")

