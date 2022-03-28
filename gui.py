from tkinter import *
from tkinter import messagebox


def split(word):
    return[char for char in word]

def entry_to_word():
    if guess_entry.get() not in word_dictionary:
        messagebox.showerror('Błąd!', 'Słowo nie znajduje się w słowniku!')
        guess_entry.delete(0, END)
         

    word_guess.set(guess_entry.get())
    temp = word_guess.get()
    word_list = split(temp)

    #OSTATECZNIE TO NIE TUTAJ | ZOSTAWIAM DO DEBUGOWANIA
    #print(word_list)
    #guess_print = Label(root, text=word_list)
    #guess_print.grid(column=0, row=lp.get())

    lp_change()
    update_status_indicator()

def lp_change():
    lp.set(lp.get()+1)
    if lp.get() == 6:
        gameover()

def gameover():
    return

def update_status_indicator():
    status_indicator = Label(root, text='Próba ' + str(lp.get()) + ' z 6  ', bd=1, relief=SUNKEN, anchor=E)
    status_indicator.grid(column=0, row=8, columnspan=6, sticky=W+E, padx=5, pady=5)
root = Tk()
root.title('Wordle: Igor Edition')
root.iconbitmap('a.ico')
word_guess = StringVar(root)
word_list = []
lp = IntVar(root, 1)

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