import pickle

import CommonLib as lib
import DsLib as dslib
import CommonLib as lib
import DsLib as dslib
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC
from sklearn.naive_bayes import MultinomialNB
from sklearn.ensemble import RandomForestClassifier
#import xgboost as xgb
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report

output = "./RecordedResult/"
def main_training(size, lbltype):
    # Step 1: Preparing the data
    # textList, labelList = lib.prepre_texts()
    # textList, labelList = dslib.getDataLists(2800)
    textList, labelList = dslib.getDataLists(size, lbltype)

    # Step 2: Preprocessing the data
    textList = [lib.preprocess(t) for t in textList]

    # Step 3: Convert Text to TF-IDF Vectors
    X = lib.convertToTfIdfVector(textList)

    # Step 4: Preparing the training and testing datasets

    X_train, X_test, y_train, y_test = lib.prepareTrainingTestingDataset(X, labelList)

    # Step 5: Training the model
    modelList = [LogisticRegression(max_iter=1000),
                 LinearSVC(),
                 MultinomialNB(),
                 RandomForestClassifier(n_estimators=100),
                 # xgb.XGBClassifier(use_label_encoder=False, eval_metric='mlogloss'),
                 KNeighborsClassifier(n_neighbors=3),
                 DecisionTreeClassifier()]

    for m in modelList:
        m.fit(X_train, y_train)
        y_pred = m.predict(X_test)  # or svm_clf.predict(X_test)
        print("+++++++++++++++++++++++++++++")
        print("Working on Model: " + str(m) + ", Size: " + str(size) + ", label Type: " + lbltype)
        print(classification_report(y_test, y_pred))
        print("+++++++++++++++++++++++++++++")

        # Save model
        with open(output + str(m)[:str(m).find("(")] + "_" + str(size) + "_" + lbltype +'_Eng_Sync.pkl', 'wb') as f:
            pickle.dump(m, f)

lblTypeList = ["lbl", "plbl", "slbl"]
sizeList = [400, 1600, 2800]

for size in sizeList:
    for lbltype in lblTypeList:
        main_training(size, lbltype)


