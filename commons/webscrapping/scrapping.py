from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import re

USER_NAME = "johnlehping"
PWD = "myLehping123"
wait_seconds = 100
short_wait_seconds = 5


def get_x_web_component():
    # Get the web component for X. The web component is the main page after successfully login. It will turn off the
    # autoplay video feature to save the streaming data.

    # Setup Driver
    options = Options()
    options.page_load_strategy = 'eager'
    driver = webdriver.Chrome(options=options)

    # Access the page
    driver.get("https://twitter.com/login")

    # Setup the log in
    wait = WebDriverWait(driver, wait_seconds)

    element_locator = (By.XPATH, "//input[@name='text']")
    username = wait.until(EC.visibility_of_element_located(element_locator))
    username.send_keys(USER_NAME)
    next_button = driver.find_element(By.XPATH, "//span[contains(text(),'Next')]")
    next_button.click()

    password_locator = (By.XPATH, "//input[@name='password']")
    password = wait.until(EC.visibility_of_element_located(password_locator))
    password.send_keys(PWD)
    log_in = driver.find_element(By.XPATH, "//span[contains(text(),'Log in')]")
    log_in.click()
    sleep(short_wait_seconds)

    # turn off autoplay video
    driver.get("https://twitter.com/settings/autoplay")
    # element_autoplay = (By.XPATH, "//input[@name='video_autoplay']")
    element_never = (By.XPATH, "//span[contains(text(),'Never')]")
    text_never = wait.until(EC.visibility_of_element_located(element_never))
    text_never.click()
    sleep(short_wait_seconds)

    # back to the home page
    driver.get("https://twitter.com/home")
    sleep(short_wait_seconds)

    return driver


def search_tweets_topic(driver, search_value):
    # Search tweets
    # Search item and fetch it
    wait = WebDriverWait(driver, wait_seconds)

    element_search = (By.XPATH, "//input[@data-testid='SearchBox_Search_Input']")
    search_box = wait.until(EC.visibility_of_element_located(element_search))
    search_box.send_keys(search_value)
    search_box.send_keys(Keys.ENTER)
    sleep(short_wait_seconds)

def extract_tweets_topic(driver):

    hrefs = []
    # Scrap data on the landing page
    # extract data
    elems = driver.find_elements(By.XPATH, "//a[contains(@href,'/status')]")
    for elem in elems:
        #print(elem.get_attribute('href'))
        hrefs.append(elem.get_attribute('href'))

    # scroll to bottom to load more of the search result
    prev_height = driver.execute_script('return document.body.scrollHeight')
    max_refresh = 10
    cnt_refresh = 0
    while True:
        driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
        sleep(short_wait_seconds)
        new_height = driver.execute_script('return document.body.scrollHeight')

        # extract data
        elems = driver.find_elements(By.XPATH, "//a[contains(@href,'/status')]")
        for elem in elems:
            #print(elem.get_attribute('href'))
            hrefs.append(elem.get_attribute('href'))
        # extract data
        if new_height == prev_height:
            break
        prev_height = new_height
        #print('Load...')

    #print('End load...')
    #print(len(hrefs))
    return hrefs

def main_scrap_topic(search_string):
    driver = get_x_web_component()
    search_tweets_topic(driver, search_string)
    hrefs = extract_tweets_topic(driver)

    # remove invalid urls
    final_urls = []
    for href in hrefs:
        x = re.search("/analytics", href)
        y = re.search('/photo/*', href)
        z = re.search('/media_tags', href)
        if x is None and y is None and z is None:
            final_urls.append(href)

    # remove the duplicated

    final_urls = list(dict.fromkeys(final_urls))

    return final_urls


def extract_tweets(driver):
    """
    Scrap the tweets from
    :param driver: browser driver
    :return: The scrapped tweets
    """

    # scroll to bottom to load more of the search result
    prev_height = driver.execute_script('return document.body.scrollHeight')
    max_refresh = 50
    cnt_refresh = 0
    tweets = []

    while True:
        """
        To scroll to the bottom of the page and let the page to load all the tweets
        """
        try:

            driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
            sleep(short_wait_seconds)
            new_height = driver.execute_script('return document.body.scrollHeight')

            cnt_refresh = cnt_refresh + 1
            if cnt_refresh > max_refresh:
                break

            # click the show more  "Show more replies"
            sleep(2)
            try:
                more_spans = driver.find_elements(By.XPATH, "//span[contains(text(),'Show more replies')]")
                print("Found>>>")
                for more_span in more_spans:
                    more_span.click()
                sleep(short_wait_seconds)
            except:
                print("No more reply")

            # When reaching at the bottom of the page.
            if new_height == prev_height:
                break
            prev_height = new_height
            print('Load...')
        except:
            print("Exception during loading")

    print('End load...')

    """
    To scrap the tweets by 
    """
    Sections = driver.find_elements(By.XPATH, "//section[@role='region']")
    Tweets_section = Sections[0]


    Tweets_articles = Tweets_section.find_elements(By.XPATH, ".//article[@role='article']")
    print(">> " + str(len(Tweets_articles)))

    for Tweets_article in Tweets_articles:
        try:
            AdSpan = Tweets_article.find_elements(By.XPATH, ".//span[contains(text(),'Ad')]")

            if len(AdSpan) == 0:
                print("No Ad Span")
                tweettext_elems = Tweets_article.find_elements(By.XPATH, ".//div[@data-testid='tweetText']")

                for tweettext_elam in tweettext_elems:
                    span_elems = tweettext_elam.find_elements(By.TAG_NAME, "span")
                    if len(span_elems) == 0:
                        continue
                    try:
                        tweetStr = span_elems[0].text
                        print(">>" + tweetStr)
                        tweets.append(tweetStr)
                    except:
                        print("An exception occurred")

            else:
                print("#####has Ad Span")

        except Exception as error:
            print("An exception occurred:", error)
            print("Exception: No AsSpan")



    # remove the duplicates
    tweets = list(dict.fromkeys(tweets))

    print("Total tweets: " + str(len(tweets)))
    return tweets


def search_tweets(driver, url_string):
    """
    Go to the tweets URL
    :param driver: Browser driver
    :param url_string: URL for the tweets
    :return: None
    """
    driver.get(url_string)
    sleep(short_wait_seconds)


def main_scrap_tweets(url_string):
    """
    The main function for scrapping tweets by the URL
    :param url_string: The Tweets URL
    :return: The tweets list
    """
    driver = get_x_web_component()
    search_tweets(driver, url_string)
    tweetsList = extract_tweets(driver)
    return tweetsList



