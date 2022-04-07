from enum import Enum
from correct_answer import *

class Result(Enum):
            CORRECT_WORD_CORRECT_PLACE = 1
            CORRECT_WORD_INCORRECT_PLACE = 2
            INCORRECT_WORD_INCORRECT_PLACE = 3

class Wordle:
    def __init__(self, correct_answer):
        self.correct_answer = correct_answer

    def word_check(self, passed_word):
        #passed_word = split(passed_word)
        char_position = 0
        guess_check_results = []

        for char in passed_word:
            if char == self.correct_answer[char_position]:
                guess_check_results.append(Result.CORRECT_WORD_CORRECT_PLACE.value)
                            
            elif char in self.correct_answer:
                guess_check_results.append(Result.CORRECT_WORD_INCORRECT_PLACE.value)
                            
            else:    
                guess_check_results.append(Result.INCORRECT_WORD_INCORRECT_PLACE.value)                 
                            
            char_position+=1

        #print(guess_check_results)
        return guess_check_results


    