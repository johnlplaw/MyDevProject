import matplotlib.pyplot as plt
import numpy as np
from dataclasses import dataclass

@dataclass
class PerformanceData:
    label: str
    yvalue: list

def plotGraph(Title, performDataList):

    # line 1 points
    x1 = range(1, 16)
    # plotting the lines
    for performData in performDataList:
        plt.plot(x1, performData.yvalue, label = performData.label)

    # naming the x axis
    plt.xlabel('Epoch')
    # naming the y axis
    plt.ylabel('Accuracy')
    # giving a title to my graph
    plt.title(Title)

    # show a legend on the plot
    plt.legend()

    # function to show the plot
    plt.show()

Title = "Performance VS Epoch"
label = "data 1"
yvalue = np.random.random_sample(size = 15)
performData = PerformanceData(label, yvalue)

performDataList = []
performDataList.append(performData)
plotGraph(Title, performDataList)