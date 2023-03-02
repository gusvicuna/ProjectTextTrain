import tkinter as tk
from src.views.page import Page
from src.database.database import GetDatabase


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

    def LoadMatchTrain(self, drivers):
        database = GetDatabase()
        column_id = 0
        for driver in database:

            driver_frame = tk.Frame(master=self.grid_frame)
            driver_frame.grid(column=column_id, row=0)
            driver_label = tk.Label(master=driver_frame, text=driver)
            driver_label.pack(side="top", fill="x")

            row_id = 1
            for component in database[driver]:
                component_frame = tk.Frame(master=self.grid_frame)
                component_frame.grid(column=column_id, row=row_id)

                component_label = tk.Label(master=component_frame,
                                           text=component)
                component_label.pack(side="top", fill="x")

                row_id += 1
            column_id += 1
