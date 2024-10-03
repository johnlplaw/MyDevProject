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
    path = "output_phrase2"
    plt.savefig(path+"/"+Title + '.png')

    # Clear the current figure for the next plot
    plt.clf()



# def plotingGraph(Title, modelTypeList, langTypeList, pfmTypeList, ylabel):
#
#     for langType in langTypeList:
#         for pfmType in pfmTypeList:
#             performDataList = []
#             for modelType in modelTypeList:
#                 Type = " (" + langType + " - " + pfmTypeTxt(pfmType) + ") "
#                 datasetSizeList = ["400", "1600", "2800"]
#
#                 for dsSize in datasetSizeList:
#                     label = modelType + "-" + dsSize
#                     yvalue = dict[modelType + "_" + langType + "_" + dsSize][pfmType].tolist()
#                     performData1 = PerformanceData(label, yvalue)
#                     performDataList.append(performData1)
#
#             plotGraph(Title + Type, performDataList, ylabel)

def pfmTypeTxt(type):
    str = ""
    if type == "training_accuracy":
        str = "Training accuracy"
    elif type == "val_accuracy":
        str = "Validation accuracy"
    elif type == "elapsed":
        str = "Elapse"
    return str

# Functions - end

#Step0: Env Setting
dataFile = "./TrainingModelTrainingProcess_phrase2.csv"
datatypeList = ['SYN', 'GPT']
dataSizeList = ['400', '1600', '2800']
langTypeList = ['ENG', 'MULTI']
modelTypeList = ['FBXLMR', 'mBERT']
labelTypeList = ['LBL', 'PLBL', 'SLBL']
pfmTypeList = ["training_accuracy", "val_accuracy" ]
pfmTypeList = ["elapsed"]
#Step1: Read the file
df = Read_data(dataFile)

#Step2: Content of the data

## model name
model_list = pd.unique(df['model_name'])
#print(model_list)

FBXLMR_GPT_LBL_MULTI_400 = Filter_data(df, "Final-FB-XLM-R_gpt_LBL_Multilingual_400_1e-05")
FBXLMR_GPT_LBL_MULTI_1600 = Filter_data(df, "Final-FB-XLM-R_gpt_LBL_Multilingual_1600_1e-05")
FBXLMR_GPT_LBL_MULTI_2800 = Filter_data(df, "Final-FB-XLM-R_gpt_LBL_Multilingual_2800_1e-05")
FBXLMR_GPT_PLBL_MULTI_400 = Filter_data(df, "Final-FB-XLM-R_gpt_PLBL_Multilingual_400_1e-05")
FBXLMR_GPT_PLBL_MULTI_1600 = Filter_data(df, "Final-FB-XLM-R_gpt_PLBL_Multilingual_1600_1e-05")
FBXLMR_GPT_PLBL_MULTI_2800 = Filter_data(df, "Final-FB-XLM-R_gpt_PLBL_Multilingual_2800_1e-05")
FBXLMR_GPT_SLBL_MULTI_400 = Filter_data(df, "Final-FB-XLM-R_gpt_SLBL_Multilingual_2800_1e-05")
FBXLMR_GPT_SLBL_MULTI_1600 = Filter_data(df, "Final-FB-XLM-R_gpt_SLBL_Multilingual_1600_1e-05")
FBXLMR_GPT_SLBL_MULTI_2800 = Filter_data(df, "Final-FB-XLM-R_gpt_SLBL_Multilingual_400_1e-05")

mBERT_GPT_LBL_MULTI_400 = Filter_data(df, "Final-mBERT_gpt_LBL_Multilingual_400_1e-05")
mBERT_GPT_LBL_MULTI_1600 = Filter_data(df, "Final-mBERT_gpt_LBL_Multilingual_1600_1e-05")
mBERT_GPT_LBL_MULTI_2800 = Filter_data(df, "Final-mBERT_gpt_LBL_Multilingual_2800_1e-05")
mBERT_GPT_PLBL_MULTI_400 = Filter_data(df, "Final-mBERT_gpt_PLBL_Multilingual_400_1e-05")
mBERT_GPT_PLBL_MULTI_1600 = Filter_data(df, "Final-mBERT_gpt_PLBL_Multilingual_1600_1e-05")
mBERT_GPT_PLBL_MULTI_2800 = Filter_data(df, "Final-mBERT_gpt_PLBL_Multilingual_2800_1e-05")
mBERT_GPT_SLBL_MULTI_400 = Filter_data(df, "Final-mBERT_gpt_SLBL_Multilingual_400_1e-05")
mBERT_GPT_SLBL_MULTI_1600 = Filter_data(df, "Final-mBERT_gpt_SLBL_Multilingual_1600_1e-05")
mBERT_GPT_SLBL_MULTI_2800 = Filter_data(df, "Final-mBERT_gpt_SLBL_Multilingual_2800_1e-05")

