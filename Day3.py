 # coding=utf-8 
# Day 3 Project

treasure_image = '''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
'''

print(treasure_image)
print("Your Mission is to find the Treasure.")
direction = input("You're at a cross road. Where do you want to go? Type 'left' or 'right'\t")
if direction == 'left':
    action = input("You come to a lake. There is an island in the middle of the lake.Type 'wait' to wait for a boat or 'swim' to swim across.\t")
    if action == 'wait':
        color = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which color do you choose?\t")
        if color == 'yellow':
            print("You Win!!!")
        elif color == 'blue':
            print("Eaten by beasts.\nGame Over!")
        elif color == 'red':
            print("Burned by fire.\nGame Over!")
        else:
            print("Game Over!")
    else:
        print("Attacked by trout.\nGame Over!")
else:
    print("Fall into a hole.\nGame Over!")

bill = 0

print("Welcome to the Rollercoaster!")
height = int(input("What is your height in cm?\t"))

if height > 120:
   
    print("You can ride the Rollercoaster")
    age= int(input("What is your age?\t"))
    if age >=45 and age <= 55:
        print("Sorry about the Mid-Life Crisis, your ticket is free")
        bill += 0
    elif age >18:
        print("Adult tickets cost $12")
        bill += 12
    elif age >12 and age <= 18:
        print("Youth tickets cost $7")
        bill += 7
    else:
        print("Child tickets cost $5")
        bill += 5
    photos = input("Do you want a photo taken? Y or N\t")
    if photos == "Y":
        bill += 3
    print(f"Your final bill is ${bill}")
else:
    print("Sorry, you have to grow taller before you can ride.")


# Excercise 3.1 Write program that checks to see if a number is Even or Odd

number = int(input("Give me a number from 1-100\t"))

if number%2 ==0:
    print("This is an Even Number")
else:
    print("This is an Odd Number")

# Excercise 3.2 Write program that checks to see where you are in the BMI
# ???? Don't change the code below ????
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# ???? Don't change the code above ????

#Write your code below this line ????
bmi = weight// (height**2)

if int(bmi) >= 35:
    print(f"Your BMI is {bmi} and you are clinically obese.")
elif int(bmi) >= 30 and int(bmi) < 35:
    print(f"Your BMI is {bmi} and you are obese.")
elif int(bmi) >= 25 and int(bmi)< 30:
    print(f"Your BMI is {bmi} and you are overweight.")
elif bmi >= 18.5 and int(bmi) < 25:
    print(f"Your BMI is {bmi} and you are normal weight.")
else:
    print(f"Your BMI is {bmi} and you are underweight.")

# Excercise 3.3 Write program that checks to see if year is a leap year
year = int(input("Which year do you want to check?\t"))

if year % 4 == 0 and year % 100 != 0:
   print(f"{year} is a Leap year")
elif year % 400 == 0:
  print(f"{year} is a Leap year")       
else:
    print(f"{year} is not a Leap year")

# Excercise 3.4 Write program that helps with ordering pizza
# ???? Don't change the code below ????
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# ???? Don't change the code above ????

#Write your code below this line ????
bill = 0
if size.upper() == "S":
  print("Small Pizza costs $15")
  bill +=15
elif size.upper() == "M":
  print("Medium Pizza costs $20")
  bill +=20
else:
  print("Large Pizza costs $25")
  bill +=25
if add_pepperoni.upper() == "Y" and size =="S":
  print("Adding Pepperoni on a Small Pizza costs $2")
  bill += 2
elif add_pepperoni.upper() == "Y":
  print("Adding Pepperoni on a Medium or Large Pizza costs $3")
  bill += 3
if extra_cheese.upper() == "Y":
  print("Adding Extra Cheese to a Pizza costs $1")
  bill += 1

print(f"The total comes to: ${bill}")

# Excercise 3.5 Write program that helps with ordering pizza
# ???? Don't change the code below ????
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# ???? Don't change the code above ????

#Write your code below this line ????
key = {"t":0,
"r":0,
"u":0,
"e":0,
"l":0,
"o":0,
"v":0
}

def checkLetterForLove(letter):
  t=r=u=e=l=o=v=0
  true_count = 0
  love_count = 0
  if letter.upper() == "T":
    true_count+= 1
    key["t"]+=1 
  elif letter.upper() == "R":
    true_count+= 1
    key["r"]+=1 
  elif letter.upper() == "U":
    true_count+= 1
    key["u"]+=1 
  elif letter.upper() == "E":
    true_count+= 1
    love_count+=1 
    key["e"]+=2
  elif letter.upper() == "L":
    love_count+= 1
    key["l"]+=1 
  elif letter.upper() == "O":
    love_count+= 1
    key["o"]+=1 
  elif letter.upper() == "V":
    love_count+= 1
    key["v"]+=1
  
  return true_count*10 + love_count

def checkNamesForLove(name1,name2):
  true_love_score = 0
  for letter in name1:
    true_love_score += checkLetterForLove(letter)

  for letter in name2:
    true_love_score +=checkLetterForLove(letter)

  print(f"T occurs {key['t']} times.")
  print(f"R occurs {key['r']} times.")
  print(f"U occurs {key['u']} times.")
  print(f"E occurs {key['e']} times.")
  
  print(f"L occurs {key['l']} times.")
  print(f"O occurs {key['o']} times.")
  print(f"V occurs {key['v']} times.")
  print(f"E occurs {key['e']} times.")
  if true_love_score < 10:
      print(f"Your score is {true_love_score}, you go together like Coke and Mentos.")
  elif true_love_score >= 40 and true_love_score <= 50:
      print(f"Your score is {true_love_score}, you are alright together.")
  else:
      print(f"Your love score is {true_love_score}")


checkNamesForLove(name1, name2)

