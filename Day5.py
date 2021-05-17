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

# Day 5.1 Exercise: Average Height

# 🚨 Don't change the code below 👇
student_heights = [180, 124, 165, 173, 189, 169, 146]

for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
totalHeights = 0
list_length = 0
for height in student_heights:
    totalHeights += height
    list_length += 1 

total = totalHeights/list_length
print(round(total))

# Day 5.2 Exercise: Highest score in class

# 🚨 Don't change the code below 👇
# student_scores = input("Input a list of student scores ").split()
# student_scores = [78, 65, 89, 86, 55, 91, 64, 89]
student_scores = [r.randrange(1, 100, 1) for i in range(5,r.randint(6,10))]
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
current_high_score = 0

for score in student_scores:
  if score > current_high_score: 
    current_high_score = score
 
print(f"The highest score in this list is: {current_high_score}")


# Day 5.3 Exercise: Sum of Even Numbers to 100

#Write your code below this row 👇
total_even = 0
for num in range(1,101):
  if num %2 == 0:
    total_even += num

print(total_even)


# Day 5.4 Exercise: FizzBuzz

#Write your code below this row 👇
for num in range(1,101):
  if num %3 == 0 and num%5==0:
    print("FizzBuzz")
  elif num %5 ==0:
    print("Buzz")
  elif num %3 ==0:
    print("Fizz")
  else:
    print(num)

