import pickle

import mysql
from sklearn.feature_extraction.text import TfidfVectorizer

import commons.mysql.mysqlHelper as sqlHelper

COL_DT_LBL = "DecisionTreeClassifier_lbl"
COL_KN_LBL = "KNeighborsClassifier_lbl"
COL_SVC_LBL = "LinearSVC_lbl"
COL_LR_LBL = "LogisticRegression_lbl"
COL_NB_LBL = "MultinomialNB_lbl"
COL_RF_LBL = "RandomForestClassifier_lbl"
COL_DT_GPT_LBL = "DecisionTreeClassifierGPT_lbl"
COL_KN_GPT_LBL = "KNeighborsClassifierGPT_lbl"
COL_SVC_GPT_LBL = "LinearSVCGPT_lbl"
COL_LR_GPT_LBL = "LogisticRegressionGPT_lbl"
COL_NB_GPT_LBL = "MultinomialNBGPT_lbl"
COL_RF_GPT_LBL = "RandomForestClassifierGPT_lbl"


COL_DT_PLBL = "DecisionTreeClassifier_plbl"
COL_KN_PLBL = "KNeighborsClassifier_plbl"
COL_SVC_PLBL = "LinearSVC_plbl"
COL_LR_PLBL = "LogisticRegression_plbl"
COL_NB_PLBL = "MultinomialNB_plbl"
COL_RF_PLBL = "RandomForestClassifier_plbl"
COL_DT_GPT_PLBL = "DecisionTreeClassifierGPT_plbl"
COL_KN_GPT_PLBL = "KNeighborsClassifierGPT_plbl"
COL_SVC_GPT_PLBL = "LinearSVCGPT_plbl"
COL_LR_GPT_PLBL = "LogisticRegressionGPT_plbl"
COL_NB_GPT_PLBL = "MultinomialNBGPT_plbl"
COL_RF_GPT_PLBL = "RandomForestClassifierGPT_plbl"

COL_DT_SLBL = "DecisionTreeClassifier_slbl"
COL_KN_SLBL = "KNeighborsClassifier_slbl"
COL_SVC_SLBL = "LinearSVC_slbl"
COL_LR_SLBL = "LogisticRegression_slbl"
COL_NB_SLBL = "MultinomialNB_slbl"
COL_RF_SLBL = "RandomForestClassifier_slbl"
COL_DT_GPT_SLBL = "DecisionTreeClassifierGPT_slbl"
COL_KN_GPT_SLBL = "KNeighborsClassifierGPT_slbl"
COL_SVC_GPT_SLBL = "LinearSVCGPT_slbl"
COL_LR_GPT_SLBL = "LogisticRegressionGPT_slbl"
COL_NB_GPT_SLBL = "MultinomialNBGPT_slbl"
COL_RF_GPT_SLBL = "RandomForestClassifierGPT_slbl"



class Selected_MLModel:
    """
    Model info.
    """
    def __init__(self, fileName, modelName, colName):
        self.fileName = fileName
        self.modelName = modelName
        self.colName = colName

class EvaTextMLData:
    id = "",
    thetext = "",
    label = "",
    dstype = "",
    labeltype = ""
    predictedLabel = ""

    def __init__(self, id, thetext, label, dstype, labeltype, predictedLabel):
        self.id = id
        self.thetext = thetext
        self.label = label
        self.dstype = dstype
        self.labeltype = labeltype
        self.predictedLabel = predictedLabel

    def toString(self):
        print(self.id + " / " +
        self.thetext + " / " +
        self.label + " / " +
        self.dstype + " / " +
        self.labeltype )



def get_cleanned_ori_text(tableName, colName):
    """
    Query the cleanned text info.
    :return:
    """

    print("Start to query ...")
    TextDataList = []
    try:
        conn = sqlHelper.get_mysql_conn()
        mycursor = conn.cursor()
        Select_sql = "select id, thetext, label, dstype, labeltype from " + tableName + " where " + colName + " is null"
        print(Select_sql)
        mycursor.execute(Select_sql)
        result = mycursor.fetchall()

        for i in result:
            id = i[0]
            thetext = i[1]
            label = i[2]
            dstype = i[3]
            labeltype = i[4]

            data = EvaTextMLData(id, thetext, label, dstype, labeltype, None)
            TextDataList.append(data)

        print("Finish query ...")
    except mysql.connector.Error as error:
        print("Failed to select record to database: {}".format(error))
    finally:
        if conn.is_connected():
            mycursor.close()
            conn.close()
            print("MySQL connection is closed")

    return TextDataList

def update_prediction_result(textDataList, tablename, colname):
    """
    Update the predicted result in the tweets table
    :param textDataList: The pass in text data list with predicted label
    :param colname: the column name to be updated
    :return: Nothing
    """
    try:
        conn = sqlHelper.get_mysql_conn()
        mycursor = conn.cursor()
        update_sql = "Update " + tablename + " set " + colname + "= %s where id = %s "

        values = []

        for textData in textDataList:
            tuppleData = (textData.predictedLabel, textData.id)
            values.append(tuppleData)

        # executemany() method
        mycursor.executemany(update_sql, values)
        # save changes
        conn.commit()

    except mysql.connector.Error as error:
        print("Failed to insert record to database: {}".format(error))
    finally:
        if conn.is_connected():
            mycursor.close()
            conn.close()
            print("MySQL connection is closed")

def convertToTfIdfVector(textsList):
    """

    :param textsList:
    :return:
    """
    vectorizer = TfidfVectorizer(max_features=5000, ngram_range=(1, 2))  # 1-grams and 2-grams
    X = vectorizer.fit_transform(textsList)
    return X

def predictionML(modelobj, fileDir, evaTxtMLData):
    filePath = fileDir + modelobj.fileName

    X_test = []
    for obj in evaTxtMLData:
        X_test.append(obj.thetext)

    X = convertToTfIdfVector(X_test)

    # Load model
    with open(filePath, 'rb') as f:
        loaded_model = pickle.load(f)
    y_pred = loaded_model.predict(X)

    for i in range(len(y_pred)):
        evaTxtMLData[i].predictedLabel = str(y_pred[i])

    return evaTxtMLData

def get_predicted_labels(tableName, colName, dstype, labeltype):
    """
    Query the cleanned text info.
    :return:
    """

    print("Start to query ...")
    TextDataList = []
    try:
        conn = sqlHelper.get_mysql_conn()
        mycursor = conn.cursor()
        Select_sql = "select id, thetext, label, dstype, labeltype, " + colName + " from " + tableName + " where dstype = '" + dstype + "' and labeltype = '" + labeltype + "'"
        print(Select_sql)
        mycursor.execute(Select_sql)
        result = mycursor.fetchall()

        for i in result:
            id = i[0]
            thetext = i[1]
            label = i[2]
            dstype = i[3]
            labeltype = i[4]
            predictedLabel = i[5]

            data = EvaTextMLData(id, thetext, label, dstype, labeltype, predictedLabel)
            TextDataList.append(data)

        print("Finish query ...")
    except mysql.connector.Error as error:
        print("Failed to select record to database: {}".format(error))
    finally:
        if conn.is_connected():
            mycursor.close()
            conn.close()
            print("MySQL connection is closed")

    return TextDataList