# From Synthetic dataset

FBXLMR_SYN_LBL_ENG_400 = Filter_data(df, "Final-FB-XLM-R_LBL_English_400_1e-05")
FBXLMR_SYN_LBL_ENG_1600 = Filter_data(df, "Final-FB-XLM-R_LBL_English_1600_1e-05")
FBXLMR_SYN_LBL_ENG_2800 = Filter_data(df, "Final-FB-XLM-R_LBL_English_2800_1e-05")
FBXLMR_SYN_PLBL_ENG_400 = Filter_data(df, "Final-FB-XLM-R_PLBL_English_400_1e-05")
FBXLMR_SYN_PLBL_ENG_1600 = Filter_data(df, "Final-FB-XLM-R_PLBL_English_1600_1e-05")
FBXLMR_SYN_PLBL_ENG_2800 = Filter_data(df, "Final-FB-XLM-R_PLBL_English_2800_1e-05")
FBXLMR_SYN_SLBL_ENG_400 = Filter_data(df, "Final-FB-XLM-R_SLBL_English_400_1e-05")
FBXLMR_SYN_SLBL_ENG_1600 = Filter_data(df, "Final-FB-XLM-R_SLBL_English_1600_1e-05")
FBXLMR_SYN_SLBL_ENG_2800 = Filter_data(df, "Final-FB-XLM-R_SLBL_English_2800_1e-05")

mBERT_SYN_LBL_ENG_400 = Filter_data(df, "Final-mBERT_LBL_English_400_1e-05")
mBERT_SYN_LBL_ENG_1600 = Filter_data(df, "Final-mBERT_LBL_English_1600_1e-05")
mBERT_SYN_LBL_ENG_2800 = Filter_data(df, "Final-mBERT_LBL_English_2800_1e-05")
mBERT_SYN_PLBL_ENG_400 = Filter_data(df, "Final-mBERT_PLBL_English_400_1e-05")
mBERT_SYN_PLBL_ENG_1600 = Filter_data(df, "Final-mBERT_PLBL_English_1600_1e-05")
mBERT_SYN_PLBL_ENG_2800 = Filter_data(df, "Final-mBERT_PLBL_English_2800_1e-05")
mBERT_SYN_SLBL_ENG_400 = Filter_data(df, "Final-mBERT_SLBL_English_400_1e-05")
mBERT_SYN_SLBL_ENG_1600 = Filter_data(df, "Final-mBERT_SLBL_English_1600_1e-05")
mBERT_SYN_SLBL_ENG_2800 = Filter_data(df, "Final-mBERT_SLBL_English_2800_1e-05")

FBXLMR_SYN_LBL_MULTI_400 = Filter_data(df, "Final-FB-XLM-R_LBL_Multilingual_400_1e-05")
FBXLMR_SYN_LBL_MULTI_1600 = Filter_data(df, "Final-FB-XLM-R_LBL_Multilingual_1600_1e-05")
FBXLMR_SYN_LBL_MULTI_2800 = Filter_data(df, "Final-FB-XLM-R_LBL_Multilingual_2800_1e-05")
FBXLMR_SYN_PLBL_MULTI_400 = Filter_data(df, "Final-FB-XLM-R_PLBL_Multilingual_400_1e-05")
FBXLMR_SYN_PLBL_MULTI_1600 = Filter_data(df, "Final-FB-XLM-R_PLBL_Multilingual_1600_1e-05")
FBXLMR_SYN_PLBL_MULTI_2800 = Filter_data(df, "Final-FB-XLM-R_PLBL_Multilingual_2800_1e-05")
FBXLMR_SYN_SLBL_MULTI_400 = Filter_data(df, "Final-FB-XLM-R_SLBL_Multilingual_400_1e-05")
FBXLMR_SYN_SLBL_MULTI_1600 = Filter_data(df, "Final-FB-XLM-R_SLBL_Multilingual_1600_1e-05")
FBXLMR_SYN_SLBL_MULTI_2800 = Filter_data(df, "Final-FB-XLM-R_SLBL_Multilingual_2800_1e-05")

