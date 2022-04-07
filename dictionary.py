expected_word_length = 5
word_dictionary = []
word_dictionary_full = list(open('lista.txt').read().split('\n'))
word_dictionary_full.sort(reverse=True)
for word in word_dictionary_full:
    if len(word) == expected_word_length:
        word_dictionary.append(word)
