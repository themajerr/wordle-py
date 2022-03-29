from tkinter import *
from tkinter import messagebox
import random


def split(word):
    return[char for char in word]

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
    guess_check()

def guess_check():
    global guess_counter 
    guess_counter+=1
    temp = 0
    while temp < 5:
        for char in word_guess_listform:

            if char == correct_anwser_list[temp]:
                letter_box = Label(root, text=word_guess_listform[temp], bg='#67e84a', fg='white', width=10, height=5)
                letter_box.grid(column=temp, row=guess_counter)

                temp+=1
                continue

            if char in correct_anwser_list:
                letter_box = Label(root, text=word_guess_listform[temp], bg='#ffd036', fg='white', width=10, height=5)
                letter_box.grid(column=temp, row=guess_counter)

                temp+=1
                continue

            if char not in correct_anwser_list:
                letter_box = Label(root, text=word_guess_listform[temp], bg='#7d796b', fg='white', width=10, height=5)
                letter_box.grid(column=temp, row=guess_counter)

                temp+=1
                continue

    update_status_indicator()
    if guess_counter == 6:
        gameover()
            

    

#def guess_counter_change():
#    guess_counter.set(guess_counter.get()+1)

    #if guess_counter.get() == 6:
    #    gameover()

def gameover():
    
    #print('this is the end')
    messagebox.showinfo(title='Koniec gry!', message='Niestety! Skończyły Ci się próby.\nPoprawna odpowiedź to: ' + str(correct_anwser))
    root.quit()
def update_status_indicator():

    global guess_counter 
    print(guess_counter)
    status_indicator = Label(root, text='Próba ' + str(guess_counter) + ' z 6  ', bd=1, relief=SUNKEN, anchor=E)
    status_indicator.grid(column=0, row=8, columnspan=6, sticky=W+E, padx=5, pady=5)
root = Tk()

root.title('Wordle: Igor Edition')
root.iconbitmap('a.ico')

word_guess = StringVar(root)
word_list = []
#guess_counter = IntVar(root, 1)
global guess_counter 
guess_counter = 0

#cały słownik, zmienne i zawartość
word_dictionary_txt_temp = open('lista.txt').read().split('\n')
word_dictionary = list()
for word in word_dictionary_txt_temp:
    if len(word) == 5:
        word_dictionary.append(word)

correct_anwser = random.choice(word_dictionary)
correct_anwser_list = split(correct_anwser)
print(correct_anwser_list)



guess_entry = Entry(root, width=40, border=5, relief=SUNKEN)
guess_entry.grid(column=0, row=7, columnspan=4, padx=5, pady=5)

guess_button = Button(root, text='Guess!', command= entry_to_word)
guess_button.grid(column=4, row=7, padx=5, pady=5)

status_indicator = Label(root, text='Próba 1 z 6  ', bd=1, relief=SUNKEN, anchor=E)
status_indicator.grid(column=0, row=8, columnspan=5, sticky=W+E, padx=5, pady=5)









root.mainloop()