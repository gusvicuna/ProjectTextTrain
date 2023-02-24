import tkinter as tk
from Services.ProcessTrainText import ProcessTrainText
from Enums.SortType import SortType


def ShowMainView():
    window = tk.Tk()

    RESULTSFRAMEHEIGHT = 600
    RESULTSFRAMEWIDTH = 800
    PLOTRESULTSFRAMEWIDTH = 500

    input_frame = tk.Frame(master=window)
    input_frame.pack(fill=tk.X)

    entry_frame = tk.Frame(master=input_frame, height=50)
    entry_frame.grid(column=0)

    entry_label = tk.Label(master=entry_frame, text="Ingrese Tren de Texto:")
    entry_label.pack(fill=tk.X)

    entry = tk.Entry(master=entry_frame, width=50)
    entry.pack(fill=tk.X)
    entry.insert(0, "el repartidor dentro de 15-20 minutos entrega el paquete")

    options_frame = tk.Frame(master=input_frame)
    options_frame.grid(column=1, row=0)

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

    limit = 10

    button = tk.Button(master=input_frame, text="Match")
    button.grid(column=0, row=1)

    results_frame = tk.Frame(
        master=window,
        height=RESULTSFRAMEHEIGHT,
        width=RESULTSFRAMEWIDTH)
    results_frame.pack()

    def handle_match_button_click(event):
        plot_result_frame = tk.Frame(
            master=results_frame,
            height=RESULTSFRAMEHEIGHT,
            width=PLOTRESULTSFRAMEWIDTH)
        plot_result_frame.place(x=0, y=0)

        aceptions_result_frame = tk.Frame(
            master=results_frame,
            height=RESULTSFRAMEHEIGHT,
            width=RESULTSFRAMEWIDTH - PLOTRESULTSFRAMEWIDTH)
        aceptions_result_frame.place(x=PLOTRESULTSFRAMEWIDTH, y=0)
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

        ProcessTrainText(
            plotFrame=plot_result_frame,
            aceptionsFrame=aceptions_result_frame,
            trainText=train_text,
            order=order,
            isOrderReversed=is_reversed,
            limit=limit)

    button.bind("<Button-1>", handle_match_button_click)

    window.mainloop()


if __name__ == "__main__":
    ShowMainView()
