import random
from enum import Enum, auto

class Dictionary:
    
    global split
    def split(word):
        return[char for char in word]

    def __new__(self):
        expected_word_length = 5
        # Dictionary creation
        word_dictionary_txt_temp = open('lista.txt').read().split('\n')
        global word_dictionary
        word_dictionary = list()

        for word in word_dictionary_txt_temp:
            if len(word) == expected_word_length:
                word_dictionary.append(word)

         # Random word selection for answer
        return word_dictionary
        
class Correct_answer:
    def __new__(self):
        temporary_dictionary = Dictionary()
        correct_answer = random.choice(temporary_dictionary)
        print(correct_answer)
        return correct_answer
        
class Wordle:
    
    # Enum creation
    class Result(Enum):
        CORRECT_WORD_CORRECT_PLACE = auto()
        CORRECT_WORD_INCORRECT_PLACE = auto()
        INCORRECT_WORD_INCORRECT_PLACE = auto()

    # validation part
    
    def __new__(self, passed_word, correct_word):
        # setup for new word
        entered_word = split(passed_word)
        correct_word = split(correct_word)
        char_position = 0
        guess_check_results = []
        
        # validation mechanism
                 
        for char in entered_word:
            if char == correct_word[char_position]:
                guess_check_results.append(self.Result.CORRECT_WORD_CORRECT_PLACE.value)
                        
            elif char in correct_word:
                guess_check_results.append(self.Result.CORRECT_WORD_INCORRECT_PLACE.value)
                        
            else:    
                guess_check_results.append(self.Result.INCORRECT_WORD_INCORRECT_PLACE.value)                 
                        
            char_position+=1

        print(guess_check_results)
        result = guess_check_results

        return result

    

    