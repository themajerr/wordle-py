import json

class Settings:
    def __init__(self):
        self.load_settings_from_file()

    def dump_settings_into_file(self, expected_word_length, max_number_of_guesses):
        with open("settings.json") as f:
            data = json.load(f)
            if expected_word_length != '': data["expected_word_length"] = expected_word_length
            if max_number_of_guesses != '': data["max_number_of_guesses"] = max_number_of_guesses
            json.dump(data, open("settings.json", "w"), indent = 4)

        self.load_settings_from_file

    def load_settings_from_file(self):
        settings = open('settings.json')
        settings = json.load(settings)
        self.max_number_of_guesses = settings['max_number_of_guesses']
        self.expected_word_length = settings['expected_word_length']

    def reset_settings_to_default(self):
        with open("settings.json") as f:
            data = json.load(f)
            data["expected_word_length"] = 5
            data["max_number_of_guesses"] = 6
            json.dump(data, open("settings.json", "w"), indent = 4)

    def get_expected_word_length(self):
        return self.expected_word_length
    
    def get_max_number_of_guesses(self):
        return self.max_number_of_guesses
