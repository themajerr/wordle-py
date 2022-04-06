class Dictionary:
    def split(word):
        return[char for char in word]

    def __new__(self):
        expected_word_length = 5 #add to settings
        # Dictionary creation
        word_dictionary_txt_temp = open('lista.txt').read().split('\n')
        global word_dictionary
        word_dictionary = list()

        for word in word_dictionary_txt_temp:
            if len(word) == expected_word_length:
                word_dictionary.append(word)

         # Random word selection for answer
        return word_dictionary