mBERT_SYN_LBL_MULTI_400 = Filter_data(df, "Final-mBERT_LBL_Multilingual_400_1e-05")
mBERT_SYN_LBL_MULTI_1600 = Filter_data(df, "Final-mBERT_LBL_Multilingual_1600_1e-05")
mBERT_SYN_LBL_MULTI_2800 = Filter_data(df, "Final-mBERT_LBL_Multilingual_2800_1e-05")
mBERT_SYN_PLBL_MULTI_400 = Filter_data(df, "Final-mBERT_PLBL_Multilingual_400_1e-05")
mBERT_SYN_PLBL_MULTI_1600 = Filter_data(df, "Final-mBERT_PLBL_Multilingual_1600_1e-05")
mBERT_SYN_PLBL_MULTI_2800 = Filter_data(df, "Final-mBERT_PLBL_Multilingual_2800_1e-05")
mBERT_SYN_SLBL_MULTI_400 = Filter_data(df, "Final-mBERT_SLBL_Multilingual_400_1e-05")
mBERT_SYN_SLBL_MULTI_1600 = Filter_data(df, "Final-mBERT_SLBL_Multilingual_1600_1e-05")
mBERT_SYN_SLBL_MULTI_2800 = Filter_data(df, "Final-mBERT_SLBL_Multilingual_2800_1e-05")

