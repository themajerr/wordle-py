from threading import get_ident
from tkinter import *
from tkinter import messagebox
import gamesystem

global guess_counter
guess_counter = 0

def whole_guess_operation():

    #entry to word + dictionary check -> pass word to gamesystem
    global guess_counter

    entered_word = guess_entry.get()
    entered_word_letters = entered_word
    if entered_word not in gamesystem.Wordle.word_dictionary:
        messagebox.showerror(title='Error!', message='This word is not in the dictionary!')
        guess_entry.delete(0, END)

    else:
        entered_word = gamesystem.Wordle(entered_word)
        guess_entry.delete(0, END)

    # visual answer generation
    
    temporary_position = 0
    
    for char in entered_word:
       
        temporary_color = ''
        if entered_word[temporary_position] == gamesystem.Wordle.Result.CORRECT_WORD_CORRECT_PLACE.value:
            temporary_color = '#569c38' #green
        elif entered_word[temporary_position] == gamesystem.Wordle.Result.CORRECT_WORD_INCORRECT_PLACE.value:
            temporary_color = '#d6c527' #yellow
        elif entered_word[temporary_position] == gamesystem.Wordle.Result.INCORRECT_WORD_INCORRECT_PLACE.value: 
            temporary_color = '#7d796b' #grey
        
        print(temporary_color)
        colorful_box = Label(root, text=entered_word_letters[temporary_position], bg=temporary_color, fg='white', width=10, height=5, font=('Helvetica', 10, 'bold'))
        colorful_box.grid(row=guess_counter, column=temporary_position)
        
        temporary_position+=1
        
    
    #update guess indicator
    
    guess_counter+=1
    status_indicator = Label(root, text='Guess ' + str(guess_counter) + ' of 6  ', bd=1, relief=SUNKEN, anchor=E)
    status_indicator.grid(column=0, row=8, columnspan=6, sticky=W + E, padx=5, pady=5)

    # check if the word was correct
    # komentarz żebym nie zapomniał, dlatego po januszowemu; jeżeli program ma otrzymać wyłącznie info [dobrze, dobrze, średnio] itd to on technicznie nie zna odpowiedzi więc to jest mocno na trytytce xd
    if entered_word == [gamesystem.Wordle.Result.CORRECT_WORD_CORRECT_PLACE.value, 
                        gamesystem.Wordle.Result.CORRECT_WORD_CORRECT_PLACE.value, 
                        gamesystem.Wordle.Result.CORRECT_WORD_CORRECT_PLACE.value, 
                        gamesystem.Wordle.Result.CORRECT_WORD_CORRECT_PLACE.value, 
                        gamesystem.Wordle.Result.CORRECT_WORD_CORRECT_PLACE.value]:
        messagebox.showinfo(title="You won!", message='Congratulation! You have guessed the answer!')
        root.quit()

    # check for gameover
    # also komentarz - tutaj też teoretycznie nie zna poprawnej odpowiedzi xd
    if guess_counter == max_number_of_guesses:
        messagebox.showerror(title='Game over!', message='Too bad! You have ran out of guesses!.\nCorrect answer is: ' + str(gamesystem.Wordle.correct_answer))
        root.quit()

# GUI frame + starting elements
root = Tk()
root.title('Wordle: Igor Edition')
root.iconbitmap('a.ico')

# variables
#guess_counter = 0
max_number_of_guesses = 6

# interface
guess_entry = Entry(root, width=52, border=5, relief=SUNKEN)
guess_entry.grid(column=0, row=7, columnspan=4, padx=5, pady=5)


guess_button = Button(root, text='Guess!', command=whole_guess_operation)
guess_button.grid(column=4, row=7, padx=5, pady=5)

status_indicator = Label(root, text='Guess 0 of 6  ', bd=1, relief=SUNKEN, anchor=E)
status_indicator.grid(column=0, row=8, columnspan=5, sticky=W+E, padx=5, pady=5)


root.mainloop()

