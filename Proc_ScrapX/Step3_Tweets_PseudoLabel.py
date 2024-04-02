import commons.lang.CleanText as ct
import commons.webscrapping.scrapping as sc
import commons.mysql.mysqlHelper as sqlHelper
import mysql.connector
from translate_shell.translate import translate
import commons.emotion.identifyEmotion as emo
import time

shortform_csv_path = "../data/kamus_singkatan2.csv"

def light_clean(input, BM_shortfform_list):
    # not include the stop word and punctuation removal since they still have impact to the BERT
    txt = ct.removebStr(input)
    txt = ct.removeURL(txt)
    txt = ct.remove_a_tag(txt)
    txt = ct.remove_html_tag(txt)
    txt = ct.removeWordStarsWithChar(txt)
    txt = ct.transform_emojis_into_char(txt)
    txt = ct.removeChar(txt)

    txt = ct.remove_repeated_char(txt)
    txt = ct.remove_redundant_space(txt)

    txt = ct.replaceChar(txt)
    txt = ct.toLowerCase(txt)
    txt = ct.replace_numeric_with_symbol(txt)

    txt = ct.replace_malay_shortform(txt, BM_shortfform_list)

    # txt = ct.spelling_correction(txt)
    # txt = ct.remove_hashWord(txt)
    return txt



class tweetsData:
    id = ""
    tweet = ""

    def __init__(self, id, tweet):
        self.id = id
        self.tweet = tweet

    def __str__(self):
        return str(self.id) + " | " + self.tweet


class ProcessedTweetsData:
    id = ""
    clean_text = ""
    In_english = ""
    pseudo_label = ""

    def __init__(self, id, clean_text, In_english, pseudo_label):
        self.id = id
        self.clean_text = clean_text
        self.In_english = In_english
        self.pseudo_label = pseudo_label

    def __str__(self):
        return str(self.id) + " | " + self.clean_text + " | " + self.In_english + " | " + self.pseudo_label

def Get_Unlabelled_tweets():
    """
    Get the unlabelled tweets from database
    :return:
    """
    tweetsList = []
    try:
        conn = sqlHelper.get_mysql_conn()
        mycursor = conn.cursor()
        sql = ("select id, tweet from tweets where In_English is null and tweet is not null LIMIT 50")
        mycursor.execute(sql)
        result = mycursor.fetchall()

        for i in result:
            id = i[0]
            tweet = i[1]
            data = tweetsData(id, tweet)
            tweetsList.append(data)

    except mysql.connector.Error as error:
        print("Failed to select record to database: {}".format(error))
    finally:
        if conn.is_connected():
            mycursor.close()
            conn.close()
            print("MySQL connection is closed")

    return tweetsList

def Update_Tweet_pseudolabel(processedList):
    """
    Update the tweets pseudo label
    :param processedList: Processed tweets pseudo label
    """
    conn = sqlHelper.get_mysql_conn()
    mycursor = conn.cursor()
    try:
        sql = ("update tweets set clean_text = %s, In_English = %s, pseudo_label = %s where id = %s")

        for tweet in processedList:
            val = (tweet.clean_text, tweet.In_english, tweet.pseudo_label, tweet.id)
            mycursor.execute(sql, val)

        conn.commit()

    except mysql.connector.Error as error:
        print("Failed to update record to database: {}".format(error))
    finally:
        if conn.is_connected():
            mycursor.close()
            conn.close()
            print("MySQL connection is closed")


shortform_csv_path = "../data/kamus_singkatan2.csv"
shortform_list = ct.get_shortform_list(shortform_csv_path)

# repeat the process
for i in range (1, 1000):
    #1. Get the unlabelled tweets
    topicList = Get_Unlabelled_tweets()

    #2. Clean the text + translate to English + Pseudo label
    try:
        processedTweets = []
        for i in topicList:
            clean_text = light_clean(i.tweet, shortform_list)
            translate_en = translate(clean_text, source_lang="auto", target_lang="en").results[0].paraphrase
            emotion_detected = emo.identifyEmotion(translate_en)
            ptweet = ProcessedTweetsData(i.id, clean_text, translate_en, emotion_detected)
            processedTweets.append(ptweet)
            print("------------")
            print("ori: " + i.tweet)
            print("clean_text: " + clean_text)
            print("English: " + translate_en)
            print("Emotion: " + emotion_detected)
            print("------------")

        # 3. update the database
        Update_Tweet_pseudolabel(processedTweets)

        time.sleep(10)
    except Exception as error:
        print("Failed to pseudo-labelling: {}".format(error))




