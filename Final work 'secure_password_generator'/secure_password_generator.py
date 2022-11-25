import random

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
chars = ''

def is_digit(num):
    if num.isdigit():
        return True
    else:
        return False

def generate_password(length, chars):
    password = ''
    for _ in range(length):
        password += random.choice(chars)
    return password 

print("This is a Secure Password Generator")
print("Let's start generating passwords")

flag = False
while flag == False:
    cntPw = input('Specify the number of passwords to generate: ')
    if is_digit(cntPw):
        flag = True
    else:
        print("You didn't enter a number! Try again!")

flag = False
while flag == False:
    lenPw = input('Specify the length of one password: ')
    if is_digit(lenPw):
        flag = True
    else:
        print("You didn't enter a number! Try again!")

flag = False
while flag == False:
    digOn = input('Should the numbers 0123456789 be included? (y/n): ')
    if (digOn.lower() != 'y' and digOn.lower() != 'n'):
            print("Whoa, wrong answer! Onle 'Y' or 'N'! Try again!")
            flag = False
    else:
        flag = True

flag = False
while flag == False:
    ABCon = input('Should uppercase be included?  (y/n): ')
    if (ABCon.lower() != 'y' and ABCon.lower() != 'n'):
            print("Whoa, wrong answer! Onle 'Y' or 'N'! Try again!")
            flag = False
    else:
        flag = True

flag = False
while flag == False:
    abcOn = input('Should lowercase be included?  (y/n): ')
    if (abcOn.lower() != 'y' and abcOn.lower() != 'n'):
            print("Whoa, wrong answer! Onle 'Y' or 'N'! Try again!")
            flag = False
    else:
        flag = True

flag = False
while flag == False:
    chOn = input('Should symbols (!#$%&*+-=?@^_) be included? (y/n): ')
    if (chOn.lower() != 'y' and chOn.lower() != 'n'):
            print("Whoa, wrong answer! Onle 'Y' or 'N'! Try again!")
            flag = False
    else:
        flag = True

flag = False
while flag == False:
    excOn = input('Should il1Lo0O ambiguous characters be excluded? (y/n): ')
    if (excOn.lower() != 'y' and excOn.lower() != 'n'):
            print("Whoa, wrong answer! Onle 'Y' or 'N'! Try again!")
            flag = False
    else:
        flag = True

if digOn.lower() == 'y':
    chars += digits
if abcOn.lower() == 'y':
    chars += lowercase_letters
if ABCon.lower() == 'y':
    chars += uppercase_letters
if chOn.lower() == 'y':
    chars += punctuation
if excOn.lower() == 'y':
    for c in 'il1Lo0O':
        chars = chars.replace(c,'')

password_list = []
for _ in range(int(cntPw)):
    password_list.append(generate_password(int(lenPw), chars))
print("Your password is:")
print(*password_list, sep="\n")