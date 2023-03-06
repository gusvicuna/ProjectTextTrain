import tkinter as tk
from src.services.ProcessTrainText import (ToListOfTrainTextMatchs,
                                           OrderListOfTrainTextMatches)
from src.enums.sortType import SortType
from src.views.plotpage import PlotPage
from src.views.gridpage import GridPage
from src.services.DatabaseToAceptions import DBtoAceptions


class MainView(tk.Frame):

    ordered_train_text_matches = None
    train_text = None
    has_been_plot_reseted = False
    has_been_grid_reset = False

    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)

        # Input Frame
        input_frame = tk.Frame(master=self)
        input_frame.pack(fill="x")

        entry_frame = tk.Frame(master=input_frame, height=50)
        entry_frame.pack(side="top", fill="x")

        entry_label = tk.Label(
            master=entry_frame,
            text="Ingrese Tren de Texto:")
        entry_label.pack(fill=tk.X)

        entry = tk.Entry(master=entry_frame)
        entry.pack(fill=tk.X)
        entry.insert(
            0, "el repartidor dentro de 15-20 minutos entrega el paquete")

        options_frame = tk.Frame(master=input_frame)
        options_frame.pack(side="top", fill="x")

        order_tk = tk.IntVar()
        order_by_char_radio_button = tk.Radiobutton(
            master=options_frame,
            text="Porcentaje de carácteres",
            variable=order_tk, value=1)
        order_by_char_radio_button.grid(column=0, row=0)
        order_by_words_radio_button = tk.Radiobutton(
            master=options_frame,
            text="Porcentaje de palabras",
            variable=order_tk,
            value=2)
        order_by_words_radio_button.grid(column=0, row=1)

        is_reversed_tk = tk.IntVar()
        is_reversed_checkbox = tk.Checkbutton(
            master=options_frame,
            text="Revertir orden",
            variable=is_reversed_tk)
        is_reversed_checkbox.grid(column=1, row=0)

        execute_button = tk.Button(master=input_frame, text="Ejecutar")
        execute_button.pack(side="top", fill="x")

        self.feedback_frame = tk.Frame(master=input_frame, height=100)
        self.feedback_frame.pack(side="top", fill="x")

        self.feedback_label = tk.Label(master=self.feedback_frame,
                                       text="", height=50)
        self.feedback_label.place(width=0, height=0)

        def ResetTrainText(event):
            self.has_been_grid_reset = True
            self.has_been_plot_reseted = True

            self.feedback_label = tk.Label(master=self.feedback_frame,
                                           text="Cargando...", height=50)
            self.feedback_label.place(width=0, height=0)

            self.train_text = entry.get()

            order = 1
            if order_tk.get() == 1:
                order = SortType.CHARACTERSPERCENT
            elif order_tk.get() == 2:
                order = SortType.WORDSPERCENT

            is_reversed = True
            if is_reversed_tk.get() == 0:
                is_reversed = False
            else:
                is_reversed = True

            aceptions = DBtoAceptions()

            train_text_matches = ToListOfTrainTextMatchs(
                aceptions,
                trainText=self.train_text)
            self.ordered_train_text_matches = OrderListOfTrainTextMatches(
                train_text_matches,
                order=order,
                isOrderReversed=is_reversed)

            self.feedback_label = tk.Label(master=self.feedback_frame,
                                           text="Cargado ☻", height=50)
            self.feedback_label.place(width=0, height=0)

        execute_button.bind("<Button-1>", ResetTrainText)

        # Pages
        plot_page = PlotPage(self)
        grid_page = GridPage(self)

        button_frame = tk.Frame(self)
        button_frame.pack(side="top", fill="x")
        page_container = tk.Frame(master=self)
        page_container.pack(side="top", fill="both", expand=True)

        plot_page.place(in_=page_container, x=0, y=0, relheight=1, relwidth=1)
        grid_page.place(in_=page_container, x=0, y=0, relheight=1, relwidth=1)

        def ShowPlotResults(event):
            if self.has_been_plot_reseted:
                self.has_been_plot_reseted = False
                plot_page.ShowResults(self.ordered_train_text_matches)
            plot_page.show()

        def ShowGridResults(event):
            if self.has_been_grid_reset:
                self.has_been_grid_reset = False
                grid_page.LoadMatchTrain(trainText=self.train_text)
            grid_page.show()

        plot_page_button = tk.Button(
            button_frame,
            text="Mostrar Gráfico")
        grid_page_button = tk.Button(
            button_frame,
            text="Mostrar Cuadrícula",
            command=grid_page.show
        )

        plot_page.show()

        plot_page_button.pack(side="left")
        grid_page_button.pack(side="left")

        plot_page_button.bind("<Button-1>", ShowPlotResults)
        grid_page_button.bind("<Button-1>", ShowGridResults)
