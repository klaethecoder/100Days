import random as r
import string as s
# Day 5 Project: Password Generators

print("Welcome to PyPassword Generator")
length = int(input("How many letters do you want in your password?\n"))
symbols = int(input("How many symbols do you want in your password?\n"))
numbers = int(input("How many numbers do you want in your password?\n"))
password = ""
arr = []

def loopity(choices,amount):
    for thing in range(amount):
        arr.append(r.choice(choices))


loopity(s.ascii_letters,length)
loopity(s.digits,numbers)
loopity(s.punctuation,symbols)

print(arr)
r.shuffle(arr)

print(password.join(arr))

