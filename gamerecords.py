import json

class Gamerecords:
    def __init__(self):
        self.game_records = open('statistics.json')
        self.game_records = json.load(self.game_records)
        
    def add_game_report_to_statistics(self, word, guess_counter, max_number_of_guesses):
            
            with open('statistics.json', 'r+') as f:
                current_records = json.load(f)
                               
                new_game_record = {}
                new_game_record[word] = [word, guess_counter, max_number_of_guesses]
                

                current_records['game_statistics'].update(new_game_record)

                f.seek(0)
                x = json.dump(current_records, f, indent=4)
             
                
    
    def output_statistics(self):
        return self.game_records

       