import commons.webscrapping.scrapping as sc
import commons.mysql.mysqlHelper as sqlHelper
import mysql.connector
from selenium import webdriver
# Get the tweets topic

class tweets_topic:
    """
    Class for tweets topic
    """
    id = ""
    searchTxt = ""
    url = ""
    status = ""

    def __init__(self, id, searchTxt, url, status):
        self.id = id
        self.searchTxt = searchTxt
        self.url = url
        self.status = status

    def __str__(self):
        return str(self.id) + " | " + self.searchTxt + " | " + self.url + " | " + str(
            self.status)


def Get_Tweet_topic():
    """
    Get the topic which has not been used for downloading
    :return: tweet topic
    """

    topicList = []
    try:
        conn = sqlHelper.get_mysql_conn()
        mycursor = conn.cursor()
        sql = ("select ID, SEARCH_TXT, URL, status from tweets_topic where status not in ('Y') LIMIT 500")
        mycursor.execute(sql)
        result = mycursor.fetchall()

        for i in result:
            id = i[0]
            searchTxt = i[1]
            url = i[2]
            status = i[3]
            data = tweets_topic(id, searchTxt, url, status)
            topicList.append(data)

    except mysql.connector.Error as error:
        print("Failed to select record to database: {}".format(error))
    finally:
        if conn.is_connected():
            mycursor.close()
            conn.close()
            print("MySQL connection is closed")

    return topicList

def Update_Tweet_topic_status(id, status):
    """
    Update the tweets topic status
    :param id: Topic ID
    :param status: status
    """
    conn = sqlHelper.get_mysql_conn()
    mycursor = conn.cursor()
    try:
        sql = ("update tweets_topic set status = %s where id = %s")
        val = (status, id)
        mycursor.execute(sql, val)
        conn.commit()

    except mysql.connector.Error as error:
        print("Failed to update record to database: {}".format(error))
    finally:
        if conn.is_connected():
            mycursor.close()
            conn.close()
            print("MySQL connection is closed")


def Insert_Tweets(topicId, tweetsList):
    """
    Insert tweets into tweets table
    :param topicId: Topic ID
    :param tweets: Tweets text
    """
    conn = sqlHelper.get_mysql_conn()
    mycursor = conn.cursor()
    try:
        sql = ("insert into tweets (topic_id, tweet) values (%s, %s)")

        for tweets in tweetsList:
            val = (topicId, tweets)
            mycursor.execute(sql, val)
        conn.commit()

    except mysql.connector.Error as error:
        print("Failed to insert record to database: {}".format(error))
    finally:
        if conn.is_connected():
            mycursor.close()
            conn.close()
            print("MySQL connection is closed")


for cnt in range(1, 4):
    id = 0
    try:

        # 0. Prepare the twitter
        driver = sc.get_x_web_component()

        # 1. Get the topic list
        topicList = Get_Tweet_topic()

        # 2. Query the tweets
        for topic in topicList:

            try:
                id = topic.id
                url = topic.url
                Update_Tweet_topic_status(id, "I")
                #tweetsList = sc.main_scrap_tweets(url)
                sc.search_tweets(driver, url)
                tweetsList = sc.extract_tweets(driver)

                Insert_Tweets(id, tweetsList)
                Update_Tweet_topic_status(id, "Y")
            except:
                print("Error... ")
                Update_Tweet_topic_status(id, "X")
    except:
        print("Error... ")
        Update_Tweet_topic_status(id, "X")


"""
tweet_url = "https://twitter.com/dccomm_gov/status/1751215857001460162"
tweetsList = sc.main_scrap_tweets(tweet_url)

print("tweets count: " + str(len(tweetsList)))

for tweet in tweetsList:
    print(tweet)

"""