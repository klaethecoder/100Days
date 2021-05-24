import string as s
# Day 8 Project: Ceasar Cipher

logo = logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
done = True

def encodeCipher(message, cipher):
    newMessage = []
    newWord = []
    for char in message:
        if char not in s.ascii_letters:
             newMessage.append(ord(char))
        else:
            newMessage.append(ord(char) + cipher)
    for num in newMessage:
        newWord.append(chr(num))
    return "".join(newWord)


def decodeCipher(message, cipher):
    newMessage = []
    newWord = []
    for char in message:
        if char in s.ascii_letters:
         newMessage.append(ord(char) - cipher)
        else:
           newMessage.append(ord(char)) 
    for num in newMessage:
        newWord.append(chr(num))
    return "".join(newWord)

print(logo)
while done:
    result = ''
    initial_choice = input(
        "Type 'encode' to encrypt and write 'decode' to decrypt\n").lower()
    cipher = int(input("Type the shift number\n"))
    if initial_choice == 'encode':
        message = input("Type your message\n")
        result = encodeCipher(message, cipher)
    elif initial_choice == 'decode':
        message = input("Type message you needed decoded.\n")
        result = decodeCipher(message, cipher)

    print(f"Here is the encoded messsage: {result}")
    answer = input("Would you like to contiue with the Caeser Cipher?\tyes or no\n").lower()
    if answer == "no":
        done = False


# Day 8.1 Excercise 
# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

def greet():
  print("Hello World!")
  print("It is me again")
  print("Alrgith I am out :)")

# multiple argument functions

def greet_with_stuff(name, location):
    print(f"Hello {name}")
    print(f"How is the weather in {location}")

#Write your code below this line 👇
def paint_calc(height, width, cover):
  print(round((height*width) / cover))

#Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.   

# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)

# Day 8.2 Excercise: Prime Number Checker

#Write your code below this line 👇
def prime_checker(number):

  for num in range(2,number):
    if number%num ==0:
      return print("It's not a prime number.")
    else:
      continue
  print("It's a prime number.")

#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
