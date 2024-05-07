from transformers import BertTokenizer, BertForSequenceClassification
import pickle
import torch
from transformers import XLMRobertaForSequenceClassification, XLMRobertaTokenizer
import Lib_analysis as lib

# Get the texts to be predicted
data_list = lib.get_cleanned_ori_text()

# Prepare the model, tokenizer
print("Prepare model and tokenizer ... start")
model, tokenizer = lib.prepare_model_mBERT_Eng()
print("Prepare model and tokenizer ... end")

# Load the model
print("Load model ... start")
model_path = "./selected_models/mBERT_English_2800_ori_RO3_Batch_8_model.pth"
state_dict = torch.load(model_path)
model.load_state_dict(state_dict)
print("Load model ... end")

# 5. Set the model to evaluation mode
model.eval()

# 6. Predictin process
predicted_datalist = lib.evaluation(data_list, tokenizer, model)

same_pseudo_predicted = 0
for disp in predicted_datalist:
    if disp.pseudo_label == lib.Label_Code_Desc[disp.predicted_label] :
        same_pseudo_predicted = same_pseudo_predicted + 1
    print(str(disp.id) + " / " + disp.clean_text + " / " + disp.pseudo_label + " / " +  str(lib.Label_Code_Desc[disp.predicted_label]))

print(same_pseudo_predicted)

