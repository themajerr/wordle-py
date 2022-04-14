import settings

class WordList:
    def __init__(self, expected_word_length):
        self.expected_word_length = expected_word_length
        self.create_wordlist(expected_word_length)

    def create_wordlist(self, expected_word_length):
        
        word_list_full = list(open('dictionary.txt').read().split('\n'))
        word_list_full.sort(reverse=True)

        self.word_list = []

        for word in word_list_full:
            if len(word) == expected_word_length:
                self.word_list.append(word)

    def open_wordlist(self):
        return self.word_list