import torch
from transformers import BertTokenizer, BertForSequenceClassification, AdamW
from torch.utils.data import DataLoader, TensorDataset
from torch.optim import Adam
from sklearn.model_selection import train_test_split
import time
from torchviz import make_dot
import os
import matplotlib.pyplot as plt

# For grahic
os.environ["PATH"] += os.pathsep + '/opt/homebrew/bin/'

NUM_CLASSES = 3

# Load BERT tokenizer and model
tokenizer = BertTokenizer.from_pretrained('bert-base-multilingual-uncased')
model = BertForSequenceClassification.from_pretrained('bert-base-multilingual-cased', num_labels=NUM_CLASSES)


# Print model architecture and details
print("Model architecture:")
print(model)

# Print model configuration
print("\nModel configuration:")
print(model.config)

# Example data
texts = ["Example sentence 1", "Example sentence 2", "Example sentence 3","Example sentence 1", "Example sentence 2", "Example sentence 3"]
labels = [0, 1, 2,0, 1, 2]  # Assuming three classes for simplicity

# Tokenize input texts
tokenized_inputs = tokenizer(texts, padding=True, truncation=True, return_tensors="pt")

# Build dataset and dataloader
input_ids = tokenized_inputs["input_ids"]
attention_mask = tokenized_inputs["attention_mask"]
labels = torch.tensor(labels)

dataset = TensorDataset(input_ids, attention_mask, labels)

train_dataset, val_dataset = train_test_split(dataset, test_size=0.2, random_state=42)

train_dataloader = DataLoader(train_dataset, batch_size=32, shuffle=True)
val_dataloader = DataLoader(val_dataset, batch_size=32)

# Build and train the model
optimizer = AdamW(model.parameters(), lr=3e-5)

# Use CrossEntropyLoss for multi-class classification
criterion = torch.nn.CrossEntropyLoss()

# Move model to GPU if available
device = torch.device("mps" if torch.backends.mps.is_available() else "cpu")
model.to(device)

# data for monitoring of the training process
epochsList = []
train_accuracyList = []
val_accuracyList = []
train_lossList = []
val_lossList = []


# Training loop
num_epochs = 3
for epoch in range(num_epochs):
    start_time = time.time()  # Record the start time for the epoch
    model.train()
    total_correct = 0
    total_samples = 0
    total_loss = 0.0

    for batch in train_dataloader:
        batch = tuple(t.to(device) for t in batch)
        inputs = {"input_ids": batch[0], "attention_mask": batch[1]}
        labels = batch[2].to(device)
        outputs = model(**inputs)
        logits = outputs.logits
        loss = criterion(logits, labels)
        total_loss += loss.item()

        _, predicted_labels = torch.max(logits, 1)
        total_correct += (predicted_labels == labels).sum().item()
        total_samples += labels.size(0)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

    accuracy = total_correct / total_samples
    avg_loss = total_loss / len(train_dataloader)
    print(f'Epoch {epoch + 1}/{num_epochs}, Training Loss: {avg_loss:.4f}, Training Accuracy: {accuracy:.4f}')

    # Validation
    model.eval()
    total_correct_val = 0
    total_samples_val = 0
    total_loss_val = 0.0

    with torch.no_grad():
        for batch in val_dataloader:
            batch = tuple(t.to(device) for t in batch)
            inputs = {"input_ids": batch[0], "attention_mask": batch[1]}
            labels = batch[2].to(device)
            outputs = model(**inputs)
            logits = outputs.logits
            loss = criterion(logits, labels)
            total_loss_val += loss.item()

            _, predicted_labels_val = torch.max(logits, 1)
            total_correct_val += (predicted_labels_val == labels).sum().item()
            total_samples_val += labels.size(0)

    accuracy_val = total_correct_val / total_samples_val
    avg_loss_val = total_loss_val / len(val_dataloader)

    # Calculate and print the time spent
    end_time = time.time()
    epoch_time = end_time - start_time

    print(f'Epoch {epoch + 1}/{num_epochs}, Time: {epoch_time:.2f}s, Validation Loss: {avg_loss_val:.4f}, Validation Accuracy: {accuracy_val:.4f}')


    # Keeping training info
    epochsList.append(epoch)
    train_accuracyList.append(accuracy)
    val_accuracyList.append(avg_loss)
    train_lossList.append(accuracy_val)
    val_lossList.append(avg_loss_val)


# Save the trained model if needed
torch.save(model.state_dict(), 'trained_bert_model.pth')


# Create a graph of the computation

inputs = None
for batch in val_dataloader:
    batch = tuple(t.to(device) for t in batch)
    inputs = {"input_ids": batch[0], "attention_mask": batch[1]}
    break
outputs = model(**inputs)
graph = make_dot(outputs.logits, params=dict(model.named_parameters()))

# Save the graph as an image (PNG)
graph.render(filename='bert_model', format='png', cleanup=True)



# Save the trained model if needed
torch.save(model.state_dict(), 'bert_model.pth')


# Generate graph
# Plotting accuracy
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.plot(epochsList, train_accuracyList, label='Training Accuracy', marker='o')
plt.plot(epochsList, val_accuracyList, label='Validation Accuracy', marker='o')
plt.title('Epoch vs Accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend()

# Plotting average loss
plt.subplot(1, 2, 2)
plt.plot(epochsList, train_lossList, label='Training Loss', marker='o')
plt.plot(epochsList, val_lossList, label='Validation Loss', marker='o')
plt.title('Epoch vs Average Loss')
plt.xlabel('Epoch')
plt.ylabel('Average Loss')
plt.legend()

plt.tight_layout()

# Save the figure to an image file (e.g., PNG)
plt.savefig('mBERT_training_graph.png')

# Show the plot (optional)
plt.show()
