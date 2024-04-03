from transformers import BertTokenizer, BertForSequenceClassification
import PTM_lib as ptm
import pickle
from sklearn.preprocessing import LabelEncoder
import pandas as pd
import random

# Configuration for training
NUM_CLASSES = 6
num_epochs = 20
BATCH_SIZE = 8
#LEARNING_RATE = 3e-4 #0.0003
LEARNING_RATE = 3e-5 #0.00003

fileObj = open('backup/engdb_txt.obj', 'rb')
engdb_txt_1 = pickle.load(fileObj)
fileObj.close()
fileObj = open('backup/engdb_label.obj', 'rb')
engdb_label_1 = pickle.load(fileObj)
fileObj.close()

# Initialize LabelEncoder
label_encoder = LabelEncoder()

# Fit label encoder and transform labels to numeric values
numeric_labels = label_encoder.fit_transform(engdb_label_1)

# Convert numerical labels back to actual labels (for prediction)
# original_labels = label_encoder.inverse_transform(numeric_labels)

fileObj = open('numeric_labels_mBERT_en.obj', 'wb')
pickle.dump(numeric_labels,fileObj)
fileObj.close()

df = pd.DataFrame({'Text': engdb_txt_1, 'Label': numeric_labels})
# Set random seed for reproducibility
random.seed(42)
# Randomly select 10 rows from the DataFrame
text_df = df.sample(n=3000)

txt = text_df['Text']
label = text_df['Label']

# Load BERT tokenizer and model
model_name = "bert-base-multilingual-uncased"
tokenizer = BertTokenizer.from_pretrained(model_name)
model = BertForSequenceClassification.from_pretrained(model_name, num_labels=NUM_CLASSES)

ptm.Main_trainingModel("mBERT_en_cased", tokenizer, model, txt.tolist(), label.tolist(), BATCH_SIZE, LEARNING_RATE, num_epochs)

# model_name = "xlm-roberta-base"
# tokenizer = XLMRobertaTokenizer.from_pretrained(model_name)
# model = XLMRobertaForSequenceClassification.from_pretrained(model_name, num_labels=NUM_CLASSES)
#
# ptm.Main_trainingModel("xlmR", tokenizer, model, texts, labels)