import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import pandas as pd
import chromedriver_autoinstaller
from config import email, passw, user
import os
 
chromedriver_autoinstaller.install()


def scrape_tweets(keyword):
    number_of_tweets = 300
    print(f"keyword: {keyword}")
    file_name = "twitter_output.csv"

    # binary = FirefoxBinary('/usr/bin/google-chrome')

    # You can change the binary to the browser of your choice

    driver = webdriver.Chrome()
    driver.get("https://twitter.com/login")

    sleep(3)
    driver.find_element(By.NAME, "text").send_keys(email)
    wait = WebDriverWait(driver, timeout=10).until(
        EC.presence_of_all_elements_located((By.XPATH, "//div[@role='button']"))
    )
    buttons = driver.find_elements(By.XPATH, "//div[@role='button']")
    buttons[2].click()
    wait = WebDriverWait(driver, timeout=10).until(
        EC.presence_of_all_elements_located((By.NAME, "text"))
    )
    driver.find_element(By.NAME, "text").send_keys(user)
    buttons = driver.find_elements(By.XPATH, "//div[@role='button']")
    buttons[1].click()
    wait = WebDriverWait(driver, timeout=10).until(
        EC.presence_of_all_elements_located((By.NAME, "password"))
    )
    driver.find_element(By.NAME, "password").send_keys(passw)
    driver.find_element(
        By.XPATH, "//div[@data-testid='LoginForm_Login_Button']"
    ).click()
    wait = WebDriverWait(driver, timeout=10).until(
        EC.presence_of_all_elements_located(
            (By.XPATH, "//span[text()='Refuse non-essential cookies']")
        )
    )
    driver.find_element(
        By.XPATH, "//span[text()='Refuse non-essential cookies']"
    ).click()

    sleep(3)

    driver.get(f"https://twitter.com/search?q={keyword}&src=typed_query&f=live")

    Tweets = []
    last_tweet_count = 0
    no_new_tweets_count = 0

    articles = driver.find_elements(By.XPATH, "//article[@data-testid='tweet']")

    while len(Tweets) < number_of_tweets:
        for article in articles:

            try:
                Tweet = article.find_element(By.XPATH, ".//div[@data-testid='tweetText']").text
                Tweets.append(Tweet)
            except:
                Tweets.append('')

        Tweets = list(set(Tweets))

        # Check if new tweets were found
        if len(Tweets) == last_tweet_count:
            no_new_tweets_count += 1
        else:
            no_new_tweets_count = 0

        # If no new tweets were found for 3 consecutive iterations, break
        if no_new_tweets_count >= 3:
            break

        last_tweet_count = len(Tweets)

        driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
        sleep(3)
        articles = driver.find_elements(By.XPATH, "//article[@data-testid='tweet']")

    print(f"{len(Tweets)} tweets")
    # keyword = [' '.join(keyword)]
    # Check if the file already exists
    if os.path.isfile(file_name):
        # If the file exists, append the new data without writing the header
        with open(file_name, mode='a', newline='', encoding='utf-8') as file:
            df = pd.DataFrame(zip([keyword] * len(Tweets), Tweets), columns=['Keyword', 'Tweets'])


            df.to_csv(file, index=False, header=False, mode='a', encoding='utf-8')
    else:
        # If the file doesn't exist, create it and write both the header and the new data
        df = pd.DataFrame(zip([keyword] * len(Tweets), Tweets), columns=['Keyword', 'Tweets'])

        df.to_csv(file_name, index=False, encoding='utf-8')


if __name__ == "__main__":
    # kw = input(str("Enter keywords followed by a comma: "))
    # keyword = kw.split(",")
    # print(keyword)
    keywords = ['Veerpont Gelderland',
                'Veerpont Rozenburg',
                'Veerpont Ameland',
                'Veerpont schiermonnikoog',
                'Veerpont Terschelling',
                'Veerpont Waddenveren']

    # Remove leading and trailing spaces from each keyword
    keywords = [keyword.strip() for keyword in keywords]
    for kw in keywords:
        scrape_tweets(kw)
        sleep(random.randint(4, 8))
