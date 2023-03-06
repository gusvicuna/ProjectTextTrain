import tkinter as tk
from src.views.page import Page
from src.views.plots.plotMatchTrain import PlotMatchTrain


class PlotPage(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        TITLETEXT = "Gráfico y orden de Acepcion"
        RESULTSFRAMEHEIGHT = 600
        RESULTSFRAMEWIDTH = 800
        self.limit = 10

        title = tk.Label(master=self, text=TITLETEXT)
        title.pack(side="top", fill="both")

        self.results_frame = tk.Frame(
            master=self,
            height=RESULTSFRAMEHEIGHT,
            width=RESULTSFRAMEWIDTH)
        self.results_frame.pack(side="top")

        self.plot_result_frame = tk.Frame(master=self.results_frame)
        self.plot_result_frame.pack(side="left", fill="y")

        self.aceptions_result_frame = tk.Frame(master=self.results_frame)
        self.aceptions_result_frame.pack(side="left", fill="y")

    def ShowResults(self, listOfTrainTextsMatch):

        self.ShowAceptionsListed(listOfTrainTextsMatch=listOfTrainTextsMatch)
        PlotMatchTrain(
            listOfTrainTextMatch=listOfTrainTextsMatch,
            frame=self.plot_result_frame)

    def ShowAceptionsListed(self, listOfTrainTextsMatch):
        i = 0
        while i < self.limit:
            aception_result_frame = tk.Frame(
                master=self.aceptions_result_frame,
                height=50)
            aception_result_frame.grid(row=i, pady=5)

            aception_label = tk.Label(
                master=aception_result_frame,
                text=f"{i+1}. {listOfTrainTextsMatch[i].aception}")
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
                text=f"Mejor porcentaje: {best_percent_of_chars}" +
                f"  {word_percent_symbol}")
            aception_percentage_label.pack()

            i += 1
