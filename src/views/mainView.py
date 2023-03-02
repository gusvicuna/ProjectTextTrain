import tkinter as tk
from src.services.GetAceptionsInOrder import GetAceptionsInOrder
from src.enums.sortType import SortType
from src.views.plotpage import PlotPage
from src.views.gridpage import GridPage
from src.services.DatabaseToAceptions import DBtoDrivers


class MainView(tk.Frame):
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

        match_button = tk.Button(master=input_frame, text="Ejecutar")
        match_button.pack(side="top", fill="x")

        # Pages
        plot_page = PlotPage(self)
        grid_page = GridPage(self)

        button_frame = tk.Frame(self)
        button_frame.pack(side="top", fill="x")
        page_container = tk.Frame(master=self)
        page_container.pack(side="top", fill="both", expand=True)

        plot_page.place(in_=page_container, x=0, y=0, relheight=1, relwidth=1)
        grid_page.place(in_=page_container, x=0, y=0, relheight=1, relwidth=1)

        plot_page_button = tk.Button(
            button_frame,
            text="Mostrar Gráfico",
            command=plot_page.show)
        grid_page_button = tk.Button(
            button_frame,
            text="Mostrar Cuadrícula",
            command=grid_page.show
        )

        plot_page.show()

        plot_page_button.pack(side="left")
        grid_page_button.pack(side="left")

        def handle_match_button_click(event):
            train_text = entry.get()

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

            drivers = DBtoDrivers()

            ordered_aceptions = GetAceptionsInOrder(
                drivers,
                trainText=train_text,
                order=order,
                isOrderReversed=is_reversed)

            plot_page.ShowResults(ordered_aceptions)
            grid_page.LoadMatchTrain(drivers)

        match_button.bind("<Button-1>", handle_match_button_click)
