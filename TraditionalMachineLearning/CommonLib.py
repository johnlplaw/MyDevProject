import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

def prepre_texts():
    """
    Preparing the dataset
    :return: List of Texts and Lables
    """
    texts = ["I'm so happy today!", "This is terrible.", "I'm scared to talk."]
    labels = ["joy", "anger", "fear"]
    return texts, labels

def preprocess(text):
    """
    Prepapring the dataset
    :param text: The passing text
    :return: Cleaned text
    """
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)  # keep only letters
    return text

def convertToTfIdfVector(textsList):
    """

    :param textsList:
    :return:
    """
    vectorizer = TfidfVectorizer(max_features=5000, ngram_range=(1, 2))  # 1-grams and 2-grams
    X = vectorizer.fit_transform(textsList)
    return vectorizer, X

def prepareTrainingTestingDataset(vectorsList, labelsList):
    """
    Create the training and testing datasets
    :param vectorsList: The vectorised list
    :param labelsList: The label text
    :return: X_train, X_test, y_train, y_test
    """
    X_train, X_test, y_train, y_test = train_test_split(vectorsList, labelsList, test_size=0.2, random_state=42)
    return X_train, X_test, y_train, y_test