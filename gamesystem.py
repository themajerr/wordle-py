import random


class Wordle:
    def __init__(self, guess_entry, word_guess_listform, word_dictionary, max_number_of_guesses, correct_answer_list, guess_counter, guess_check_results, entered_word, is_gameover, is_win):
        self.guess_entry = guess_entry
        self.word_guess_listform = word_guess_listform
        self.word_dictionary = word_dictionary
        self.max_number_of_guesses = max_number_of_guesses
        self.correct_answer_list = correct_answer_list
        self.guess_counter = guess_counter
        self.guess_check_results = guess_check_results
        self.entered_word = entered_word
        self.is_gameover = is_gameover
        self.is_win = is_win


    def split(word):
        return[char for char in word]          

    # dictionary creation + assigning random word as correct anwser
    is_win = False
    is_gameover = False
    guess_counter = 0
    max_number_of_guesses = 6 
    expected_word_length = 5
    word_dictionary_txt_temp = open('lista.txt').read().split('\n')
    word_dictionary = list()

    for word in word_dictionary_txt_temp:
        if len(word) == expected_word_length:
            word_dictionary.append(word)

    correct_answer = random.choice(word_dictionary)
    correct_answer_list = split(correct_answer)
    print(correct_answer)

    def guess_check(entered_word):
        
        # word to list
        print(entered_word)
        Wordle.entered_word = list(Wordle.split(entered_word))
        print(Wordle.entered_word)
        #guess_counter+=1
        print(Wordle.guess_counter)
        
        # mechanism itself

        char_position = 0
        Wordle.guess_check_results = []
                 
        for char in Wordle.entered_word:
            if char == Wordle.correct_answer_list[char_position]:
                Wordle.guess_check_results.append('CorrectLetter_CorrectPlace')
                    
            elif char in Wordle.correct_answer_list:
                Wordle.guess_check_results.append('CorrectLetter_IncorrectPlace')
                    
            else:    
                Wordle.guess_check_results.append('IncorrectLetter_IncorrectPlace')                 
                    
            char_position+=1
                
        print(Wordle.guess_check_results)
        Wordle.guess_counter+=1    

        # win check

        if Wordle.entered_word == Wordle.correct_answer_list:
            Wordle.is_win = True

        # gameover check

        if Wordle.guess_counter == Wordle.max_number_of_guesses:
            Wordle.is_gameover = True           
        

    