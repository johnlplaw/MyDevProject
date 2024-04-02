from transformers import BertTokenizer, BertForSequenceClassification
import PTM_lib as ptm
import pickle
from sklearn.preprocessing import LabelEncoder
import pandas as pd
import random
import Variable as var

# 1. Load the dataset
combineDF = ptm.get_subset_combine_dataset(var.SAMPLING_TYPE_UNDER, sample_count=6000)

training_txt = combineDF['cleanedtxt'].tolist()
training_label = combineDF['std_label'].tolist()
training_label = [int(i) for i in training_label]

print('Len of the training dataset')
print(len(training_label))

# save to a physical file
fileObj = open(var.FILE_CROSSLINGUAL_UNDERSAMPLING_DF, 'wb')
pickle.dump(combineDF, fileObj)
fileObj.close()