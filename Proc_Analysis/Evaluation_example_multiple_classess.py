from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score, classification_report, roc_curve, auc
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from itertools import cycle
from sklearn.preprocessing import LabelEncoder

def analysis_compare (model_name, y_true_multi, y_pred_multi):
    # Calculate confusion matrix
    conf_matrix_multi = confusion_matrix(y_true_multi, y_pred_multi)

    # Calculate evaluation metrics
    accuracy_multi = accuracy_score(y_true_multi, y_pred_multi)
    precision_micro = precision_score(y_true_multi, y_pred_multi, average='micro')
    recall_micro = recall_score(y_true_multi, y_pred_multi, average='micro')
    f1_micro = f1_score(y_true_multi, y_pred_multi, average='micro')

    precision_macro = precision_score(y_true_multi, y_pred_multi, average='macro')
    recall_macro = recall_score(y_true_multi, y_pred_multi, average='macro')
    f1_macro = f1_score(y_true_multi, y_pred_multi, average='macro')

    # Print evaluation metrics
    print("Confusion Matrix:")
    print(conf_matrix_multi)
    print("Accuracy:", accuracy_multi)
    print("Precision (Micro):", precision_micro)
    print("Recall (Micro):", recall_micro)
    print("F1-score (Micro):", f1_micro)
    print("Precision (Macro):", precision_macro)
    print("Recall (Macro):", recall_macro)
    print("F1-score (Macro):", f1_macro)

    # Classification report
    print("Classification Report:")
    print(classification_report(y_true_multi, y_pred_multi))


    # Plot confusion matrix
    plt.figure(figsize=(8, 6))
    sns.heatmap(conf_matrix_multi, annot=True, fmt='d', cmap='Blues', cbar=False, square=True)
    plt.xlabel('Predicted Labels')
    plt.ylabel('True Labels')
    plt.title('Confusion Matrix')
    # Save the plotted graph
    plt.savefig(model_name + '_conf_matrix_multi.png')



    # Compute ROC curve and ROC area for each class

    # Encode labels into numerical representations
    label_encoder = LabelEncoder()
    y_true_encoded = label_encoder.fit_transform(y_true_multi)
    y_pred_encoded = label_encoder.transform(y_pred_multi)

    # Compute ROC curve and ROC area for each class
    fpr = dict()
    tpr = dict()
    roc_auc = dict()
    n_classes = len(np.unique(y_true_encoded))

    for i in range(n_classes):
        y_true_binary = np.array([1 if label == i else 0 for label in y_true_encoded])
        y_pred_binary = np.array([1 if label == i else 0 for label in y_pred_encoded])
        fpr[i], tpr[i], _ = roc_curve(y_true_binary, y_pred_binary)
        roc_auc[i] = auc(fpr[i], tpr[i])

    # Plot ROC curve for each class
    plt.figure()
    lw = 2
    colors = ['aqua', 'darkorange', 'cornflowerblue']
    for i, color in zip(range(n_classes), colors):
        plt.plot(fpr[i], tpr[i], color=color, lw=lw,
                 label='ROC curve of class {0} (area = {1:0.2f})'
                 ''.format(i, roc_auc[i]))

    plt.plot([0, 1], [0, 1], color='navy', lw=lw, linestyle='--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('ROC Curve for Multi-class Classification')
    plt.legend(loc="lower right")
    #plt.show()

    # Save the plotted graph
    plt.savefig(model_name + '_roc_curve.png')

    # Example of reversing label encoding
    y_true_decoded = label_encoder.inverse_transform(y_true_encoded)
    y_pred_decoded = label_encoder.inverse_transform(y_pred_encoded)
    print("Original non-numeric labels (ground truth):", y_true_multi)
    print("Decoded non-numeric labels (ground truth):", y_true_encoded)
    print("Decoded non-numeric labels (ground truth):", y_true_decoded)
    print("Original non-numeric labels (predictions):", y_pred_multi)
    print("Decoded non-numeric labels (predictions):", y_pred_encoded)
    print("Decoded non-numeric labels (predictions):", y_pred_decoded)

# Generate example ground truth and predictions for multi-class classification
y_true_multi = np.array(["A", "B", "C", "B", "A", "C", "B", "A", "C", "B"])  # Example ground truth
y_pred_multi = np.array(["A", "B", "C", "B", "A", "A", "B", "C", "C", "B"])  # Example predictions

analysis_compare("TestModel", y_true_multi, y_pred_multi)
