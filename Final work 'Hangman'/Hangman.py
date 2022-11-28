import random

word_list = ['money', 'career', 'java', 'python','developer','college']

def get_word():
    secret_word = random.choice(word_list)
    return secret_word

def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
                # голова, торс, обе руки, одна нога
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
                # голова, торс, обе руки
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
                # голова, торс и одна рука
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
                # голова и торс
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
                # голова
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                # начальное состояние
                '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]
    return stages[tries]

def print_word(word_, list_):
    for c in word_:
        if c in list_:
            print(c, end=' ')
        else:
            print('_', end=' ')
    print()

def play(word):
    # function body
    word_completion = '_' * len(word)  # строка, содержащая символы _ на каждую букву задуманного слова
    guessed = False                    # сигнальная метка
    guessed_letters = []               # список уже названных букв
    guessed_words = []                 # список уже названных слов
    tries = 6                          # количество попыток
    
    print("Let's play Hangman game!")
    print("Remember: 6 mistakes - and you\'ll find yourself hanging on the gallows.")
    print(display_hangman(tries))

    print("|", word_completion,"|")

    while True:
        word_input = input('Enter letter or word: ').upper()
        # print(word_input)
        if not word_input.isalpha():
            print("You didn't enter a letter or a word! Try again!")
            continue
        if word_input in guessed_words or word_input in guessed_letters:
            print('You have already entered this letters or words')
            continue
        if len(word_input) > 1:
            if word_input == word:
                print('Congratulations, you guessed the word! You won!')
                break
            else:
                guessed_words.append(word_input)
                tries -= 1
                print('Wrong, attempts left ', tries)
                print(display_hangman(tries))
                print_word(word, guessed_letters)
                if tries == 0:
                    print("You failed to guess the word: ", word)
                    break
                continue
        if len(word_input) == 1:
            if word_input in word:
                guessed_letters.append(word_input)
                for c in word:
                    if c not in guessed_letters:
                        print('Guessed the letter')
                        print_word(word, guessed_letters)
                        guessed = False
                        break
                    guessed = True
                if guessed:    
                    print_word(word, guessed_letters)
                    print('Congratulations, you guessed the word! You won!')
                    break
            else:
                guessed_letters.append(word_input)
                tries -= 1
                print('Wrong, attempts left ', tries)
                print(display_hangman(tries))
                print_word(word, guessed_letters)
            if tries == 0:
                print("You failed to guess the word: ", word)
                break

play(get_word().upper())