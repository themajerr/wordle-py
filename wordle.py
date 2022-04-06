from enum import Enum, auto

def split(word):
        return[char for char in word]
        
class Wordle:
    
    # Enum creation
    class Result(Enum):
        CORRECT_WORD_CORRECT_PLACE = 1
        CORRECT_WORD_INCORRECT_PLACE = 2
        INCORRECT_WORD_INCORRECT_PLACE = 3

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
        return  guess_check_results

    

    