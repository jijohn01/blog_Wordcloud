import pyperclip
from selenium import webdriver
import pyautogui
import re
import csv
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

class function:
    def __init__(self,driver):
        self.driver = driver
        self.action = webdriver.common.action_chains.ActionChains(self.driver)
        f = open('stop_words.txt','r')
        self.stop_words = []
        for line in f:
            self.stop_words.append(line.strip())
        f.close()

    def tap_change_main(self):
        self.driver.switch_to.window(self.driver.window_handles[0])

    def tap_change_sub(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    def cleanText(self,readData, del_text):
        text = re.sub(del_text,' ', readData)
        word_tokens = word_tokenize(text)
        result=''
        for w in word_tokens:
            if w not in self.stop_words:
                result = result+' '+w
        return result

    def headless(self):
        options= webdriver.ChromeOptions()
        options.add_argument('headless')

    def pass_auction_article(self,title):
        cnt = 0
        ispass = False
        pass_words = ['경매','매매','임대']
        for pass_word in pass_words:
            cnt += title.count(pass_word)
        if cnt >0:
            ispass = True
        return ispass