# From ChatGPT dataset
dictGpt = {
"FBXLMR_GPT_LBL_MULTI_400" : FBXLMR_GPT_LBL_MULTI_400,
"FBXLMR_GPT_LBL_MULTI_1600" : FBXLMR_GPT_LBL_MULTI_1600,
"FBXLMR_GPT_LBL_MULTI_2800" : FBXLMR_GPT_LBL_MULTI_2800,
"FBXLMR_GPT_PLBL_MULTI_400" : FBXLMR_GPT_PLBL_MULTI_400,
"FBXLMR_GPT_PLBL_MULTI_1600" : FBXLMR_GPT_PLBL_MULTI_1600,
"FBXLMR_GPT_PLBL_MULTI_2800" : FBXLMR_GPT_PLBL_MULTI_2800,
"FBXLMR_GPT_SLBL_MULTI_400" : FBXLMR_GPT_SLBL_MULTI_400,
"FBXLMR_GPT_SLBL_MULTI_1600" : FBXLMR_GPT_SLBL_MULTI_1600,
"FBXLMR_GPT_SLBL_MULTI_2800" : FBXLMR_GPT_SLBL_MULTI_2800,

"mBERT_GPT_LBL_MULTI_400" : mBERT_GPT_LBL_MULTI_400,
"mBERT_GPT_LBL_MULTI_1600" : mBERT_GPT_LBL_MULTI_1600,
"mBERT_GPT_LBL_MULTI_2800" : mBERT_GPT_LBL_MULTI_2800,
"mBERT_GPT_PLBL_MULTI_400" : mBERT_GPT_PLBL_MULTI_400,
"mBERT_GPT_PLBL_MULTI_1600" : mBERT_GPT_PLBL_MULTI_1600,
"mBERT_GPT_PLBL_MULTI_2800" : mBERT_GPT_PLBL_MULTI_2800,
"mBERT_GPT_SLBL_MULTI_400" : mBERT_GPT_SLBL_MULTI_400,
"mBERT_GPT_SLBL_MULTI_1600" : mBERT_GPT_SLBL_MULTI_1600,
"mBERT_GPT_SLBL_MULTI_2800" : mBERT_GPT_SLBL_MULTI_2800,
}
# From Synthetic dataset
dictSyn = {
"FBXLMR_SYN_LBL_ENG_400" : FBXLMR_SYN_LBL_ENG_400,
"FBXLMR_SYN_LBL_ENG_1600" : FBXLMR_SYN_LBL_ENG_1600,
"FBXLMR_SYN_LBL_ENG_2800" : FBXLMR_SYN_LBL_ENG_2800,
"FBXLMR_SYN_PLBL_ENG_400" : FBXLMR_SYN_PLBL_ENG_400,
"FBXLMR_SYN_PLBL_ENG_1600" : FBXLMR_SYN_PLBL_ENG_1600,
"FBXLMR_SYN_PLBL_ENG_2800" : FBXLMR_SYN_PLBL_ENG_2800,
"FBXLMR_SYN_SLBL_ENG_400" : FBXLMR_SYN_SLBL_ENG_400,
"FBXLMR_SYN_SLBL_ENG_1600" : FBXLMR_SYN_SLBL_ENG_1600,
"FBXLMR_SYN_SLBL_ENG_2800" : FBXLMR_SYN_SLBL_ENG_2800,

"mBERT_SYN_LBL_ENG_400" : mBERT_SYN_LBL_ENG_400,
"mBERT_SYN_LBL_ENG_1600" : mBERT_SYN_LBL_ENG_1600,
"mBERT_SYN_LBL_ENG_2800" : mBERT_SYN_LBL_ENG_2800,
"mBERT_SYN_PLBL_ENG_400" : mBERT_SYN_PLBL_ENG_400,
"mBERT_SYN_PLBL_ENG_1600" : mBERT_SYN_PLBL_ENG_1600,
"mBERT_SYN_PLBL_ENG_2800" : mBERT_SYN_PLBL_ENG_2800,
"mBERT_SYN_SLBL_ENG_400" : mBERT_SYN_SLBL_ENG_400,
"mBERT_SYN_SLBL_ENG_1600" : mBERT_SYN_SLBL_ENG_1600,
"mBERT_SYN_SLBL_ENG_2800" : mBERT_SYN_SLBL_ENG_2800,

"FBXLMR_SYN_LBL_MULTI_400" : FBXLMR_SYN_LBL_MULTI_400,
"FBXLMR_SYN_LBL_MULTI_1600" : FBXLMR_SYN_LBL_MULTI_1600,
"FBXLMR_SYN_LBL_MULTI_2800" : FBXLMR_SYN_LBL_MULTI_2800,
"FBXLMR_SYN_PLBL_MULTI_400" : FBXLMR_SYN_PLBL_MULTI_400,
"FBXLMR_SYN_PLBL_MULTI_1600" : FBXLMR_SYN_PLBL_MULTI_1600,
"FBXLMR_SYN_PLBL_MULTI_2800" : FBXLMR_SYN_PLBL_MULTI_2800,
"FBXLMR_SYN_SLBL_MULTI_400" : FBXLMR_SYN_SLBL_MULTI_400,
"FBXLMR_SYN_SLBL_MULTI_1600" : FBXLMR_SYN_SLBL_MULTI_1600,
"FBXLMR_SYN_SLBL_MULTI_2800" : FBXLMR_SYN_SLBL_MULTI_2800,

"mBERT_SYN_LBL_MULTI_400" : mBERT_SYN_LBL_MULTI_400,
"mBERT_SYN_LBL_MULTI_1600" : mBERT_SYN_LBL_MULTI_1600,
"mBERT_SYN_LBL_MULTI_2800" : mBERT_SYN_LBL_MULTI_2800,
"mBERT_SYN_PLBL_MULTI_400" : mBERT_SYN_PLBL_MULTI_400,
"mBERT_SYN_PLBL_MULTI_1600" : mBERT_SYN_PLBL_MULTI_1600,
"mBERT_SYN_PLBL_MULTI_2800" : mBERT_SYN_PLBL_MULTI_2800,
"mBERT_SYN_SLBL_MULTI_400" : mBERT_SYN_SLBL_MULTI_400,
"mBERT_SYN_SLBL_MULTI_1600" : mBERT_SYN_SLBL_MULTI_1600,
"mBERT_SYN_SLBL_MULTI_2800" : mBERT_SYN_SLBL_MULTI_2800

}


## Each Model name generating
ylabel = "Accuracy"
Title = "Performance vs Epoch"
#Title = "Elapse vs Epoch"
pfmTypeList = ["training_accuracy", "val_accuracy" ]

def plotThePerformance(dataType, dict):
    for modelType in modelTypeList:

        for labelType in labelTypeList:
            for langType in langTypeList:
                for pfmType in pfmTypeList:
                    Type = " (" + modelType + '-' + dataType + '-' + labelType + '-' + langType + " - " + pfmTypeTxt(pfmType) + ") "
                    performDataList = []
                    for dataSize in dataSizeList:
                        label = modelType + "_" + dataType + "_" + labelType + "_" + langType + "_" + dataSize
                        if label in dict:
                            yvalue = dict[label][pfmType].tolist()
                            performData1 = PerformanceData(label, yvalue)
                            performDataList.append(performData1)

                    print(Title + Type)
                    if len(performDataList) > 0:
                        plotGraph(Title + Type, performDataList, ylabel)

