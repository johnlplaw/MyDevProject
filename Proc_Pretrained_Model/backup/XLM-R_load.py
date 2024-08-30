import torch
from transformers import XLMRobertaForSequenceClassification, XLMRobertaTokenizer, AdamW


# Define the number of labels for your classification task
num_labels = 3  # Adjust this based on your specific task

model_name = "xlm-roberta-base"
tokenizer = XLMRobertaTokenizer.from_pretrained(model_name)
model = XLMRobertaForSequenceClassification.from_pretrained(model_name, num_labels=num_labels)  # Adjust num_labels for your task

# Load the saved state dictionary into the model
model_path = "./trained_xlmr_model.pth"  # Path to the saved state dictionary file
state_dict = torch.load(model_path)
model.load_state_dict(state_dict)

# Set the model to evaluation mode
model.eval()

# Example text for classification
text = "I am feeling happy today."

# Tokenize input text
inputs = tokenizer(text, return_tensors='pt')

# Perform classification
with torch.no_grad():
    outputs = model(**inputs)

# Get predicted label (assuming binary classification)
predicted_label = torch.argmax(outputs.logits, dim=1).item()

# Print the predicted label
print("Predicted Label:", predicted_label)