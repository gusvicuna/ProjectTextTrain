from .Classes.Aception import Aception
from .Classes.MatchData import MatchData

def MatchTrainText(staticAception=Aception, movingAception=Aception):
    
    matches_data = []
    
    train_index = 0
    while train_index < 3 * movingAception.charCount:
        char_match_count = 0
        word_match_count = 0
        word_match = True
        
        char_index = 0
        while char_index < staticAception.charCount:
            moving_aception_index = movingAception.charCount - train_index + char_index
            if moving_aception_index < 0 or moving_aception_index >= movingAception.charCount:
                moving_char_evaluator = ""
            else:
                moving_char_evaluator = movingAception.characters[moving_aception_index]
            
            if staticAception.characters[char_index] == " " or char_index == len(staticAception.characters) - 1:
                if word_match:
                    word_match_count += 1
                word_match = True

            if staticAception.characters[char_index] == moving_char_evaluator and moving_char_evaluator != "":
                char_match_count += 1
            else:
                word_match = False
            
            char_index += 1
        
        match_data = MatchData(staticAception.wordCount, word_match_count, staticAception.charCount, char_match_count)
        matches_data.append(match_data)
        
        train_index += 1
    return matches_data