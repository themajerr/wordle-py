import random
import dictionary

class Correct_answer:
    def __new__(self):
        temporary_dictionary = dictionary.Dictionary()
        correct_answer = random.choice(temporary_dictionary)
        print(correct_answer)
        return correct_answer