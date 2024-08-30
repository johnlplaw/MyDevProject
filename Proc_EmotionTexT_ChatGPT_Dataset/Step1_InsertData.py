import os
import commons.mysql.mysqlHelper as sqlHelper

"""
This script is for inserting the texts gathered from ChatGPT into the database storage.
"""

def read_file_list(filePath):
    """
    Get the file list in a given path
    :param filePath: The given file path
    :return: The file list
    """
    file_list = os.listdir(filePath)
    return file_list


the_chatGpt_file_path = "Source_files"


def show_the_files_info(file_list):
    """
    Show the file info.
    :param file_list: The given file list
    :return: Nothing
    """
    for thefile in file_list:
        fileName, emotion, lang_type, language = get_files_info(thefile)

        print(thefile + ": " + emotion + " - " + lang_type + " - " + language)


def get_files_info(fileName):
    """
    Show the file info.
    :param file_list: The given file list
    :return: Nothing
    """
    fileSection = fileName.split("-")
    emotion = ""
    lang_type = ""
    language = ""
    if len(fileSection) == 2:
        # mono language
        emotion = fileSection[0]
        lang_type = "mono"
        language = fileSection[1]
    elif len(fileSection) == 4:
        # multi language
        emotion = fileSection[0]
        lang_type = fileSection[1]
        language = fileSection[2] + "-" + fileSection[3]

    return fileName, emotion, lang_type, language


class EmotionFileContent:
    def __init__(self, oriTxt, txtType, lang, label):
        self.oriTxt = oriTxt
        self.txtType = txtType
        self.lang = lang
        self.label = label


def read_the_file_content(the_chatGpt_file_path, file_list):
    the_result_list = []
    for thefile in file_list:
        if thefile.__eq__(".DS_Store"):
            continue
        fileName, emotion, lang_type, language = get_files_info(thefile)

        with open(the_chatGpt_file_path + "/" + thefile) as file:
            for line in file:
                line = line.strip()
                line = line.replace("\"", "")

                textObj = EmotionFileContent(line, lang_type, language, emotion)
                the_result_list.append(textObj)

    return the_result_list


def insert_data(theContentList):
    conn = sqlHelper.get_mysql_conn()
    mycursor = conn.cursor()
    sql = "INSERT INTO emotion_text (ori_text, text_type, lang, label) VALUES (%s, %s, %s, %s)"

    for content in theContentList:
        val = (content.oriTxt, content.txtType, content.lang, content.label)
        mycursor.execute(sql, val)

    conn.commit()
    print(mycursor.rowcount, "record inserted.")


# Step 1: Get the ChatGPT generated emotional text files
file_list = read_file_list(the_chatGpt_file_path)
# Step 2: Show the file info
show_the_files_info(file_list)
# Step 3: Read the file contents
theContentList = read_the_file_content(the_chatGpt_file_path, file_list)

insert_data(theContentList)