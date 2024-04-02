# This is for standardise the variable name and values.

# OUTPUT DIR
DIR_OUTPUT = "output/"

# File name for datasets - start
FILE_OVERSAMPLING_ENG_TEXT_DATASET = DIR_OUTPUT + "Dataset_engdb_txt_over.obj"
FILE_OVERSAMPLING_ENG_LABEL_DATASET = DIR_OUTPUT + "Dataset_engdb_label_over.obj"
FILE_OVERSAMPLING_MULTI_TEXT_DATASET = DIR_OUTPUT + "Dataset_multiLang_txt_over.obj"
FILE_OVERSAMPLING_MULTI_LABEL_DATASET = DIR_OUTPUT + "Dataset_multiLang_label_over.obj"
FILE_OVERSAMPLING_MULTICOMB_TEXT_DATASET = DIR_OUTPUT + "Dataset_multiLangComb_txt_over.obj"
FILE_OVERSAMPLING_MULTICOMB_LABEL_DATASET = DIR_OUTPUT + "Dataset_multiLangComb_label_over.obj"

FILE_UNDERSAMPLING_ENG_TEXT_DATASET = DIR_OUTPUT + "Dataset_engdb_txt_under.obj"
FILE_UNDERSAMPLING_ENG_LABEL_DATASET = DIR_OUTPUT + "Dataset_engdb_label_under.obj"
FILE_UNDERSAMPLING_MULTI_TEXT_DATASET = DIR_OUTPUT + "Dataset_multiLang_txt_under.obj"
FILE_UNDERSAMPLING_MULTI_LABEL_DATASET = DIR_OUTPUT + "Dataset_multiLang_label_under.obj"
FILE_UNDERSAMPLING_MULTICOMB_TEXT_DATASET = DIR_OUTPUT + "Dataset_multiLangComb_txt_under.obj"
FILE_UNDERSAMPLING_MULTICOMB_LABEL_DATASET = DIR_OUTPUT + "Dataset_multiLangComb_label_under.obj"

FILE_NOSAMPLING_ENG_TEXT_DATASET = DIR_OUTPUT + "Dataset_engdb_txt_nos.obj"
FILE_NOSAMPLING_ENG_LABEL_DATASET = DIR_OUTPUT + "Dataset_engdb_label_nos.obj"
FILE_NOSAMPLING_MULTI_TEXT_DATASET = DIR_OUTPUT + "Dataset_multiLang_txt_nos.obj"
FILE_NOSAMPLING_MULTI_LABEL_DATASET = DIR_OUTPUT + "Dataset_multiLang_label_nos.obj"
FILE_NOSAMPLING_MULTICOMB_TEXT_DATASET = DIR_OUTPUT + "Dataset_multiLangComb_txt_nos.obj"
FILE_NOSAMPLING_MULTICOMB_LABEL_DATASET = DIR_OUTPUT + "Dataset_multiLangComb_label_nos.obj"
# File name for datasets - end

FILE_MULTICOMB_DF = DIR_OUTPUT + "DataFrame_multiLangComb_nos_resampling_"
FILE_TRAINING_ENG_NOS = DIR_OUTPUT + "DataFrame_training_eng_nos_"
FILE_TRAINING_MUL_NOS = DIR_OUTPUT + "DataFrame_training_multi_nos_"

EMOTION_LABEL_NEUTRAL_CODE = 0
EMOTION_LABEL_HAPPY_CODE = 1
EMOTION_LABEL_FEAR_CODE = 2
EMOTION_LABEL_SURPRISE_CODE = 3
EMOTION_LABEL_ANGRY_CODE = 4
EMOTION_LABEL_SAD_CODE = 5

EMOTION_LABEL_NEUTRAL = 'Neutral'
EMOTION_LABEL_HAPPY = 'Happy'
EMOTION_LABEL_FEAR = 'Fear'
EMOTION_LABEL_SURPRISE = 'Surprise'
EMOTION_LABEL_ANGRY = 'Angry'
EMOTION_LABEL_SAD = 'Sad'

Label_Desc_Code = {
    EMOTION_LABEL_NEUTRAL: EMOTION_LABEL_NEUTRAL_CODE,
    EMOTION_LABEL_HAPPY: EMOTION_LABEL_HAPPY_CODE,
    EMOTION_LABEL_FEAR: EMOTION_LABEL_FEAR_CODE,
    EMOTION_LABEL_SURPRISE: EMOTION_LABEL_SURPRISE_CODE,
    EMOTION_LABEL_ANGRY: EMOTION_LABEL_ANGRY_CODE,
    EMOTION_LABEL_SAD: EMOTION_LABEL_SAD_CODE
}

Label_Code_Desc = {
    EMOTION_LABEL_NEUTRAL_CODE: EMOTION_LABEL_NEUTRAL,
    EMOTION_LABEL_HAPPY_CODE: EMOTION_LABEL_HAPPY,
    EMOTION_LABEL_FEAR_CODE: EMOTION_LABEL_FEAR,
    EMOTION_LABEL_SURPRISE_CODE: EMOTION_LABEL_SURPRISE,
    EMOTION_LABEL_ANGRY_CODE: EMOTION_LABEL_ANGRY,
    EMOTION_LABEL_SAD_CODE: EMOTION_LABEL_SAD
}



FILE_CROSSLINGUAL_UNDERSAMPLING_DF = 'DF_crosslingual_under.obj'
FILE_CROSSLINGUAL_OVERSAMPLING_DF = 'DF_crosslingual_over.obj'

language_type = [
        'cleanedtxt',
        'translate_chn',
        'translate_my',
        'translate_tm',
        'cm_en_chn',
        'cm_en_my',
        'cm_en_tm',
        'cm_chn_en',
        'cm_chn_my',
        'cm_chn_tm',
        'cm_my_en',
        'cm_my_chn',
        'cm_my_tm',
        'cm_tm_en',
        'cm_tm_chn',
        'cm_tm_my',
        'cw_en_chn',
        'cw_en_my',
        'cw_en_tm',
        'cw_chn_en',
        'cw_chn_my',
        'cw_chn_tm',
        'cw_my_en',
        'cw_my_chn',
        'cw_my_tm',
        'cw_tm_en',
        'cw_tm_chn',
        'cw_tm_my'
]
COLUMN_NAME_STD_LABEL = 'std_label'
COLUMN_NAME_MULTI_LANG_TXT = 'multilang_text'
COLUMN_NAME_SRC_TYPE = 'src_type'
COLUMN_NAME_ENG_TXT = 'cleanedtxt'

# Sampling data
SAMPLING_400 = 400
SAMPLING_800 = 800
SAMPLING_1200 = 1200
SAMPLING_1600 = 1600
SAMPLING_2000 = 2000
SAMPLING_2400 = 2400
SAMPLING_2800 = 2800

sampling_size_list = [SAMPLING_400, SAMPLING_800, SAMPLING_1200, SAMPLING_1600, SAMPLING_2000, SAMPLING_2400, SAMPLING_2800]

# Model Name
MODEL_MBERT = 'mBERT'
MODEL_XMLR = 'XML-R'


# Language Type
LANG_TYPE_ENG = 'English'
LANG_TYPE_MULTI = 'Multilingual'
LANG_TYPE_COMBINED_MULTI = 'Combined'

# Sampling type
SAMPLING_TYPE_OVER = 'Over'
SAMPLING_TYPE_UNDER = 'Under'
SAMPLING_TYPE_ORI = 'ori'

