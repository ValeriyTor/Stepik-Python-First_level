from random import *

phrases_too_much = ['Oh, too much! Try again', 'Too much!', "Whoa, that's too much!",
                        'A lot!', 'Take it lower', 'Too much!', 'Need a smaller number!']
phrases_too_little = ['Oh, too little! Try again', "It won't be enough!", "Oh, it's too little!",
                        'Not enough!', 'Take it higher', 'Not enough!', 'Need more!']
phrases_guessed = ['Congratulations! You guessed my number :)', 'Well done! You guessed it :)', 'Hooray, you guessed it! :)']

def is_digit(num):
    if num.isdigit():
        return True
    else:
        return False

counter = 0
flag = False
print("Hello, my friend! Do yoy want to play with me?")
print("Please, say 'Yes' or 'No'")
print("I'm waiting...")
answer = input("Answer is: ")
while flag == False:
    if (answer.lower() != 'yes' and answer.lower() != 'no'):
        print("Whoa, wrong answer! Onle 'Yes' or 'No'! Try again!")
        flag = False
    elif answer.lower() == 'no':
        print("Bad day! Ok! I understand! Se la vie!")
        flag = True
        break
    else:
        print("Wonderful choiсe! \n Let's start, but first of all you must choose upper bound! \n Please, tell me it:")
        n = input("Upper bound is: ")
        while True:
            if is_digit(str(n)):
                n = int(n)
                break
            else:
                print("You didn't enter a number! Try again!")
                n = input("Upper bound is: ")
        secret_number = randint(1, n)
        flag1 = False
        print("I guessed a number from 0 to", n, "\nTry to guess!")
        while flag1 == False:
            my_number = input("Enter a number: ")
            if is_digit(str(my_number)):
                my_number = int(my_number)  
                if my_number > secret_number:
                    print(phrases_too_much[randint(0,len(phrases_too_much)-1)])
                    print("Try again!")
                    counter += 1
                    flag1 = False
                elif my_number < secret_number:
                    print(phrases_too_little[randint(0,len(phrases_too_little)-1)])
                    print("Try again!")
                    counter += 1
                    flag1 = False
                else:
                    print(phrases_guessed[randint(0,len(phrases_guessed)-1)])
                    print("You used", counter, "tries")
                    flag1 = True
            else:
                print("You didn't enter a number! Try again!")
    print("-------------------------", "\nDo you want to play again?!")
    print("Please, say 'Yes' or 'No'")
    answer = input("Answer is: ")

