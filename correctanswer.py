import random

class CorrectAnswer:
    def __init__(self, wordlist):
        self.wordlist = wordlist
        self.set_correct_answer()
        

    def set_correct_answer(self):
        self.CORRECT_ANSWER = random.choice(self.wordlist)
        
    def get_correct_answer(self):
        return self.CORRECT_ANSWER
