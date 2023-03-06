from src.classes.Aception import Aception
from src.classes.TextTrainMatch import TrainTextMatch
from src.enums.sortType import SortType


def ToListOfTrainTextMatchs(aceptions=str,
                            trainText=str):

    train_text_aception = Aception(trainText, None, None)

    list_of_train_texts = []
    for aception in aceptions:
        matches = TrainTextMatch(train_text_aception, aception)
        list_of_train_texts.append(matches)

    # WriteResults(listOfTrainTextsMatch=list_of_train_texts)
    return list_of_train_texts


def OrderListOfTrainTextMatches(listOfTrainTextMatches,
                                order=SortType, isOrderReversed=bool):
    new_list = listOfTrainTextMatches
    if order == SortType.CHARACTERSPERCENT:
        new_list.sort(key=OrderMatchesByPercentKey,
                      reverse=isOrderReversed)
    elif order == SortType.WORDSPERCENT:
        new_list.sort(key=OrderMatchesByWordPercentKey,
                      reverse=isOrderReversed)
    return new_list


def OrderMatchesByPercentKey(trainTextMatch=TrainTextMatch):
    return trainTextMatch.GetGreatestPercentageOfCharMatch()


def OrderMatchesByWordPercentKey(trainTextMatch=TrainTextMatch):
    return trainTextMatch.GetGreatestPercentageOfWordMatch()


def WriteResults(listOfTrainTextsMatch):
    f = open("demoMatchTrain.txt", "w")
    f.write(f"Tren de Texto: {listOfTrainTextsMatch[0].trainText.text}\n")
    for train_text_match in listOfTrainTextsMatch:
        f.write(f"\n Acepción: {train_text_match.movingAception}\n")
        for match_data in train_text_match.listOfMatchData:
            f.write(f"{str(match_data)}\n")
    f.close()
