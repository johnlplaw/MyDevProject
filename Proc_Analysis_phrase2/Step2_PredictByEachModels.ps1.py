import Analysis_Lib as lib
import os.path

from Analysis_Lib import Selected_Model

"""
This script is for emotion prediction to be done by the models. The result of the prediction is updated in to the EVATEXT 
table.
"""

#1.  Get the texts to be predicted
data_list = lib.get_cleanned_ori_text()

# for txtData in data_list:
#     print(str(txtData.id) + " - " + txtData.clean_text)

#2. identify the selected model

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
m_mBERT_syn_plbl = Selected_Model("Final-mBERT_PLBL_Multilingual_2800_1e-05_model.pth","mBERT-syn-lbl", lib.COL_SYN_PLBL_MBERT)
m_mBERT_syn_slbl = Selected_Model("Final-mBERT_SLBL_Multilingual_2800_1e-05_model.pth","mBERT-syn-lbl", lib.COL_SYN_SLBL_MBERT)

e_fbXLMr_syn_lbl = Selected_Model("Final-FB-XLM-R_LBL_English_2800_1e-05_model.pth","FB-XLM-R-e-lbl", lib.COL_SYN_LBL_XMLB_E)
e_fbXLMr_syn_plbl = Selected_Model("Final-FB-XLM-R_PLBL_English_2800_1e-05_model.pth","FB-XLM-R-e-plbl", lib.COL_SYN_PLBL_XMLB_E)
e_fbXLMr_syn_slbl = Selected_Model("Final-FB-XLM-R_SLBL_English_2800_1e-05_model.pth","FB-XLM-R-e-slbl", lib.COL_SYN_SLBL_XMLB_E)

e_mBERT_syn_lbl = Selected_Model("Final-mBERT_LBL_English_2800_1e-05_model.pth", "mBERT-e-lbl", lib.COL_SYN_LBL_MBERT_E)
e_mBERT_syn_plbl = Selected_Model("Final-mBERT_PLBL_English_2800_1e-05_model.pth","mBERT-e-lbl", lib.COL_SYN_PLBL_MBERT_E)
e_mBERT_syn_slbl = Selected_Model("Final-mBERT_SLBL_English_2800_1e-05_model.pth","mBERT-e-lbl", lib.COL_SYN_SLBL_MBERT_E)

mbert_model_list = [m_mBERT_gpt_lbl, m_mBERT_gpt_plbl, m_mBERT_gpt_slbl, m_mBERT_syn_lbl, m_mBERT_syn_plbl, m_mBERT_syn_slbl, e_mBERT_syn_lbl, e_mBERT_syn_plbl, e_mBERT_syn_slbl]
xmlr_model_list = [m_fbXLMr_gpt_lbl, m_fbXLMr_gpt_plbl, m_fbXLMr_gpt_slbl, m_fbXLMr_syn_lbl, m_fbXLMr_syn_plbl, m_fbXLMr_syn_slbl, e_fbXLMr_syn_lbl, e_fbXLMr_syn_plbl, e_fbXLMr_syn_slbl]
model_file_path = "./models/"


for model in mbert_model_list:
    """
    For mBERT model family
    """

    print("==================")
    print(model.modelName + " start")
    print("==================")
    isFound = os.path.exists(model_file_path + model.fileName)
    print("Is model binary found: " + str(isFound))

    print("==================")
    print(model.modelName + " end")
    print("==================")


for model in xmlr_model_list:
    """
    For FB-XML-R family
    """

    print("==================")
    print(model.modelName + " start")
    print("==================")
    isFound = os.path.exists(model_file_path + model.fileName)
    print("Is model binary found: " + str(isFound))


    print("==================")
    print(model.modelName + " end")
    print("==================")

# #2. identify the selected model
# e_mBert_400 = Selected_Model("Final-mBERT_English_400_1e-05_model.pth", "mBERT-400", lib.COL_MBERT_ENG_400)
# e_mBert_1600 = Selected_Model("Final-mBERT_English_1600_1e-05_model.pth", "mBERT-1600", lib.COL_MBERT_ENG_1600)
# e_mBert_2800 = Selected_Model("Final-mBERT_English_2800_1e-05_model.pth", "mBERT-2800", lib.COL_MBERT_ENG_2800)
# e_fbXLMr_400 = Selected_Model("Final-FB-XLM-R_English_400_1e-05_model.pth", "FB-XLM-R-400", lib.COL_XLMR_ENG_400)
# e_fbXLMr_1600 = Selected_Model("Final-FB-XLM-R_English_1600_1e-05_model.pth", "FB-XLM-R-1600", lib.COL_XLMR_ENG_1600)
# e_fbXLMr_2800 = Selected_Model("Final-FB-XLM-R_English_2800_1e-05_model.pth", "FB-XLM-R-2800", lib.COL_XLMR_ENG_2800)
# m_mBert_400 = Selected_Model("Final-mBERT_Multilingual_400_1e-05_model.pth", "mBERT-400", lib.COL_MBERT_MUL_400)
# m_mBert_1600 = Selected_Model("Final-mBERT_Multilingual_1600_1e-05_model.pth", "mBERT-1600", lib.COL_MBERT_MUL_1600)
# m_mBert_2800 = Selected_Model("Final-mBERT_Multilingual_2800_1e-05_model.pth", "mBERT-2800", lib.COL_MBERT_MUL_2800)
# m_fbXLMr_400 = Selected_Model("Final-FB-XLM-R_Multilingual_400_1e-05_model.pth", "FB-XLM-R-400", lib.COL_XLMR_MUL_400)
# m_fbXLMr_1600 = Selected_Model("FInal-FB-XLM-R_Multilingual_1600_1e-05_model.pth", "FB-XLM-R-1600", lib.COL_XLMR_MUL_1600)
# m_fbXLMr_2800 = Selected_Model("Final-FB-XLM-R_Multilingual_2800_1e-05_model.pth", "FB-XLM-R-2800", lib.COL_XLMR_MUL_2800)
#
#
# mbert_model_list = [e_mBert_400, e_mBert_1600, e_mBert_2800, m_mBert_400, m_mBert_1600, m_mBert_2800]
# xmlr_model_list = [e_fbXLMr_400, e_fbXLMr_1600, e_fbXLMr_2800, m_fbXLMr_400, m_fbXLMr_1600, m_fbXLMr_2800]
# model_file_path = "../Proc_Pretrained_Model/output/"
#
# for model in mbert_model_list:
#     """
#     For mBERT model family
#     """
#
#     print("==================")
#     print(model.modelName + " start")
#     print("==================")
#     isFound = os.path.exists(model_file_path + model.fileName)
#     print("Is model binary found: " + str(isFound))
#     predict_list = lib.prediction_mbert(model, model_file_path, data_list)
#     print("===")
#     print("Record count: " + str(len(predict_list)))
#     print("===")
#
#     lib.update_prediction_result(predict_list, model.colName)
#     print("==================")
#     print(model.modelName + " end")
#     print("==================")
#
#
# for model in xmlr_model_list:
#     """
#     For FB-XML-R family
#     """
#
#     print("==================")
#     print(model.modelName + " start")
#     print("==================")
#     isFound = os.path.exists(model_file_path + model.fileName)
#     print("Is model binary found: " + str(isFound))
#     predict_list = lib.prediction_xlmr(model, model_file_path, data_list)
#     print("===")
#     print("Record count: " + str(len(predict_list)))
#     print("===")
#
#     lib.update_prediction_result(predict_list, model.colName)
#     print("==================")
#     print(model.modelName + " end")
#     print("==================")

