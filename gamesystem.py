import random
from enum import Enum


class Wordle:
    def split(word):
        return[char for char in word]

    guess_counter = 0
    max_number_of_guesses = 6
    expected_word_length = 5
    is_win = False
    is_gameover = False
    # Dictionary creation
    word_dictionary_txt_temp = open('lista.txt').read().split('\n')
    word_dictionary = list()

    for word in word_dictionary_txt_temp:
        if len(word) == expected_word_length:
            word_dictionary.append(word)
    
    # Random word selection for answer

    correct_answer = random.choice(word_dictionary)
    correct_answer_list = split(correct_answer)
    print(correct_answer)
    
    def __new__(self, passed_word):
        # setup for new word
        entered_word = self.split(passed_word)
        char_position = 0
        guess_check_results = []

        # Enum creation
        class Result(Enum):
            CORRECT_WORD_CORRECT_PLACE = 1
            CORRECT_WORD_INCORRECT_PLACE = 2
            INCORRECT_WORD_INCORRECT_PLACE = 3

        # validation mechanism
                 
        for char in entered_word:
            if char == self.correct_answer_list[char_position]:
                guess_check_results.append(Result.CORRECT_WORD_CORRECT_PLACE.value)
                        
            elif char in self.correct_answer_list:
                guess_check_results.append(Result.CORRECT_WORD_INCORRECT_PLACE.value)
                        
            else:    
                guess_check_results.append(Result.INCORRECT_WORD_INCORRECT_PLACE.value)                 
                        
            char_position+=1

        self.guess_counter+=1   
        
        if entered_word == self.correct_answer_list:
            self.is_win = True 

        print(guess_check_results)
        result = guess_check_results

        if self.guess_counter == self.max_number_of_guesses:
            self.is_gameover = True
            
        
        return result

    

    