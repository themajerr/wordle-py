from tkinter import *
from tkinter import messagebox
import gamesystem

def whole_guess_operation():

    #entry to word + dictionary check -> pass word to gamesystem
    
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
        if entered_word[temporary_position] == 1:
            temporary_color = '#569c38' #green
        elif entered_word[temporary_position] == 2:
            temporary_color = '#d6c527' #yellow
        elif entered_word[temporary_position] == 3: 
            temporary_color = '#7d796b' #grey
        
        print(temporary_color)
        colorful_box = Label(root, text=entered_word_letters[temporary_position], bg=temporary_color, fg='white', width=10, height=5, font=('Helvetica', 10, 'bold'))
        colorful_box.grid(row=gamesystem.Wordle.guess_counter, column=temporary_position)
        temporary_position+=1

    #update guess indicator
        
    status_indicator = Label(root, text='Guess ' + str(gamesystem.Wordle.guess_counter) + ' of 6  ', bd=1, relief=SUNKEN, anchor=E)
    status_indicator.grid(column=0, row=8, columnspan=6, sticky=W + E, padx=5, pady=5)

    # check if the word was correct
    if gamesystem.Wordle.is_win:
        messagebox.showinfo(title="You won!", message='Congratulation! You have guessed the answer!')
        root.quit()

    # check for gameover
    if gamesystem.Wordle.is_gameover:
        messagebox.showerror(title='Game over!', message='Too bad! You have ran out of guesses!.\nCorrect answer is: ' + str(gamesystem.Wordle.correct_answer))
        root.quit()

# GUI frame + starting elements
root = Tk()
root.title('Wordle: Igor Edition')
root.iconbitmap('a.ico')

guess_entry = Entry(root, width=52, border=5, relief=SUNKEN)
guess_entry.grid(column=0, row=7, columnspan=4, padx=5, pady=5)


guess_button = Button(root, text='Guess!', command=whole_guess_operation)
guess_button.grid(column=4, row=7, padx=5, pady=5)

status_indicator = Label(root, text='Guess 0 of 6  ', bd=1, relief=SUNKEN, anchor=E)
status_indicator.grid(column=0, row=8, columnspan=5, sticky=W+E, padx=5, pady=5)


root.mainloop()

