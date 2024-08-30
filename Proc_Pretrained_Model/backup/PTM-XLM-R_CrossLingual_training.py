from transformers import BertTokenizer, BertForSequenceClassification
import PTM_lib as ptm
import pickle
from sklearn.preprocessing import LabelEncoder
import pandas as pd
import random
import Variable as var
from transformers import XLMRobertaForSequenceClassification, XLMRobertaTokenizer

# Configuration for training
NUM_CLASSES = 6
num_epochs = 20
BATCH_SIZE = 8
LEARNING_RATE = 3e-5 #0.00003
NUMBER_OF_SAMPLE = 5
LANG_TYPE = var.LANG_TYPE_ENG
SAMPLING_TYPE = var.SAMPLING_TYPE_OVER
EXP_TYPE = 'CrossLingual'

# 1. Load the dataset
# combineDF = ptm.get_combine_dataset(var.SAMPLING_TYPE_UNDER, sample_count=500)
fileObj = open(var.FILE_CROSSLINGUAL_DF, 'rb')
combineDF = pickle.load(fileObj)
fileObj.close()

# 2. Adjustment on the dataset
training_txt = combineDF['cleanedtxt'].tolist()
training_label = combineDF['std_label'].tolist()
training_label = [int(i) for i in training_label]

print('Len of the training dataset')
print(len(training_label))

# 3. Load BERT tokenizer and model
# model_name = "bert-base-multilingual-uncased"
# tokenizer = BertTokenizer.from_pretrained(model_name)
# model = BertForSequenceClassification.from_pretrained(model_name, num_labels=NUM_CLASSES)
# ptm.Main_trainingModel("mBERT_" + LANG_TYPE + '_' + SAMPLING_TYPE + '_' + EXP_TYPE, tokenizer, model, training_txt, training_label, BATCH_SIZE, LEARNING_RATE, num_epochs)

model_name = "xlm-roberta-base"
tokenizer = XLMRobertaTokenizer.from_pretrained(model_name)
model = XLMRobertaForSequenceClassification.from_pretrained(model_name, num_labels=NUM_CLASSES)
ptm.Main_trainingModel("XLM-R" + '_' + LANG_TYPE + '_' + SAMPLING_TYPE + '_' + EXP_TYPE, tokenizer, model, training_txt, training_label, BATCH_SIZE, LEARNING_RATE, num_epochs)