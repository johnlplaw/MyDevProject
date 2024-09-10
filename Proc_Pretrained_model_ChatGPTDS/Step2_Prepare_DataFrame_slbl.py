import commons.DataClass.Variable as var
import pickle
import pandas as pd
import os
from imblearn.over_sampling import RandomOverSampler

# Step 1: Load the list of the ChatGPT generated text
fileName = var.FILE_NOSAMPLING_CHATGPT_TEXT_DATASET
print(fileName)

isExist = os.path.exists(fileName)
print(isExist)

fileObj = open(fileName, 'rb')
ChatGPTTextList = pickle.load(fileObj)
fileObj.close()

# Step 2: Build a dataframe

# Generate the list

textList = []
labelList = []
plabelList = []

for obj in ChatGPTTextList:
    # filter the same label
    if obj.label == obj.pseudoLabel:
        textList.append(obj.text)
        labelList.append(obj.label)
        plabelList.append(obj.pseudoLabel)

dict = {
    'txt': textList,
    'slabel': labelList,

}

df = pd.DataFrame(dict)

print(df.head(5))


sampling_class_size = [var.SAMPLING_400, var.SAMPLING_1600, var.SAMPLING_2800]
emotion_list = list(var.Label_Code_Desc.keys())

label = 'slabel'

for sampling_size in sampling_class_size:

    # create empty dataframe with the column names
    columnsList = [label]
    sampling_df = pd.DataFrame(columns=columnsList)
    print("Working on: " + str(sampling_size))

    # Working on each column
    for emotion in emotion_list:
        print("  Working on: " + var.Label_Code_Desc.get(emotion))
        filtered_df = df[df[label] == var.Label_Code_Desc.get(emotion)]
        print(filtered_df.head(5))
        if len(filtered_df) > sampling_size:
            subSample_size = sampling_size
        else:
            subSample_size = len(filtered_df)

        selected_df = filtered_df.sample(n=subSample_size)
        sampling_df = pd.concat([sampling_df, selected_df], ignore_index=True)

    print(sampling_df)

    # Start to do sampling
    X_train = sampling_df.drop(label, axis=1)
    y_train = sampling_df[label].tolist()
    oversampler = RandomOverSampler(random_state=42)

    X_train_resampled, y_train_resampled = oversampler.fit_resample(X_train, y_train)

    resampled_df = pd.DataFrame(X_train_resampled, columns=X_train.columns)
    resampled_df['std_label'] = y_train_resampled

    print(resampled_df.head(5))

    file_name = var.FILE_CHATGPT_DF + str(sampling_size) + "_" + label + ".obj"
    fileObj = open(file_name, 'wb')
    pickle.dump(sampling_df, fileObj)
    fileObj.close()


# Step 3: Check the dataset

for sampling_size in sampling_class_size:
    file_name = var.FILE_CHATGPT_DF + str(sampling_size) + "_" + label + ".obj"
    fileObj = open(file_name, 'rb')
    sampling_df = pickle.load(fileObj)
    fileObj.close()
    print("=========================")
    print(sampling_df.head(5))
    print(len(sampling_df))
    print("=========================")