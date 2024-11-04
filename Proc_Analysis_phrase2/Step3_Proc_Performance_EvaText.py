import Analysis_Lib as lib
from Analysis_Lib import Selected_Model

"""
This script is for evaluating the predicted label of the models for the evatest data against the "label" based on each labeling type.
"""
dsTypeList = ["chatgpt","multiLangComb_nos"]
labelingTypeList = ["la","pla","sla"]
tableName = "EvaText"
label = "label"

# 1. Get the Model Info
m_fbXLMr_gpt_lbl = Selected_Model("Final-FB-XLM-R_gpt_LBL_Multilingual_2800_1e-05_model.pth", "FB-XLM-R-gpt-lbl", lib.COL_GPT_LBL_XMLB)
m_fbXLMr_gpt_plbl = Selected_Model("Final-FB-XLM-R_gpt_PLBL_Multilingual_2800_1e-05_model.pth", "FB-XLM-R-gpt-plbl", lib.COL_GPT_PLBL_XMLB)
m_fbXLMr_gpt_slbl = Selected_Model("Final-FB-XLM-R_gpt_SLBL_Multilingual_2800_1e-05_model.pth","FB-XLM-R-gpt-slbl", lib.COL_GPT_SLBL_XMLB)
m_mBERT_gpt_lbl = Selected_Model("Final-mBERT_gpt_LBL_Multilingual_2800_1e-05_model.pth", "mBERT-gpt-lbl", lib.COL_GPT_LBL_MBERT)
m_mBERT_gpt_plbl = Selected_Model("Final-mBERT_gpt_PLBL_Multilingual_2800_1e-05_model.pth", "mBERT-gpt-plbl", lib.COL_GPT_PLBL_MBERT)
m_mBERT_gpt_slbl = Selected_Model("Final-mBERT_gpt_SLBL_Multilingual_2800_1e-05_model.pth","mBERT-gpt-slbl", lib.COL_GPT_SLBL_MBERT)

m_fbXLMr_syn_lbl = Selected_Model("Final-FB-XLM-R_LBL_Multilingual_2800_1e-05_model.pth","FB-XLM-R-syn-lbl", lib.COL_SYN_LBL_XMLB)
m_fbXLMr_syn_plbl = Selected_Model("Final-FB-XLM-R_PLBL_Multilingual_2800_1e-05_model.pth","FB-XLM-R-syn-plbl", lib.COL_SYN_PLBL_XMLB)
m_fbXLMr_syn_slbl = Selected_Model("Final-FB-XLM-R_SLBL_Multilingual_2800_1e-05_model.pth","FB-XLM-R-syn-slbl", lib.COL_SYN_SLBL_XMLB)


m_mBERT_syn_lbl = Selected_Model("Final-mBERT_LBL_Multilingual_2800_1e-05_model.pth", "mBERT-syn-lbl", lib.COL_SYN_LBL_MBERT)
m_mBERT_syn_plbl = Selected_Model("Final-mBERT_PLBL_Multilingual_2800_1e-05_model.pth","mBERT-syn-plbl", lib.COL_SYN_PLBL_MBERT)
m_mBERT_syn_slbl = Selected_Model("Final-mBERT_SLBL_Multilingual_2800_1e-05_model.pth","mBERT-syn-slbl", lib.COL_SYN_SLBL_MBERT)

e_fbXLMr_syn_lbl = Selected_Model("Final-FB-XLM-R_LBL_English_2800_1e-05_model.pth","FB-XLM-R-e-lbl", lib.COL_SYN_LBL_XMLB_E)
e_fbXLMr_syn_plbl = Selected_Model("Final-FB-XLM-R_PLBL_English_2800_1e-05_model.pth","FB-XLM-R-e-plbl", lib.COL_SYN_PLBL_XMLB_E)
e_fbXLMr_syn_slbl = Selected_Model("Final-FB-XLM-R_SLBL_English_2800_1e-05_model.pth","FB-XLM-R-e-slbl", lib.COL_SYN_SLBL_XMLB_E)

e_mBERT_syn_lbl = Selected_Model("Final-mBERT_LBL_English_2800_1e-05_model.pth", "mBERT-e-lbl", lib.COL_SYN_LBL_MBERT_E)
e_mBERT_syn_plbl = Selected_Model("Final-mBERT_PLBL_English_2800_1e-05_model.pth","mBERT-e-plbl", lib.COL_SYN_PLBL_MBERT_E)
e_mBERT_syn_slbl = Selected_Model("Final-mBERT_SLBL_English_2800_1e-05_model.pth","mBERT-e-slbl", lib.COL_SYN_SLBL_MBERT_E)

