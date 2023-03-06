import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg,
    NavigationToolbar2Tk)


def PlotMatchTrain(listOfTrainTextMatch, frame) -> None:
    # the figure that will contain the plot
    fig = Figure(figsize=(5, 5), dpi=100)

    # adding the subplot
    plot1 = fig.add_subplot(111)
    plot1.set_ylim(0, 110)
    plot1.set_title(listOfTrainTextMatch[0].trainText.text)

    listOfTrainTextMatches = listOfTrainTextMatch
    listOfTrainTextMatches.reverse()

    for train_text_match in listOfTrainTextMatches:
        listOfPercents = []
        color = "yellow"

        for match_data in train_text_match.listOfMatchData:
            listOfPercents.append(match_data.matchedCharsPercent)

            if match_data.Has100PercentMatchedWords():
                color = "red"
                plot1.scatter(
                    train_text_match.listOfMatchData.index(match_data),
                    match_data.matchedCharsPercent,
                    c=color,
                    marker="*",
                    s=40,
                    linewidth=0)
            elif match_data.HasGreaterThan75PercentMatchedWords():
                color = "orange"
                plot1.scatter(
                    train_text_match.listOfMatchData.index(match_data),
                    match_data.matchedCharsPercent,
                    c=color,
                    marker="o",
                    s=40,
                    linewidth=0)

        ypoints = listOfPercents
        xpoints = np.arange(0, len(ypoints))

        plot1.plot(xpoints, ypoints, color)

    # creating the Tkinter canvas
    # containing the Matplotlib figure
    canvas = FigureCanvasTkAgg(fig,
                               master=frame)
    canvas.draw()
    # placing the canvas on the Tkinter window
    canvas.get_tk_widget().pack()

    # creating the Matplotlib toolbar
    toolbar = NavigationToolbar2Tk(canvas,
                                   frame)
    toolbar.update()

    # placing the toolbar on the Tkinter window
    canvas.get_tk_widget().place(x=0, y=0)
