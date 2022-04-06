from enum import Enum, auto
from correct_answer import *


def split(word):
        return[char for char in word]
class Result(Enum):
            CORRECT_WORD_CORRECT_PLACE = 1
            CORRECT_WORD_INCORRECT_PLACE = 2
            INCORRECT_WORD_INCORRECT_PLACE = 3

class Wordle:
    
    # wywołanie ma wyglądać Wordle.check(słowo)
    # single object of Wordle class contains one run of the game - one correct answer and word checking mechanism  
    def __init__(self, correct_answer):
        self.correct_answer = correct_answer

    #print(correct_answer)
    #def __new__(self):
    #    Wordle.correct_answer = list(selected_correct_answer)

    def word_check(self, passed_word):
        passed_word = split(passed_word)
        #correct_answer = list(selected_correct_answer)
        char_position = 0
        guess_check_results = []

        

    # validation mechanism
                 
        for char in passed_word:
            if char == self.correct_answer[char_position]:
                guess_check_results.append(Result.CORRECT_WORD_CORRECT_PLACE.value)
                            
            elif char in self.correct_answer:
                guess_check_results.append(Result.CORRECT_WORD_INCORRECT_PLACE.value)
                            
            else:    
                guess_check_results.append(Result.INCORRECT_WORD_INCORRECT_PLACE.value)                 
                            
            char_position+=1

        print(guess_check_results)
        return guess_check_results


    