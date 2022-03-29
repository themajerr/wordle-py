from tkinter import *
from tkinter import messagebox
import random

def split(word):
    return[char for char in word]

def entry_to_word():
    if guess_entry.get() not in word_dictionary:
        messagebox.showerror(title='Błąd!', message='Słowo nie znajduje się w słowniku!')
        guess_entry.delete(0, END)
        
    if guess_entry.get() in word_dictionary:    

        word_guess.set(guess_entry.get())
        temp = word_guess.get()
        global word_guess_listform
        word_guess_listform = split(temp)

        guess_check()

def guess_check():
    global guess_counter 
    guess_counter+=1
    temp = 0
    
    while temp < 5:
        for char in word_guess_listform:

            if char == correct_anwser_list[temp]:
                letter_box = Label(root, text=word_guess_listform[temp].upper(), bg='#569c38', fg='white', width=10, height=5, font=('Helvetica', 10, 'bold'))
                letter_box.grid(column=temp, row=guess_counter)

                temp+=1
                continue

            if char in correct_anwser_list:
                letter_box = Label(root, text=word_guess_listform[temp].upper(), bg='#d6c527', fg='white', width=10, height=5, font=('Helvetica', 10, 'bold'))
                letter_box.grid(column=temp, row=guess_counter)

                temp+=1
                continue

            if char not in correct_anwser_list:
                letter_box = Label(root, text=word_guess_listform[temp].upper(), bg='#7d796b', fg='white', width=10, height=5, font=('Helvetica', 10, 'bold'))
                letter_box.grid(column=temp, row=guess_counter)

                temp+=1
                continue
    if word_guess_listform == correct_anwser_list:
        messagebox.showinfo(title="Wygrałeś!", message='Gratulacje! Odgadłeś słowo!')
        root.quit()

    update_status_indicator()
    if guess_counter == 6:
        gameover()
            
    guess_entry.delete(0, END)
def gameover():
    messagebox.showinfo(title='Koniec gry!', message='Niestety! Skończyły Ci się próby.\nPoprawna odpowiedź to: ' + str(correct_anwser))
    root.quit()

def update_status_indicator():
    global guess_counter 
    #print(guess_counter)
    status_indicator = Label(root, text='Próba ' + str(guess_counter) + ' z 6  ', bd=1, relief=SUNKEN, anchor=E)
    status_indicator.grid(column=0, row=8, columnspan=6, sticky=W+E, padx=5, pady=5)


root = Tk()

root.title('Wordle: Igor Edition')
root.iconbitmap('a.ico')

word_guess = StringVar(root)
word_list = []

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
#print(correct_anwser_list)



guess_entry = Entry(root, width=40, border=5, relief=SUNKEN)
guess_entry.grid(column=0, row=7, columnspan=4, padx=5, pady=5)

guess_button = Button(root, text='Guess!', command= entry_to_word)
guess_button.grid(column=4, row=7, padx=5, pady=5)

status_indicator = Label(root, text='Próba 1 z 6  ', bd=1, relief=SUNKEN, anchor=E)
status_indicator.grid(column=0, row=8, columnspan=5, sticky=W+E, padx=5, pady=5)



root.mainloop()