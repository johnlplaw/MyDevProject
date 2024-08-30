from transformers import BertTokenizer, BertForSequenceClassification
import PTM_lib as ptm
import pickle
from sklearn.preprocessing import LabelEncoder
import pandas as pd
import random
import Variable as var

# Configuration for training
NUM_CLASSES = 6
num_epochs = 20
BATCH_SIZE = 8
LEARNING_RATE = 3e-5 #0.00003
NUMBER_OF_SAMPLE = 5
LANG_TYPE = var.LANG_TYPE_ENG
SAMPLING_TYPE = var.SAMPLING_TYPE_OVER

text, label = ptm.get_full_dataSet(var.LANG_TYPE_ENG, var.SAMPLING_TYPE_OVER)
label = [int(i) for i in label]

# df = pd.DataFrame({'Text': text, 'Label': label})
# # Set random seed for reproducibility
# random.seed(42)
# # Randomly select 10 rows from the DataFrame
# text_df = df.sample(n=NUMBER_OF_SAMPLE)
#
# print(text_df)
#
# txt = text_df['Text']
# label = text_df['Label']

# Load BERT tokenizer and model
model_name = "bert-base-multilingual-uncased"
tokenizer = BertTokenizer.from_pretrained(model_name)
model = BertForSequenceClassification.from_pretrained(model_name, num_labels=NUM_CLASSES)

# ptm.Main_trainingModel("mBERT_" + LANG_TYPE + '_' + SAMPLING_TYPE, tokenizer, model, txt.tolist(), label.tolist(), BATCH_SIZE, LEARNING_RATE, num_epochs)
ptm.Main_trainingModel("mBERT_" + LANG_TYPE + '_' + SAMPLING_TYPE, tokenizer, model, text, label, BATCH_SIZE, LEARNING_RATE, num_epochs)

# model_name = "xlm-roberta-base"
# tokenizer = XLMRobertaTokenizer.from_pretrained(model_name)
# model = XLMRobertaForSequenceClassification.from_pretrained(model_name, num_labels=NUM_CLASSES)
#
# ptm.Main_trainingModel("xlmR", tokenizer, model, texts, labels)