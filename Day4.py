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
