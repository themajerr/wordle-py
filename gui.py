from tkinter import *
from tkinter import messagebox
import wordle 
import dictionary
import correct_answer
import settings

def is_word_in_dictionary(word):
    if word not in dictionary.word_list:
        messagebox.showerror(title='Error!', message='This word is not in the dictionary!')
    else:
        single_guess(word)

    guess_entry.delete(0, END)

def single_guess(word):

    check_with_answer(word)
    display_result(word)
    update_status_indicator()
    display_message_and_quit_if_won(word)
    display_message_and_quit_if_gameover()

def check_with_answer(word):
    return single_game.word_check(word)

def display_result(word):
    temporary_position = 0
        
    for char in word:
        
        temporary_color = ''
        if check_with_answer(word)[temporary_position] == wordle.Result.CORRECT_WORD_CORRECT_PLACE.value:
            temporary_color = '#569c38' #green
        elif check_with_answer(word)[temporary_position] == wordle.Result.CORRECT_WORD_INCORRECT_PLACE.value:
            temporary_color = '#d6c527' #yellow
        elif check_with_answer(word)[temporary_position] == wordle.Result.INCORRECT_WORD_INCORRECT_PLACE.value: 
            temporary_color = '#7d796b' #grey

        colorful_box = Label(root, text=word[temporary_position], bg=temporary_color, fg='white', width=10, height=5, font=('Helvetica', 10, 'bold'))
        colorful_box.grid(row=guess_counter, column=temporary_position)
          
        temporary_position+=1

def update_status_indicator():
    global guess_counter
    guess_counter+=1
    guess_indicator_text.set('Guess ' + str(guess_counter) + ' of 6  ')

def display_message_and_quit_if_won(word):
    if word == correct_answer.CORRECT_ANSWER:
        messagebox.showinfo(title="You won!", message='Congratulation! You have guessed the answer!')
        root.quit()

def display_message_and_quit_if_gameover():
    if guess_counter == MAX_NUMBER_OF_GUESSES:
        messagebox.showerror(title='Game over!', message='Too bad! You have ran out of guesses!.\nCorrect answer is: ' + str(correct_answer.CORRECT_ANSWER))
        root.quit()

root = Tk()
root.title('Wordle: Igor Edition')
root.iconbitmap('a.ico')

guess_counter = 0
MAX_NUMBER_OF_GUESSES = settings.settings["max_number_of_guesses"]

single_game = wordle.Wordle(correct_answer.CORRECT_ANSWER)

guess_entry = Entry(root, width=52, border=5, relief=SUNKEN)
guess_entry.grid(column=0, row=7, columnspan=4, padx=5, pady=5)


guess_button = Button(root, text='Guess!', command=lambda: is_word_in_dictionary(guess_entry.get()))
guess_button.grid(column=4, row=7, padx=5, pady=5)

guess_indicator_text = StringVar()
guess_indicator_text.set('Guess ' + str(guess_counter) + ' of 6  ')
status_indicator = Label(root, textvariable= guess_indicator_text, bd=1, relief=SUNKEN, anchor=E)
status_indicator.grid(column=0, row=8, columnspan=5, sticky=W+E, padx=5, pady=5)


root.mainloop()

