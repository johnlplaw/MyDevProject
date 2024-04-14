import Variable as var
import pickle
import pandas as pd

def show_eng_df_info(size):
    file_name = var.FILE_TRAINING_ENG_NOS + str(size) + ".obj"
    fileObj = open(file_name, 'rb')
    df = pickle.load(fileObj)
    fileObj.close()
    print("-------------------------")
    print("File Name: " + file_name)
    print(type(df))
    print("Size: " + str(len(df)))
    emotionList = df[var.COLUMN_NAME_STD_LABEL].tolist()
    count = pd.Series(emotionList).value_counts()
    print("The number of the emotion:")
    print(count)
    print("-------------------------")

def show_multi_df_info(size):
    file_name = var.FILE_TRAINING_MUL_NOS + str(size) + ".obj"
    fileObj = open(file_name, 'rb')
    df = pickle.load(fileObj)
    fileObj.close()
    print("-------------------------")
    print("File Name: " + file_name)
    print(type(fileObj))

    print("Size: " + str(len(df)))
    emotionList = df[var.COLUMN_NAME_STD_LABEL].tolist()
    count = pd.Series(emotionList).value_counts()
    print("The number of the emotion:")
    print(count)
    print("The source type:")
    src_list = df[var.COLUMN_NAME_SRC_TYPE].tolist()
    count = pd.Series(src_list).value_counts()
    print(count)
    print("-------------------------")


print("====== English ======")
for size in var.sampling_size_list:
    print("Work on " + str(size))
    show_eng_df_info(size)

print("====== Multilingual ======")
for size in var.sampling_size_list:
    print("Work on " + str(size))
    show_multi_df_info(size)