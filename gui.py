from tkinter import *
from tkinter import messagebox
import wordle 
import dictionary
import correct_answer


def is_word_in_dictionary(word):
    if word not in dictionary.word_dictionary:
        messagebox.showerror(title='Error!', message='This word is not in the dictionary!')
    else:
        single_guess(word)

    guess_entry.delete(0, END)

def single_guess(word):

    def check_with_answer():
        return single_game.word_check(word)

    def display_result():
        temporary_position = 0
        
        for char in word:
        
            temporary_color = ''
            if check_with_answer()[temporary_position] == wordle.Result.CORRECT_WORD_CORRECT_PLACE.value:
                temporary_color = '#569c38' #green
            elif check_with_answer()[temporary_position] == wordle.Result.CORRECT_WORD_INCORRECT_PLACE.value:
                temporary_color = '#d6c527' #yellow
            elif check_with_answer()[temporary_position] == wordle.Result.INCORRECT_WORD_INCORRECT_PLACE.value: 
                temporary_color = '#7d796b' #grey
            
            print(temporary_color)
            colorful_box = Label(root, text=word[temporary_position], bg=temporary_color, fg='white', width=10, height=5, font=('Helvetica', 10, 'bold'))
            colorful_box.grid(row=guess_counter, column=temporary_position)
            
            temporary_position+=1
            
        #print(entered_word)

    def update_status_indicator():
        global guess_counter
        guess_counter+=1
        status_indicator = Label(root, text='Guess ' + str(guess_counter) + ' of 6  ', bd=1, relief=SUNKEN, anchor=E)
        status_indicator.grid(column=0, row=8, columnspan=6, sticky=W + E, padx=5, pady=5)

    def is_win():
        if word == correct_answer.selected_correct_answer:
            messagebox.showinfo(title="You won!", message='Congratulation! You have guessed the answer!')
            root.quit()

    def is_gameover():
        if guess_counter == max_number_of_guesses:
            messagebox.showerror(title='Game over!', message='Too bad! You have ran out of guesses!.\nCorrect answer is: ' + str(correct_answer.selected_correct_answer))
            root.quit()

    check_with_answer()
    display_result()
    update_status_indicator()
    is_win()
    is_gameover()
    
root = Tk()
root.title('Wordle: Igor Edition')
root.iconbitmap('a.ico')

guess_counter = 0
max_number_of_guesses = 6

single_game = wordle.Wordle(correct_answer.selected_correct_answer)

guess_entry = Entry(root, width=52, border=5, relief=SUNKEN)
guess_entry.grid(column=0, row=7, columnspan=4, padx=5, pady=5)


guess_button = Button(root, text='Guess!', command=lambda: is_word_in_dictionary(guess_entry.get()))
guess_button.grid(column=4, row=7, padx=5, pady=5)

status_indicator = Label(root, text='Guess 0 of 6  ', bd=1, relief=SUNKEN, anchor=E)
status_indicator.grid(column=0, row=8, columnspan=5, sticky=W+E, padx=5, pady=5)


root.mainloop()

