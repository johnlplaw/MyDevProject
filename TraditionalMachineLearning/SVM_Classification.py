import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report

# Sample data for demonstration
# Replace this with your actual dataset
corpus = ["I love machine learning", "I enjoy natural language processing", "This is a text classification example", "Support Vector Machines are powerful", "Support Vector Machines are powerful 2"]

labels = [1, 1, 0, 0, 0]  # Binary labels for each document (1 for positive, 0 for negative)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(corpus, labels, test_size=0.2, random_state=42)

# Create a TF-IDF vectorizer
vectorizer = TfidfVectorizer()

# Fit and transform the training data
X_train_tfidf = vectorizer.fit_transform(X_train)

# Transform the test data using the same vectorizer
X_test_tfidf = vectorizer.transform(X_test)

# Create and train an SVM classifier
svm_classifier = SVC(kernel='linear')  # You can choose different kernels (linear, rbf, etc.)
svm_classifier.fit(X_train_tfidf, y_train)

# Make predictions on the test set
predictions = svm_classifier.predict(X_test_tfidf)

# Evaluate the performance
accuracy = accuracy_score(y_test, predictions)
print("Accuracy:", accuracy)

classification_report_output = classification_report(y_test, predictions)
print("Classification Report:\n", classification_report_output)