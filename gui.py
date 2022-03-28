from tkinter import *
from tkinter import messagebox
import random


def split(word):
    return[char for char in word]

def get_a_word_from_dictionary():
    correct_anwser = random.choice(word_dictionary)

def entry_to_word():
    if guess_entry.get() not in word_dictionary:
        messagebox.showerror('Błąd!', 'Słowo nie znajduje się w słowniku!')
        guess_entry.delete(0, END)
         

    word_guess.set(guess_entry.get())
    temp = word_guess.get()
    global word_guess_listform
    word_guess_listform = split(temp)

    #OSTATECZNIE TO NIE TUTAJ | ZOSTAWIAM DO DEBUGOWANIA
    #print(word_list)
    #guess_print = Label(root, text=word_list)
    #guess_print.grid(column=0, row=guess_counter.get())

    #guess_counter_change()
    #update_status_indicator()
def guess_check():
    temp = 0
    for char in word_guess_listform:
        if char == word_guess_listform[temp]:
            temp+=1
        if char in word_guess_listform:
            temp+=1
        if char not in word_guess_listform:
            temp+=1
    
    guess_counter_change
    
def guess_counter_change():
    guess_counter.set(guess_counter.get()+1)
    if guess_counter.get() == 6:
        gameover()

def gameover():
    return

def update_status_indicator():
    status_indicator = Label(root, text='Próba ' + str(guess_counter.get()) + ' z 6  ', bd=1, relief=SUNKEN, anchor=E)
    status_indicator.grid(column=0, row=8, columnspan=6, sticky=W+E, padx=5, pady=5)
root = Tk()
root.title('Wordle: Igor Edition')
root.iconbitmap('a.ico')

word_guess = StringVar(root)
word_list = []
guess_counter = IntVar(root, 1)

#cały słownik, zmienne i zawartość
word_dictionary_txt_temp = open('lista.txt').read().split('\n')
word_dictionary = list()
for word in word_dictionary_txt_temp:
    if len(word) == 5:
        word_dictionary.append(word)

guess_entry = Entry(root, width=40, border=5, relief=SUNKEN)
guess_entry.grid(column=0, row=7, columnspan=4, padx=5, pady=5)

guess_button = Button(root, text='Guess!', command= entry_to_word)
guess_button.grid(column=5, row=7, padx=5, pady=5)

status_indicator = Label(root, text='Próba 1 z 6  ', bd=1, relief=SUNKEN, anchor=E)
status_indicator.grid(column=0, row=8, columnspan=6, sticky=W+E, padx=5, pady=5)









root.mainloop()