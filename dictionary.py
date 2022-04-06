expected_word_length = 5
word_dictionary = []
word_dictionary_full = list(open('lista.txt').read().split('\n'))
#print(word_dictionary_full) #change to log

for word in word_dictionary_full:
    if len(word) == expected_word_length:
        word_dictionary.append(word)

#print(word_dictionary) #change to log






#class Dictionary:
#    def split(word):
#        return[char for char in word]

#    def __new__(self):

#        expected_word_length = 5 #add to settings
#        # Dictionary creation
#        word_dictionary_txt_temp = open('lista.txt').read().split('\n')
#        global word_dictionary
#        word_dictionary = list()

#        for word in word_dictionary_txt_temp:
#            if len(word) == expected_word_length:
#                word_dictionary.append(word)
#
         # Random word selection for answer
#        return word_dictionary