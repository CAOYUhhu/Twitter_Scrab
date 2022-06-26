#两个函数，分别实现推特登录和抓取指定账户最新推文（除去置顶推文）
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import  Options
import re


class TwitterScraper:

    def __init__(self):
        self.s = Service('C:\Program Files\Google\Chrome\Application\chromedriver.exe')
        self.chrome_options = Options()
        self.chrome_options.add_argument('--headless')
        self.driver = webdriver.Chrome(service=self.s, chrome_options=self.chrome_options)

    def twitterlogin(self, accountname, key):
        self.driver.get('https://www.twitter.com/login')
        sleep(3)
        username = self.driver.find_element(by=By.XPATH, value='//input[@name="text"]')
        username.send_keys(accountname)
        username.send_keys(Keys.RETURN)
        sleep(3)
        password = self.driver.find_element(by=By.XPATH, value='//input[@name="password"]')
        password.send_keys(key)
        password.send_keys(Keys.RETURN)

    def tweetget(self, accountpage):
        self.driver.get(accountpage)
        sleep(3)
        cards = self.driver.find_elements(by=By.XPATH, value='//div[@data-testid="tweetText"]')
        cards = cards[1]
        cards = cards.text
        cards = cards.split('\n')
        for card in cards:
            if 'NFT:' in card:
                project_name = card[card.rfind('NFT:'):]
            if 'etherscan.io/address/' in card:
                address = card[card.rfind('address/'):]
                address = address[8:50]
        return (project_name, address)
