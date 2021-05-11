import random as r
#Day 4 Randomisation and Python Lists
# Project: Rock, Paper, Scissors game

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

