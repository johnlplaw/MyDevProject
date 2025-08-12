import DataLib as lib
import ModelLib as mlib
from sklearn.metrics import accuracy_score, classification_report
import os.path

"""
This script is for evaluating the model performance.
"""

TableName = 'EvaTextML'

#1. identify the selected model
model_file_path = "../TraditionalMachineLearning/output/"

dstypeList = ['multiLangComb_nos','chatgpt']
labeltypeList = ['la', 'pla', 'sla']

for dstype in dstypeList:
    for labeltype in labeltypeList:
        for model in mlib.ml_model_list:
            print("======================================")
            print("Working on model: " + str(model.modelName) + ", Testing dataset: dstype: " + dstype + ", labeltype: " + labeltype)
            print("Model Name: " + model.fileName)
            dataObjlist = lib.get_predicted_labels(TableName, model.colName, dstype, labeltype)
            print(len(dataObjlist))
            testlabel = []
            predictedlabel = []

            for obj in dataObjlist:
                testlabel.append(obj.label)
                predictedlabel.append(obj.predictedLabel)

            print("Accuracy:", accuracy_score(testlabel, predictedlabel))
            print("Accuracy:", classification_report(testlabel, predictedlabel))
            print("======================================")
