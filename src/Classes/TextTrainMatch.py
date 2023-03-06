from src.classes.Aception import Aception
from src.classes.MatchData import MatchData


class TrainTextMatch:

    def __init__(self, trainText=Aception, aception=Aception) -> None:
        self.trainText = trainText
        self.aception = aception

    def MatchTrainText(self):
        list_of_match_data = []

        aception_char_count = len(self.aception.Characters())
        train_text_char_count = len(self.trainText.Characters())

        train_id = 0
        while train_id < aception_char_count + train_text_char_count:
            char_match_count = 0
            word_match_count = 0
            word_match = True

            char_id = 0
            while char_id < train_text_char_count:

                moving_aception_id =\
                    aception_char_count - train_id + char_id
                if moving_aception_id < 0 or moving_aception_id >=\
                        aception_char_count:
                    moving_char = ""
                else:
                    moving_char =\
                        self.aception.Characters()[moving_aception_id]

                is_char_an_space = self.trainText.Characters()[char_id] == " "
                is_final_char = char_id == train_text_char_count - 1
                is_same_char =\
                    self.trainText.Characters()[char_id] == moving_char
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
                len(self.aception.Words()),
                word_match_count,
                self.aception.CountCharactersWithoutSpaces(),
                char_match_count)
            list_of_match_data.append(match_data)

            train_id += 1
        return list_of_match_data

    def GetGreatestPercentageOfCharMatch(self):
        list_of_match_data = self.MatchTrainText()
        greatest_percentage = 0
        for match_data in list_of_match_data:
            if match_data.matchedCharsPercent > greatest_percentage:
                greatest_percentage = match_data.matchedCharsPercent
        return greatest_percentage

    def GetGreatestPercentageOfWordMatch(self):
        list_of_match_data = self.MatchTrainText()
        greatest_percentage = 0
        for match_data in list_of_match_data:
            if match_data.matchedWordsPercent > greatest_percentage:
                greatest_percentage = match_data.matchedWordsPercent
        return greatest_percentage
