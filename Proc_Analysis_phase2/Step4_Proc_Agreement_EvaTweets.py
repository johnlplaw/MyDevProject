import Analysis_Lib as lib
from Analysis_Lib import Selected_Model

"""
This script is for evaluating the predicted label of the models for the EvaTweets data against the "label" based on each labeling type.
"""
dsTypeList = ["tweets"]
labelingTypeList = ["pla"]
tableName = "EvaTweets"
label = "label"


# 1. Get the Model Info

labelList = [
    "Label",
"GPT_LBL_XMLB",
"GPT_PLBL_XMLB",
"GPT_SLBL_XMLB",
"GPT_LBL_MBERT",
"GPT_PLBL_MBERT",
"GPT_SLBL_MBERT",
"SYN_LBL_XMLB",
"SYN_PLBL_XMLB",
"SYN_SLBL_XMLB",
"SYN_LBL_MBERT",
"SYN_PLBL_MBERT",
"SYN_SLBL_MBERT",
"SYN_LBL_XMLB_E",
"SYN_PLBL_XMLB_E",
"SYN_SLBL_XMLB_E",
"SYN_LBL_MBERT_E",
"SYN_PLBL_MBERT_E",
"SYN_SLBL_MBERTE"
    ]

for dsType in dsTypeList:
    for labelType in labelingTypeList:
        plabelList = []
        for colName in labelList:
            list = lib.get_Label_List_tweets(tableName, colName)
            print(len(list))
            plabelList.append(list)

        kappaScores = lib.calculate_Cohen_Kappa_Score(plabelList)

        lib.plotHeatMapKappaScore(kappaScores, plabelList, labelList, dsType+"_"+labelType)