mbert_model_list = [m_mBERT_gpt_lbl, m_mBERT_gpt_plbl, m_mBERT_gpt_slbl, m_mBERT_syn_lbl, m_mBERT_syn_plbl, m_mBERT_syn_slbl, e_mBERT_syn_lbl, e_mBERT_syn_plbl, e_mBERT_syn_slbl]
xmlr_model_list = [m_fbXLMr_gpt_lbl, m_fbXLMr_gpt_plbl, m_fbXLMr_gpt_slbl, m_fbXLMr_syn_lbl, m_fbXLMr_syn_plbl, m_fbXLMr_syn_slbl, e_fbXLMr_syn_lbl, e_fbXLMr_syn_plbl, e_fbXLMr_syn_slbl]


for dsType in dsTypeList:
    for labelType in labelingTypeList:
        # 2. Get the label list
        labelList = lib.get_Label_List(tableName, label, dsType, labelType)
        for model in mbert_model_list:
            print("DatasetType: " + dsType + ", LabelType:" + labelType)
            print("Working on: " + model.modelName + " ... start")

            predicted_label = lib.get_Label_List(tableName, model.colName, dsType, labelType)
            print(len(labelList))
            print(len(predicted_label))
            lib.analysis_compare(model.modelName, labelList, predicted_label, lib.LabelList, "on_"+dsType+"_"+labelType)

            print("DatasetType: " + dsType + ", LabelType:" + labelType)
            print("Working on: " + model.modelName + " ... done")

        for model in xmlr_model_list:
            print("DatasetType: " + dsType + ", LabelType:" + labelType)
            print("Working on: " + model.modelName + " ... start")

            predicted_label = lib.get_Label_List(tableName, model.colName, dsType, labelType)
            print(len(labelList))
            print(len(predicted_label))
            lib.analysis_compare(model.modelName, labelList, predicted_label, lib.LabelList, "on_"+dsType+"_"+labelType)

            print("DatasetType: " + dsType + ", LabelType:" + labelType)
            print("Working on: " + model.modelName + " ... done")

#
# # 1. Get the pseudo-label list (ordered by id)
# pseudo_label_list = lib.get_Label("pseudo_label")
#
# # 2. Get the model info
# e_mBert_400 = Lang_Model("mBERT-400-E", lib.COL_MBERT_ENG_400)
# e_mBert_1600 = Lang_Model("mBERT-1600-E", lib.COL_MBERT_ENG_1600)
# e_mBert_2800 = Lang_Model("mBERT-2800-E", lib.COL_MBERT_ENG_2800)
# e_fbXLMr_400 = Lang_Model("FB-XLM-R-400-E", lib.COL_XLMR_ENG_400)
# e_fbXLMr_1600 = Lang_Model("FB-XLM-R-1600-E", lib.COL_XLMR_ENG_1600)
# e_fbXLMr_2800 = Lang_Model("FB-XLM-R-2800-E", lib.COL_XLMR_ENG_2800)
# m_mBert_400 = Lang_Model("mBERT-400-M", lib.COL_MBERT_MUL_400)
# m_mBert_1600 = Lang_Model("mBERT-1600-M", lib.COL_MBERT_MUL_1600)
# m_mBert_2800 = Lang_Model("mBERT-2800-M", lib.COL_MBERT_MUL_2800)
# m_fbXLMr_400 = Lang_Model("FB-XLM-R-400-M", lib.COL_XLMR_MUL_400)
# m_fbXLMr_1600 = Lang_Model("FB-XLM-R-1600-M", lib.COL_XLMR_MUL_1600)
# m_fbXLMr_2800 = Lang_Model("FB-XLM-R-2800-M", lib.COL_XLMR_MUL_2800)
#
# mbert_model_list = [e_mBert_400, e_mBert_1600, e_mBert_2800, m_mBert_400, m_mBert_1600, m_mBert_2800]
# xmlr_model_list = [e_fbXLMr_400, e_fbXLMr_1600, e_fbXLMr_2800, m_fbXLMr_400, m_fbXLMr_1600, m_fbXLMr_2800]
#
# # xmlr_model_list = [m_fbXLMr_2800]
#
# for model in mbert_model_list:
#     print("Working on: " + model.modelName + " ... start")
#     predicted_label = lib.get_Label(model.colName)
#     lib.analysis_compare(model.modelName, pseudo_label_list, predicted_label, lib.LabelList, "")
#     print("Working on: " + model.modelName + " ... done")
#
# for model in xmlr_model_list:
#     print("Working on: " + model.modelName + " ... start")
#     predicted_label = lib.get_Label(model.colName)
#     lib.analysis_compare(model.modelName, pseudo_label_list, predicted_label, lib.LabelList, "")
#     print("Working on: " + model.modelName + " ... done")
