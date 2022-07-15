import random

class CorrectAnswer:
    def __init__(self, wordlist):
        self.wordlist = wordlist
        self.set_correct_answer()
        

    def set_correct_answer(self):
        self.CORRECT_ANSWER = random.choice(self.wordlist)
<<<<<<< HEAD
        print(self.CORRECT_ANSWER)

    def return_correct_answer(self):
=======
        
    def get_correct_answer(self):
>>>>>>> e554c60... Bug fix - game over stats now adding correctly
        return self.CORRECT_ANSWER
