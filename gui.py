from tkinter import *
from tkinter import messagebox
import wordle 
import wordlist
import correctanswer
import settings
import webbrowser

class Gui:
    def __init__(self):
        #self.current_settings = current_settings
        #self.wordlist = wordlist
        #self.correct_answer = correct_answer
        #self.single_game = single_game
        

        root = Tk()
        self.root = root
        root.title('Wordle: Igor Edition')
        root.iconbitmap('a.ico')

        self.guess_counter = 0
        self.current_settings = settings.Settings()
        self.wordlist = wordlist.WordList(int(self.current_settings.get_expected_word_length()))
        self.correct_answer = correctanswer.CorrectAnswer(self.wordlist.open_wordlist())
        self.single_game = wordle.Wordle(self.correct_answer.return_correct_answer())


        menu_bar = Menu(root)
        root.config(menu=menu_bar)

        file_menu = Menu(menu_bar, tearoff=False)
        file_menu.add_command(label='Settings', command=self.open_settings_window)
        menu_bar.add_cascade(label='File', menu=file_menu)

        help_menu = Menu(menu_bar, tearoff=False)
        help_menu.add_command(label='About', command=self.open_about_window)
        help_menu.add_separator()
        help_menu.add_command(label='Exit', command=root.destroy)
        menu_bar.add_cascade(label='Help', menu=help_menu)

        self.guess_entry = Entry(root, width=52, border=5, relief=SUNKEN)
        self.guess_entry.grid(column=0, row=7, columnspan=4, padx=5, pady=5)


        self.guess_button = Button(root, text='Guess!', command= lambda:self.is_word_in_dictionary(str(self.guess_entry.get())))
        self.guess_button.grid(column=4, row=7, padx=5, pady=5)


        self.status_indicator = Label(root, text=('Guess ' + str(self.guess_counter) + ' of ' + str(self.current_settings.get_max_number_of_guesses())), bd=1, relief=SUNKEN, anchor=E)
        self.status_indicator.grid(column=0, row=8, columnspan=5, sticky=W+E, padx=5, pady=5)


        root.mainloop()


    def is_word_in_dictionary(self, word):
        if word not in self.wordlist.open_wordlist():
            messagebox.showerror(title='Error!', message='This word is not in the dictionary!')
        else:
            self.single_guess(word)

        self.guess_entry.delete(0, END)

    def single_guess(self, word):

        self.check_with_answer(word)
        self.display_result(word)
        self.update_status_indicator()
        self.display_message_and_quit_if_won(word)
        self.display_message_and_quit_if_gameover()

    def check_with_answer(self, word):
        return self.single_game.word_check(word)

    def display_result(self, word):
        temporary_position = 0
            
        for char in word:
            
            temporary_color = ''
            if self.check_with_answer(word)[temporary_position] == wordle.Result.CORRECT_WORD_CORRECT_PLACE.value:
                temporary_color = '#569c38' #green
            elif self.check_with_answer(word)[temporary_position] == wordle.Result.CORRECT_WORD_INCORRECT_PLACE.value:
                temporary_color = '#d6c527' #yellow
            elif self.check_with_answer(word)[temporary_position] == wordle.Result.INCORRECT_WORD_INCORRECT_PLACE.value: 
                temporary_color = '#7d796b' #grey

            colorful_box = Label(self.root, text=word[temporary_position], bg=temporary_color, fg='white', width=10, height=5, font=('Helvetica', 10, 'bold'))
            colorful_box.grid(row=self.guess_counter, column=temporary_position)
            
            temporary_position+=1

    def update_status_indicator(self):
        global guess_counter
        self.guess_counter+=1
        self.status_indicator.config(text=('Guess ' + str(self.guess_counter) + ' of ' + str(self.current_settings.get_max_number_of_guesses())))
        
    def display_message_and_quit_if_won(self, word):
        if word == self.correct_answer.CORRECT_ANSWER:
            messagebox.showinfo(title="You won!", message='Congratulation! You have guessed the answer!')
            self.current_settings.reset_settings_to_default()
            self.root.quit()

    def display_message_and_quit_if_gameover(self):
        if self.guess_counter == int(self.current_settings.get_max_number_of_guesses()):
            messagebox.showerror(title='Game over!', message='Too bad! You have ran out of guesses!.\nCorrect answer is: ' + str(self.correct_answer.return_correct_answer()))
            self.current_settings.reset_settings_to_default
            self.root.quit()

    def open_settings_window(self):
        def save_current_settings():
            self.current_settings.dump_settings_into_file(word_length_setting_input.get(), max_guess_number_input.get())
            self.status_indicator.config(text=('Guess ' + str(self.guess_counter) + ' of ' + str(self.current_settings.get_max_number_of_guesses())))

        settings_window = Tk()
        settings_window.title('Settings')
        settings_window.iconbitmap('a.ico')

        word_length_setting_text = Label(settings_window, text='Words length (suggested - 4-8): ')
        word_length_setting_text.grid(column=0, row=0, columnspan=2, padx=5, pady=5)
        word_length_setting_input = Entry(settings_window, width=5)
        word_length_setting_input.grid(column=2, row=0, padx=5, pady=5)
    
        max_guess_number_text = Label(settings_window, text="How many guesses do you want to have?")
        max_guess_number_text.grid(column=0, row=1, columnspan=2, padx=5, pady=5)
        max_guess_number_input = Entry(settings_window, width=5)
        max_guess_number_input.grid(column=2, row=1, padx=5, pady=5)

        save_settings_button = Button(settings_window, text="Save", width=5, command=save_current_settings)
        save_settings_button.grid(row=2, column=0, columnspan=3, padx=5, pady=5)


        settings_window.mainloop

    def open_about_window(self):
        def open_website(url):
            webbrowser.open_new_tab(url)

        about_window = Tk()
        about_window.title('About')
        about_window.iconbitmap('a.ico')

        name_label = Label(about_window, text='Wordle!', fg='white', font=('Helvetica', 30, 'bold'), bg='grey', height=2, width=20, relief=RIDGE, border=10)
        name_label.grid(column=0, row=0, columnspan=4)

        written_by = Label(about_window, text='Written by Igor Majerczak', font=('Helvetica', 10), anchor=CENTER, padx=5, pady=5)
        written_by.grid(column=0, row=1, columnspan=2, sticky=E)

        written_by_link = Label(about_window, text='github.com/themajerr', font=('Helvetica', 10, 'underline'), fg='blue', cursor='hand2')
        written_by_link.bind('<Button-1>', lambda e: open_website('github.com/themajerr'))
        written_by_link.grid(column=2, row=1, columnspan=2, sticky=W)

        based_on_label = Label(about_window, text='Based on Wordle by Josh Wardle', font=('Helvetica', 10), anchor=CENTER, padx=5, pady=5)
        based_on_label.grid(column=0, row=2, columnspan=2, sticky=E)

        based_on_link = Label(about_window, text='nytimes.com/games/wordle', font=('Helvetica', 10, 'underline'), fg='blue', cursor='hand2')
        based_on_link.bind('<Button-1>', lambda e: open_website('nytimes.com/games/wordle'))
        based_on_link.grid(column=2, row=2, columnspan=2, sticky=W)
        
        resources_used = Label(about_window, text='RESOURCES USED', font=('Helvetica', 9, 'bold'), anchor=CENTER, padx=5, pady=5)
        resources_used.grid(row=3, column=0, columnspan=4)

        icon_link = Label(about_window, text='Icon: freewordle.org/images/wordle-game-icon-512.png', font=('Helvetica', 10, 'underline'), fg='blue', cursor='hand2', pady=3)
        icon_link.bind('<Button-1>', lambda e: open_website('freewordle.org/images/wordle-game-icon-512.png'))
        icon_link.grid(row=4, column=0, columnspan=4, sticky=W+E)

        dictionary_link = Label(about_window, text='Dictionary: github.com/dwyl/english-words', font=('Helvetica', 10, 'underline'), fg='blue', cursor='hand2', pady=3)
        dictionary_link.bind('<Button-1>', lambda e: open_website('github.com/dwyl/english-words'))
        dictionary_link.grid(row=5, column=0, columnspan=4, sticky=W+E) 
        about_window.mainloop

    
