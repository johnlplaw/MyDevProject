import Lib_analysis as lib
from Lib_analysis import Lang_Model

"""
This script is for evaluating the predicted label of the models for the testing data against the "pseudo label".
"""

# 1. Get the pseudo-label list (ordered by id)
pseudo_eng_label_list = lib.get_Testing_Label("eva_eng_text", "pseudo_label")
pseudo_mul_label_list = lib.get_Testing_Label("eva_eng_text", "pseudo_label")

class PseudoLabel:

    def __init__(self, list, tableName, type):
        self.list = list
        self.tableName = tableName
        self.type = type

pseudoEngObj =  PseudoLabel(pseudo_eng_label_list, "eva_eng_text", "EngEva")
pseudoMulObj =  PseudoLabel(pseudo_eng_label_list, "eva_mul_text","MulEva")

pseudoList = [pseudoEngObj,pseudoMulObj]

# 2. Get the model info
e_mBert_400 = Lang_Model("mBERT-400-E", lib.COL_MBERT_ENG_400)
e_mBert_1600 = Lang_Model("mBERT-1600-E", lib.COL_MBERT_ENG_1600)
e_mBert_2800 = Lang_Model("mBERT-2800-E", lib.COL_MBERT_ENG_2800)
e_fbXLMr_400 = Lang_Model("FB-XLM-R-400-E", lib.COL_XLMR_ENG_400)
e_fbXLMr_1600 = Lang_Model("FB-XLM-R-1600-E", lib.COL_XLMR_ENG_1600)
e_fbXLMr_2800 = Lang_Model("FB-XLM-R-2800-E", lib.COL_XLMR_ENG_2800)
m_mBert_400 = Lang_Model("mBERT-400-M", lib.COL_MBERT_MUL_400)
m_mBert_1600 = Lang_Model("mBERT-1600-M", lib.COL_MBERT_MUL_1600)
m_mBert_2800 = Lang_Model("mBERT-2800-M", lib.COL_MBERT_MUL_2800)
m_fbXLMr_400 = Lang_Model("FB-XLM-R-400-M", lib.COL_XLMR_MUL_400)
m_fbXLMr_1600 = Lang_Model("FB-XLM-R-1600-M", lib.COL_XLMR_MUL_1600)
m_fbXLMr_2800 = Lang_Model("FB-XLM-R-2800-M", lib.COL_XLMR_MUL_2800)

mbert_model_list = [e_mBert_400, e_mBert_1600, e_mBert_2800, m_mBert_400, m_mBert_1600, m_mBert_2800]
xmlr_model_list = [e_fbXLMr_400, e_fbXLMr_1600, e_fbXLMr_2800, m_fbXLMr_400, m_fbXLMr_1600, m_fbXLMr_2800]

# xmlr_model_list = [m_fbXLMr_2800]

for model in mbert_model_list:
    for pseusoLabelObj in pseudoList:
        print("Working on: " + model.modelName + " " + pseusoLabelObj.type+ "... start")
        predicted_label = lib.get_Testing_Label(pseusoLabelObj.tableName, model.colName)
        lib.analysis_compare(model.modelName, pseusoLabelObj.list, predicted_label, lib.LabelList, pseusoLabelObj.type)
        print("Working on: " + model.modelName + " " + pseusoLabelObj.type+ "... done")

for model in xmlr_model_list:
    for pseusoLabelObj in pseudoList:
        print("Working on: " + model.modelName + " " + pseusoLabelObj.type+ "... start")
        predicted_label = lib.get_Testing_Label(pseusoLabelObj.tableName, model.colName)
        lib.analysis_compare(model.modelName, pseusoLabelObj.list, predicted_label, lib.LabelList, pseusoLabelObj.type)
        print("Working on: " + model.modelName + " " + pseusoLabelObj.type+ "... done")
