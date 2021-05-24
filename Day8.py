# Day 8 Project: Ceasar Cipher

logo = '''

'''


def encodeCipher(message, cipher):
    newMessage = []
    newWord = []
    for letter in message:
        newMessage.append(ord(letter) + cipher)
    for num in newMessage:
        newWord.append(chr(num))
    return "".join(newWord)


def decodeCipher(message, cipher):
    newMessage = []
    newWord = []
    for letter in message:
        newMessage.append(ord(letter) - cipher)
    for num in newMessage:
        newWord.append(chr(num))
    return "".join(newWord)


result = ''
initial_choice = input(
    "Type 'encode' to encrypt and write 'decode' to decrypt\n")
cipher = int(input("Type the shift number\n"))
if initial_choice == 'encode':
    message = input("Type your message\n")
    result = encodeCipher(message, cipher)
elif initial_choice == 'decode':
    message = input("Type message you needed decoded.\n")
    result = decodeCipher(message, cipher)


print(f"Here is the encoded messsage: {result}")
