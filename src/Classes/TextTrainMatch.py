from src.Classes.Aception import Aception
from src.Classes.MatchData import MatchData


class TrainTextMatch:

    listOfMatchData = []

    def __init__(self, trainText=Aception, movingAception=Aception) -> None:
        self.trainText = trainText
        self.movingAception = movingAception
        self.listOfMatchData = self.MatchTrainText()

    def MatchTrainText(self):
        list_of_match_data = []

        train_id = 0
        while train_id < self.movingAception.charCount + self.trainText.charCount:
            char_match_count = 0
            word_match_count = 0
            word_match = True

            char_id = 0
            while char_id < self.trainText.charCount:

                moving_aception_id = self.movingAception.charCount - train_id + char_id
                if moving_aception_id < 0 or moving_aception_id >= self.movingAception.charCount:
                    moving_char = ""
                else:
                    moving_char = self.movingAception.characters[moving_aception_id]

                is_char_an_space = self.trainText.characters[char_id] == " "
                is_final_char = char_id == len(self.trainText.characters) - 1
                is_same_char = self.trainText.characters[char_id] == moving_char
                if is_char_an_space or is_final_char:
                    if word_match:
                        word_match_count += 1
                    word_match = True

                elif is_same_char and moving_char != "":
                    char_match_count += 1
                else:
                    word_match = False

                char_id += 1

            match_data = MatchData(
                self,
                self.movingAception.wordCount,
                word_match_count,
                self.movingAception.CountCharactersWithoutSpaces(),
                char_match_count)
            list_of_match_data.append(match_data)

            train_id += 1
        return list_of_match_data
