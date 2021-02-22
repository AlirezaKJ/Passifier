import random

characters = "abcdefghijklmnopqrsqrstuvwxyz"
numbers = 1234567890
symbols = "!@#$%^&*"

print('''
Passifier
Running On Version: 1.0
Developed By github.com/AlirezaKJ/
''')

while True:
    question = input("Do You Want Uppercase Alphabets In Your Password? ")
    if question.lower() == "yes":
        characters = characters + characters.upper()
    question = input("Do You Want Numbers In Your Password? ")
    if question.lower() == "yes":
        characters = characters + str(numbers)
    question = input("Do You Want Special Symbols(!@#$%^&*) In Your Password? ")
    if question.lower() == "yes":
        characters = characters + symbols
    password__length = int(input("Enter Your Password Lenght : "))
    password__count = int(input("How Many Password Do You Want : "))
    print("")
    print("")
    for x in range(0,password__count):
        password = ""
        for x in range(0,password__length):
            password_x = random.choice(characters)
            password = password + password_x
        print(password)
        print("")
    print('')
    question = input("Do You Want Another Password? ")
    if question.lower() == "yes":
        pass
    else:
        exit()
