from random import *

phrases = ['Undoubtedly', "It's a foregone conclusion", "Without any doubts",
                        'Definitely yes', 'You can be sure of it', 'I think so', "Most likely", "Good prospects",
                        'The signs say yes', 'Yes' ,'I think so', "Most likely", "Good prospects",
                        'The signs say yes', 'Yes','Do not even think', "My answer is no", "According to my information, no",
                        "Prospects are not very good", 'Highly doubtful']

print('Hello World, I am a magic ball and I know the answer to any of your questions.')
print("Tell me your name! I want to know!")
name = input("And your name is: ")
print("Oooo, wonderful! Hello, ", name,"!", sep="")
flag = False
while flag == False:
    question = input("Tell me your qustion: ")
    print("Ok, I understand... \n think... \n think...\n think...")
    print("And your answer is: ")
    print(choice(phrases))
    print("Do you want to submit another question? Please, say 'Yes' or 'No' ")
    print("I'm waiting...")
    answer = input("Answer is: ")
    if (answer.lower() != 'yes' and answer.lower() != 'no'):
        print("Whoa, wrong answer! Onle 'Yes' or 'No'! Try again!")
        flag = False
    elif answer.lower() == 'no':
        print("Ok! I understand! Se la vie! Come back if you have any questions!")
        flag = True
        break
    else:
        print("I'm listing")