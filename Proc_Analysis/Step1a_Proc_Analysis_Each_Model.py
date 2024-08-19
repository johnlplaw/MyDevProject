import Lib_analysis as lib
import os.path

"""
This script is for emotion prediction to be done by the models. The result of the prediction is updated in to the 
eva_eng_text and eva_mul_text tables.
"""

class Selected_Model:
    """
    Model info.
    """
    def __init__(self, fileName, modelName, colName):
        self.fileName = fileName
        self.modelName = modelName
        self.colName = colName

class TestingTextData:
    """
    Testing dataset info.
    """
    def __init__(self, dataList, tableName):
        self.dataList = dataList
        self.tableName = tableName


#1.  Get the texts to be predicted
eng_data_list = lib.get_cleanned_testing_text('eva_eng_text')
mul_data_list = lib.get_cleanned_testing_text('eva_mul_text')

eng_testing_obj = TestingTextData(eng_data_list, "eva_eng_text")
mul_testing_obj = TestingTextData(mul_data_list, "eva_mul_text")
dataset_list = [eng_testing_obj, mul_testing_obj]

# for txtData in data_list:
#     print(str(txtData.id) + " - " + txtData.clean_text)

#2. identify the selected model
e_mBert_400 = Selected_Model("Final-mBERT_English_400_1e-05_model.pth", "mBERT-400", lib.COL_MBERT_ENG_400)
e_mBert_1600 = Selected_Model("Final-mBERT_English_1600_1e-05_model.pth", "mBERT-1600", lib.COL_MBERT_ENG_1600)
e_mBert_2800 = Selected_Model("Final-mBERT_English_2800_1e-05_model.pth", "mBERT-2800", lib.COL_MBERT_ENG_2800)
e_fbXLMr_400 = Selected_Model("Final-FB-XLM-R_English_400_1e-05_model.pth", "FB-XLM-R-400", lib.COL_XLMR_ENG_400)
e_fbXLMr_1600 = Selected_Model("Final-FB-XLM-R_English_1600_1e-05_model.pth", "FB-XLM-R-1600", lib.COL_XLMR_ENG_1600)
e_fbXLMr_2800 = Selected_Model("Final-FB-XLM-R_English_2800_1e-05_model.pth", "FB-XLM-R-2800", lib.COL_XLMR_ENG_2800)
m_mBert_400 = Selected_Model("Final-mBERT_Multilingual_400_1e-05_model.pth", "mBERT-400", lib.COL_MBERT_MUL_400)
m_mBert_1600 = Selected_Model("Final-mBERT_Multilingual_1600_1e-05_model.pth", "mBERT-1600", lib.COL_MBERT_MUL_1600)
m_mBert_2800 = Selected_Model("Final-mBERT_Multilingual_2800_1e-05_model.pth", "mBERT-2800", lib.COL_MBERT_MUL_2800)
m_fbXLMr_400 = Selected_Model("Final-FB-XLM-R_Multilingual_400_1e-05_model.pth", "FB-XLM-R-400", lib.COL_XLMR_MUL_400)
m_fbXLMr_1600 = Selected_Model("FInal-FB-XLM-R_Multilingual_1600_1e-05_model.pth", "FB-XLM-R-1600", lib.COL_XLMR_MUL_1600)
m_fbXLMr_2800 = Selected_Model("Final-FB-XLM-R_Multilingual_2800_1e-05_model.pth", "FB-XLM-R-2800", lib.COL_XLMR_MUL_2800)


mbert_model_list = [e_mBert_400, e_mBert_1600, e_mBert_2800, m_mBert_400, m_mBert_1600, m_mBert_2800]
xmlr_model_list = [e_fbXLMr_400, e_fbXLMr_1600, e_fbXLMr_2800, m_fbXLMr_400, m_fbXLMr_1600, m_fbXLMr_2800]
model_file_path = "../Proc_Pretrained_Model/output/"


for model in mbert_model_list:
    """
    For mBERT model family
    """
    for ds in dataset_list:
        print("==================")
        print(model.modelName + " start")
        print("==================")
        isFound = os.path.exists(model_file_path + model.fileName)
        print("Is model binary found: " + str(isFound))
        predict_list = lib.prediction_mbert(model, model_file_path, ds.dataList)
        print("===")
        print("Record count: " + str(len(predict_list)))
        print("===")
        print(len(predict_list))
        lib.update_prediction_result_for_TestDS(predict_list, ds.tableName, model.colName)
        print("==================")
        print(model.modelName + " end")
        print("==================")


for model in xmlr_model_list:
    """
    For FB-XML-R family
    """
    for ds in dataset_list:
        print("==================")
        print(model.modelName + " start")
        print("==================")
        isFound = os.path.exists(model_file_path + model.fileName)
        print("Is model binary found: " + str(isFound))
        predict_list = lib.prediction_xlmr(model, model_file_path, ds.dataList)
        print("===")
        print("Record count: " + str(len(predict_list)))
        print("===")
        print(len(predict_list))
        lib.update_prediction_result_for_TestDS(predict_list, ds.tableName, model.colName)
        print("==================")
        print(model.modelName + " end")
        print("==================")

