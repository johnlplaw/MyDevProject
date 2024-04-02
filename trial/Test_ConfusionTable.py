import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix

# Example true and predicted labels
y_true = ["A", "B", "A", "C", "B", "C", "A", "C"]
y_pred = ["A", "B", "A", "C", "C", "B", "A", "C"]

# Get the unique class labels
classes = np.unique(y_true)

# Calculate confusion matrix
conf_matrix = confusion_matrix(y_true, y_pred, labels=classes)

# Plot confusion matrix
plt.figure(figsize=(8, 6))
sns.heatmap(conf_matrix, annot=True, cmap='Blues', fmt='g')

# Add labels to the plot
tick_marks = np.arange(len(classes))
plt.xticks(tick_marks, classes, rotation=45)
plt.yticks(tick_marks, classes)
plt.xlabel('Predicted Labels')
plt.ylabel('True Labels')
plt.title('Confusion Matrix')

plt.show()