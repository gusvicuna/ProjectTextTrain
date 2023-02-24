from Plots.plotMatchTrain import PlotMatchTrain
from Classes.Aception import Aception
from Services.DatabaseToAceptions import DBtoAceptions
from Classes.TextTrainMatch import TrainTextMatch
from Enums.SortType import SortType
import tkinter as tk


def ProcessTrainText(plotFrame,
                     aceptionsFrame,
                     trainText=str,
                     order=SortType,
                     isOrderReversed=bool,
                     limit=int):
    aceptions = DBtoAceptions()

    train_text_aception = Aception(trainText, None, None)

    list_of_train_texts = []
    for aception in aceptions:
        matches = TrainTextMatch(train_text_aception, aception)
        list_of_train_texts.append(matches)

    if order == SortType.CHARACTERSPERCENT:
        list_of_train_texts.sort(
            key=OrderMatchesByPercentKey,
            reverse=isOrderReversed)
    elif order == SortType.WORDSPERCENT:
        list_of_train_texts.sort(
            key=OrderMatchesByWordPercentKey,
            reverse=isOrderReversed)

    # WriteResults(listOfTrainTextsMatch=list_of_train_texts)

    ShowAceptionsInOrder(
        listOfTrainTextsMatch=list_of_train_texts,
        aceptionsFrame=aceptionsFrame,
        amount=limit)
    PlotMatchTrain(listOfTrainTextMatch=list_of_train_texts, window=plotFrame)


def OrderMatchesByPercentKey(trainTextMatch=TrainTextMatch):
    best_percentage = 0
    for i in trainTextMatch.listOfMatchData:
        if i.matchedCharsPercent > best_percentage:
            best_percentage = i.matchedCharsPercent
    return best_percentage


def OrderMatchesByWordPercentKey(trainTextMatch=TrainTextMatch):
    best_percentage = 0
    for i in trainTextMatch.listOfMatchData:
        if i.matchedWordsPercent > best_percentage:
            best_percentage = i.matchedWordsPercent
    return best_percentage


def WriteResults(listOfTrainTextsMatch):
    f = open("demoMatchTrain.txt", "w")
    f.write(f"Tren de Texto: {listOfTrainTextsMatch[0].trainText.text}\n")
    for train_text_match in listOfTrainTextsMatch:
        f.write(f"\n Acepción: {train_text_match.movingAception}\n")
        for match_data in train_text_match.listOfMatchData:
            f.write(f"{str(match_data)}\n")
    f.close()


def ShowAceptionsInOrder(listOfTrainTextsMatch, aceptionsFrame, amount=int):
    i = 0
    while i < amount:
        aception_result_frame = tk.Frame(master=aceptionsFrame, height=50)
        aception_result_frame.grid(row=i, pady=5)

        aception_label = tk.Label(
            master=aception_result_frame,
            text=f"{i+1}. {listOfTrainTextsMatch[i].movingAception}")
        aception_label.pack()

        has_100_percent_word = False
        has_75_percent_word = False
        best_percent_of_chars = 0
        for match in listOfTrainTextsMatch[i].listOfMatchData:
            if match.matchedCharsPercent > best_percent_of_chars:
                best_percent_of_chars = match.matchedCharsPercent
            if match.Has100PercentMatchedWords():
                has_100_percent_word = True
            elif match.HasGreaterThan75PercentMatchedWords():
                has_75_percent_word = True

        word_percent_symbol = " "
        if has_100_percent_word:
            word_percent_symbol = "(☆)"
        elif has_75_percent_word:
            word_percent_symbol = "(o)"

        aception_percentage_label = tk.Label(
            master=aception_result_frame,
            text=f"Mejor porcentaje: {best_percent_of_chars}  {word_percent_symbol}")
        aception_percentage_label.pack()

        i += 1
