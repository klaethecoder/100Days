import random as r
#Day 4 Randomisation and Python Lists
# Project: Rock, Paper, Scissors game

print("Welcome to the Thunder Dome!!!")
print("This is a game of Rock Paper Scissors")
p1_choice = input("Choose R for Rock, S for Scissors and P for Paper\t")
comp_choice = r.random_choice(["R", "S", "P"])

if p1_choice == comp_choice:
    print("It's a Tie")
elif p1_choice == "R" and comp_choice == "S":
    print("You Win!!!")
elif p1_choice == "S" and comp_choice == "P":
    print("You Win")
elif p1_choice == "P" and comp_choice == "R":
    print("You Win")
else:
    print("Computer Wins :( ")



count = 0
list = []
while set(list) != {0,1,2}:
    num = r.randint(0,2)
    print(num)
    count += 1
    list.append(num)

print(f"That took {count} iterations")

# Day 4.1 Exercise: Heads or Tails

#Write your code below this line 👇
#Hint: Remember to import the random module first. 🎲

num = random.randint(0,1)
if num ==1:
  print("It's Heads")
else:
  print("It's Tails")


# Day 4.2 Exercise: Who is buying lunch?
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
import random as r

length = len(names)
index = r.randint(0, length-1)

print(f"Looks like {names[index]} is getting the bill today")


# Day 4.3 Exercise: Treasure Map?

# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
col = int(position[0]) - 1
row = int(position[1])-1

map[row][col] = "X"

#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")