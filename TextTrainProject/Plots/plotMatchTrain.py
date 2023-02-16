import matplotlib.pyplot as plt
import numpy as np

def PlotMatchTrain(listOfMatchData):
    listOfPercents = []
    for i in listOfMatchData: 
        listOfPercents.append(i.matchedCharsPercent)
    
    ypoints = listOfPercents
    xpoints = np.arange(0, len(ypoints))

    plt.plot(xpoints, ypoints)
    plt.show()