dataType = "SYN"
dict = dictSyn
plotThePerformance(dataType, dict)

dataType = "GPT"
dict = dictGpt
plotThePerformance(dataType, dict)


# modelTypeList = ["FB-XLM-R", "mBERT"]
#
# ## Either
# #
# # ylabel = "Accuracy"
# # Title = "Performance vs Epoch"
# ## Or
#
# langTypeList = ["English", "Multilingual"]
# Title = "Elapse vs Epoch"
# ##
#
# ylabel = "Elapse (seconds)"
# plotingGraph(Title, modelTypeList, langTypeList, pfmTypeList, ylabel)












#
#
# DF_FBXLMR_English_1600 = Filter_data(df, "Final-FB-XLM-R_English_1600_1e-05")
# DF_FBXLMR_English_2800 = Filter_data(df, "Final-FB-XLM-R_English_2800_1e-05")
# DF_FBXLMR_English_400 = Filter_data(df, "Final-FB-XLM-R_English_400_1e-05")
# DF_FBXLMR_Multilingual_1600 = Filter_data(df, "Final-FB-XLM-R_Multilingual_1600_1e-05")
# DF_FBXLMR_Multilingual_2800 = Filter_data(df, "Final-FB-XLM-R_Multilingual_2800_1e-05")
# DF_FBXLMR_Multilingual_400 = Filter_data(df, "Final-FB-XLM-R_Multilingual_400_1e-05")
# DF_mBERT_English_1600 = Filter_data(df, "Final-mBERT_English_1600_1e-05")
# DF_mBERT_English_2800 = Filter_data(df, "Final-mBERT_English_2800_1e-05")
# DF_mBERT_English_400 = Filter_data(df, "Final-mBERT_English_400_1e-05")
# DF_mBERT_Multilingual_1600 = Filter_data(df, "Final-mBERT_Multilingual_1600_1e-05")
# DF_mBERT_Multilingual_2800 = Filter_data(df, "Final-mBERT_Multilingual_2800_1e-05")
# DF_mBERT_Multilingual_400 = Filter_data(df, "Final-mBERT_Multilingual_400_1e-05")
#
# dict = {
#
# "FB-XLM-R_English_1600" : DF_FBXLMR_English_1600,
# "FB-XLM-R_English_2800" : DF_FBXLMR_English_2800,
# "FB-XLM-R_English_400" : DF_FBXLMR_English_400,
# "FB-XLM-R_Multilingual_1600" : DF_FBXLMR_Multilingual_1600,
# "FB-XLM-R_Multilingual_2800" : DF_FBXLMR_Multilingual_2800,
# "FB-XLM-R_Multilingual_400" : DF_FBXLMR_Multilingual_400,
# "mBERT_English_1600" : DF_mBERT_English_1600,
# "mBERT_English_2800" : DF_mBERT_English_2800,
# "mBERT_English_400" : DF_mBERT_English_400,
# "mBERT_Multilingual_1600" : DF_mBERT_Multilingual_1600,
# "mBERT_Multilingual_2800" : DF_mBERT_Multilingual_2800,
# "mBERT_Multilingual_400" : DF_mBERT_Multilingual_400
# }



# Ploting Graphs





# modelTypeList = ["FB-XLM-R", "mBERT"]
#
# ## Either
# # pfmTypeList = ["training_accuracy", "val_accuracy" ]
# # ylabel = "Accuracy"
# # Title = "Performance vs Epoch"
# ## Or
# pfmTypeList = ["elapsed"]
# langTypeList = ["English", "Multilingual"]
# Title = "Elapse vs Epoch"
# ##
#
# ylabel = "Elapse (seconds)"
# plotingGraph(Title, modelTypeList, langTypeList, pfmTypeList, ylabel)

# tmpdf = df
#
# aggDf = tmpdf.groupby("model_name")['elapsed'].agg('sum')
#
# newDf = pd.DataFrame(aggDf)
# newDf = newDf.reset_index(names=['model_name'])
# newDf['duration'] = newDf['elapsed'].astype('datetime64[s]').dt.strftime("%d day %H:%M:%S")
#
# newDf['name'] = newDf["model_name"].str.replace('Final-','',regex=True)
# newDf['name'] = newDf["name"].str.replace('_1e-05','',regex=True)
# print(newDf[['name', 'duration']])
# newDf.to_csv("duration.csv")

