import tkinter as tk
from src.views.page import Page
from src.services.DatabaseToAceptions import DBtoAceptions
from src.services.ProcessTrainText import ToListOfTrainTextMatchs


class GridPage(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        TITLETEXT = "Cuadrícula de Drivers y Componentes"

        title = tk.Label(master=self, text=TITLETEXT)
        title.pack(side="top", fill="both")

        self.grid_frame = tk.Frame(
            master=self
        )
        self.grid_frame.pack(side="top")

    def LoadMatchTrain(self, trainText):
        aceptions = DBtoAceptions()
        listOfTextTrainMatches = ToListOfTrainTextMatchs(aceptions=aceptions,
                                                         trainText=trainText)

        column_id = 0
        row_id = 1
        last_driver = listOfTextTrainMatches[0].aception.driver
        last_component = listOfTextTrainMatches[0].aception.component
        bg_color = "grey"
        greatest_char_perc = 0
        greatest_word_match = 0

        for textTrainMatch in listOfTextTrainMatches:

            aception = textTrainMatch.aception

            if aception.driver != last_driver:

                driver_frame = tk.Frame(master=self.grid_frame, bg=bg_color)
                driver_frame.grid(column=column_id, row=0)
                driver_label = tk.Label(master=driver_frame,
                                        text=last_driver,
                                        bg=bg_color)

                last_driver = aception.driver
                driver_label.pack(side="top", fill="x")

                column_id += 1
                row_id = 1

            if aception.component != last_component:

                component_frame = tk.Frame(master=self.grid_frame, bg=bg_color)
                component_frame.grid(column=column_id, row=row_id)

                component_label = tk.Label(master=component_frame,
                                           text=last_component,
                                           bg=bg_color)
                component_label.pack(side="top", fill="x")

                component_percent_label = tk.Label(
                    master=component_frame,
                    text=f"{greatest_char_perc} %",
                    bg=bg_color)
                component_percent_label.pack(side="top", fill="x")

                last_component = aception.component
                greatest_char_perc = 0
                bg_color = "grey"

                row_id += 1

            if textTrainMatch.GetGreatestPercentageOfCharMatch() >\
                    greatest_char_perc:
                greatest_char_perc =\
                        textTrainMatch.GetGreatestPercentageOfCharMatch()
            # greatest_word_match =\
            #   textTrainMatch.GetGreatestPercentageOfWordMatch()

            if greatest_char_perc == 100:
                bg_color = "green"
            elif greatest_char_perc > 75:
                bg_color = "yellow"
