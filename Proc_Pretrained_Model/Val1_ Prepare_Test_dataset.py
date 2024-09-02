# This script is for preparing a dataset for validation of the best models for each language category.
# There is a 2800 dataset and use the random seed 42 to get the validation dataset from it.

import PTM_lib as ptm
import pickle
import Variable as var
from sklearn.model_selection import train_test_split

LANG_TYPE_LIST = [var.LANG_TYPE_ENG, var.LANG_TYPE_MULTI]
DATA_SIZE = var.SAMPLING_2800
OUTPUT_PATH = "./output/"
def load_df(lang, size):
    file_name = ptm.get_DF_LBL_file_path(lang, size)
    print("DataFrame file: " + file_name)
    fileObj = open(file_name, 'rb')
    df = pickle.load(fileObj)
    fileObj.close()
    return df

def generate_data(LANG_TYPE):
    df = load_df(LANG_TYPE, DATA_SIZE)
    print("Dataset size: " + str(len(df)))

    # Step2: Adjustment on the dataset
    training_txt = df[ptm.get_DF_column_name(LANG_TYPE)].tolist()
    training_label = df[var.COLUMN_NAME_STD_LABEL].tolist()
    training_label = [int(i) for i in training_label]
    print(training_txt[0:10])

    train_dataset, val_dataset = train_test_split(df, test_size=0.2, random_state=42)

    print(len(train_dataset))
    print(len(val_dataset))

    file_name = "Val_DS_" + LANG_TYPE + "_" + str(DATA_SIZE) + ".obj"
    fileObj = open(OUTPUT_PATH + file_name, 'wb')
    pickle.dump(val_dataset, fileObj)
    fileObj.close()

for LANG_TYPE in LANG_TYPE_LIST:
    # Loading the 2 language types
    generate_data(LANG_TYPE)