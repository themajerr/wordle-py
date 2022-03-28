from tkinter import *

def split(word):
    return[char for char in word]

def entry_to_word():
    
    word_guess.set(guess_entry.get())
    temp = word_guess.get()
    word_list = split(temp)

    print(word_list)
    guess_print = Label(root, text=word_list)
    guess_print.grid(column=0, row=lp.get())
    lp_change()
    print(lp.get())
    lp_change

def lp_change():
    lp.set(lp.get()+1)

root = Tk()
word_guess = StringVar(root)
word_list = []
lp = IntVar(root, 1)

guess_entry = Entry(root, width=40, border=5, relief=SUNKEN)
guess_entry.grid(column=0, row=7, columnspan=4, padx=5, pady=5)

guess_button = Button(root, text='Guess!', command= entry_to_word)
guess_button.grid(column=5, row=7, padx=5, pady=5)











root.mainloop()