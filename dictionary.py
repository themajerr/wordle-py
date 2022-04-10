import settings

EXPECTED_WORD_LENGTH = settings.settings["expected_word_length"]
word_list_full = list(open('lista.txt').read().split('\n'))
word_list_full.sort(reverse=True)

word_list = []

for word in word_list_full:
    if len(word) == EXPECTED_WORD_LENGTH:
        word_list.append(word)
