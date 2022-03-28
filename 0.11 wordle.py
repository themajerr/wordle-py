import random
from termcolor import colored


def split(word):
    return [char for char in word]


guess_counter = 0
words = open("lista.txt").read().split('\n')
mylist = list()

for word in words:

    if len(word) == 5:
        mylist.append(word)

word_anwser = random.choice(mylist)
# print(word_anwser)

word_letters = split(word_anwser)
# print(colored(word_letters, 'blue'))
while guess_counter < 5:
    word_guess = input('\n')

    if word_guess.isdigit():
        print("Słowo nie może zawierać cyfr!")
        continue

    if len(word_guess) != 5:
        print('Słowo musi zawierać 5 liter!')
        continue

    if word_guess not in mylist:
        print('To nie jest poprawne słowo!')
        continue

    if word_guess == word_anwser:
        print(colored(word_guess, 'green'))
        print('Gratulacje! Wygrałeś!')
        break

    word_guess_temp = split(word_guess)
    temp = 0

    for char in word_guess_temp:

        if char == word_anwser[temp]:
            print(colored(char, 'green'), end=' ')
            temp += 1
            continue

        if char in word_anwser:
            print(colored(char, 'yellow'), end=' ')
            temp += 1
            continue

        print(colored(char, 'red'), end=' ')
        temp += 1
        continue

    guess_counter += 1

    if guess_counter == 5:
        print('Niestety! Koniec prób. Poprawna odpowiedź to:', word_anwser)
        break
