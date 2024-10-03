import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from dataclasses import dataclass

# Functions - start
def Read_data(dataFile):
    """
    Read a data from a csv file and return the contain in dataframe object
    :param dataFile: The csv file
    :return: data in dataframe object
    """
    df = pd.read_csv(dataFile)
    return df


def Filter_data(df, modelName):
    newDf = df[df["model_name"] == modelName]
    return newDf

@dataclass
class PerformanceData:
    label: str
    yvalue: list

def plotGraph(Title, performDataList, ylabel):

    # line 1 points
    x1 = range(1, 16)
    # plotting the lines
    for performData in performDataList:
        plt.plot(x1, performData.yvalue, label = performData.label)

    # naming the x axis
    plt.xlabel('Epoch')
    # naming the y axis
    plt.ylabel(ylabel)
    # giving a title to my graph
    plt.title(Title)

    # show a legend on the plot
    plt.legend()

    # function to show the plot
    # plt.show()

    plt.savefig(Title + '.png')
    plt.clf()
# Functions - end

#Step0: Env Setting
dataFile = "./TrainingModelTrainingProcess_phrase1.csv"
dataSizeList = ['400', '1600', '2800']
langTypeList = ['English', 'Multilingual']
modelTypeList = ['FB-XLM-R', 'mBERT']

#Step1: Read the file
df = Read_data(dataFile)

#Step2: Content of the data

## model name
model_list = pd.unique(df['model_name'])
print(model_list)

## Each Model
DF_FBXLMR_English_1600 = Filter_data(df, "Final-FB-XLM-R_English_1600_1e-05")
DF_FBXLMR_English_2800 = Filter_data(df, "Final-FB-XLM-R_English_2800_1e-05")
DF_FBXLMR_English_400 = Filter_data(df, "Final-FB-XLM-R_English_400_1e-05")
DF_FBXLMR_Multilingual_1600 = Filter_data(df, "Final-FB-XLM-R_Multilingual_1600_1e-05")
DF_FBXLMR_Multilingual_2800 = Filter_data(df, "Final-FB-XLM-R_Multilingual_2800_1e-05")
DF_FBXLMR_Multilingual_400 = Filter_data(df, "Final-FB-XLM-R_Multilingual_400_1e-05")
DF_mBERT_English_1600 = Filter_data(df, "Final-mBERT_English_1600_1e-05")
DF_mBERT_English_2800 = Filter_data(df, "Final-mBERT_English_2800_1e-05")
DF_mBERT_English_400 = Filter_data(df, "Final-mBERT_English_400_1e-05")
DF_mBERT_Multilingual_1600 = Filter_data(df, "Final-mBERT_Multilingual_1600_1e-05")
DF_mBERT_Multilingual_2800 = Filter_data(df, "Final-mBERT_Multilingual_2800_1e-05")
DF_mBERT_Multilingual_400 = Filter_data(df, "Final-mBERT_Multilingual_400_1e-05")

dict = {

"FB-XLM-R_English_1600" : DF_FBXLMR_English_1600,
"FB-XLM-R_English_2800" : DF_FBXLMR_English_2800,
"FB-XLM-R_English_400" : DF_FBXLMR_English_400,
"FB-XLM-R_Multilingual_1600" : DF_FBXLMR_Multilingual_1600,
"FB-XLM-R_Multilingual_2800" : DF_FBXLMR_Multilingual_2800,
"FB-XLM-R_Multilingual_400" : DF_FBXLMR_Multilingual_400,
"mBERT_English_1600" : DF_mBERT_English_1600,
"mBERT_English_2800" : DF_mBERT_English_2800,
"mBERT_English_400" : DF_mBERT_English_400,
"mBERT_Multilingual_1600" : DF_mBERT_Multilingual_1600,
"mBERT_Multilingual_2800" : DF_mBERT_Multilingual_2800,
"mBERT_Multilingual_400" : DF_mBERT_Multilingual_400
}



# Ploting Graphs

def pfmTypeTxt(type):
    str = ""
    if type == "training_accuracy":
        str = "Training accuracy"
    elif type == "val_accuracy":
        str = "Validation accuracy"
    elif type == "elapsed":
        str = "Elapse"
    return str

def plotingGraph(Title, modelTypeList, langTypeList, pfmTypeList, ylabel):



    for langType in langTypeList:
        for pfmType in pfmTypeList:
            performDataList = []
            for modelType in modelTypeList:
                Type = " (" + langType + " - " + pfmTypeTxt(pfmType) + ") "
                datasetSizeList = ["400", "1600", "2800"]

                for dsSize in datasetSizeList:
                    label = modelType + "-" + dsSize
                    yvalue = dict[modelType + "_" + langType + "_" + dsSize][pfmType].tolist()
                    performData1 = PerformanceData(label, yvalue)
                    performDataList.append(performData1)

            plotGraph(Title + Type, performDataList, ylabel)


modelTypeList = ["FB-XLM-R", "mBERT"]

## Either
# pfmTypeList = ["training_accuracy", "val_accuracy" ]
# ylabel = "Accuracy"
# Title = "Performance vs Epoch"
## Or
pfmTypeList = ["elapsed"]
langTypeList = ["English", "Multilingual"]
Title = "Elapse vs Epoch"
##

ylabel = "Elapse (seconds)"
plotingGraph(Title, modelTypeList, langTypeList, pfmTypeList, ylabel)

