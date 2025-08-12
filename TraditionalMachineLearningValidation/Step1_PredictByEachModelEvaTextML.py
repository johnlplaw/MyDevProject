import DataLib as lib
import ModelLib as mlib

import os.path

"""
This script is for emotion prediction to be done by the models. The result of the prediction is updated in to the 
EVATEXTML table.
"""

TableName = 'EvaTextML'

#1. identify the selected model


model_file_path = "../TraditionalMachineLearning/output/"

for model in mlib.ml_model_list:

    dataObjlist = lib.get_cleanned_ori_text(TableName, model.colName)
    print (len(dataObjlist))
    print("==================")
    print(model.modelName + " start")
    print("==================")
    if len(dataObjlist) > 1:

        isFound = os.path.exists(model_file_path + model.fileName)
        print("Is model binary found: " + str(isFound))
        predict_list = lib.predictionML(model, model_file_path, dataObjlist)
        print(len(predict_list))
        lib.update_prediction_result(predict_list, TableName, model.colName)

    else :
        print ("Nothing to update")
        print("==================")
        print(model.modelName + " end")
        print("==================")


