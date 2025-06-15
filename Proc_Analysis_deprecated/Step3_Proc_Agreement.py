import Lib_analysis as lib
from Lib_analysis import Lang_Model

"""
This script is for checking agreement by kappa index between "pseudo label" with predicted label of the models for the 
tweets data.
"""

# 1. Get the pseudo-label list (ordered by id)
pseudo_label = lib.get_Label("pseudo_label")

# 2. Get the rest of the label lists
e_mBert_400_label_list = lib.get_Label(lib.COL_MBERT_ENG_400)
e_mBert_1600_label_list = lib.get_Label(lib.COL_MBERT_ENG_1600)
e_mBert_2800_label_list = lib.get_Label(lib.COL_MBERT_ENG_2800)
e_fbXLMr_400_label_list = lib.get_Label(lib.COL_XLMR_ENG_400)
e_fbXLMr_1600_label_list = lib.get_Label(lib.COL_XLMR_ENG_1600)
e_fbXLMr_2800_label_list = lib.get_Label(lib.COL_XLMR_ENG_2800)
m_mBert_400_label_list = lib.get_Label(lib.COL_MBERT_MUL_400)
m_mBert_1600_label_list = lib.get_Label(lib.COL_MBERT_MUL_1600)
m_mBert_2800_label_list = lib.get_Label(lib.COL_MBERT_MUL_2800)
m_fbXLMr_400_label_list = lib.get_Label(lib.COL_XLMR_MUL_400)
m_fbXLMr_1600_label_list = lib.get_Label(lib.COL_XLMR_MUL_1600)
m_fbXLMr_2800_label_list = lib.get_Label(lib.COL_XLMR_MUL_2800)

label_list = [
    pseudo_label,
    e_mBert_400_label_list,
    e_mBert_1600_label_list,
    e_mBert_2800_label_list,
    e_fbXLMr_400_label_list,
    e_fbXLMr_1600_label_list,
    e_fbXLMr_2800_label_list,
    m_mBert_400_label_list,
    m_mBert_1600_label_list,
    m_mBert_2800_label_list,
    m_fbXLMr_400_label_list,
    m_fbXLMr_1600_label_list,
    m_fbXLMr_2800_label_list
]

labelList = [
    "pseudo_label",
    "mBERT-400-E",
    "mBERT-1600-E",
    "mBERT-2800-E",
    "FB-XLM-R-400-E",
    "FB-XLM-R-1600-E",
    "FB-XLM-R-2800-E",
    "mBERT-400-M",
    "mBERT-1600-M",
    "mBERT-2800-M",
    "FB-XLM-R-400-M",
    "FB-XLM-R-1600-M",
    "FB-XLM-R-2800-M"
]

kappaScores = lib.calculate_Cohen_Kappa_Score(label_list)

lib.plotHeatMapKappaScore(kappaScores, label_list, labelList)
