from transformers import BertTokenizer, BertForSequenceClassification
import PTM_lib as ptm
import pickle
import Variable as var
import torch
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
LABELS=["0", "1", "2", "3", "4", "5"]

# 1. Load the dataset
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
model_name = "xlm-roberta-base"
tokenizer = XLMRobertaTokenizer.from_pretrained(model_name)
model = XLMRobertaForSequenceClassification.from_pretrained(model_name, num_labels=NUM_CLASSES)

# 4. Load the saved state dictionary into the model
model_path = "XLM-R" + '_' + LANG_TYPE + '_' + SAMPLING_TYPE + '_' + EXP_TYPE + '_model.pth'
state_dict = torch.load(model_path)
model.load_state_dict(state_dict)

# 5. Set the model to evaluation mode
model.eval()

# Evaluation
ptm.evaluation(combineDF, tokenizer, model, LABELS)
