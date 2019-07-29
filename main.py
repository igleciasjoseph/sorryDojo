from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import os, json, getpass, time, requests



# soup = BeautifulSoup(web, 'lxml')
browser = webdriver.Chrome()

def signIn():
    browser.get('https://learn.codingdojo.com/signin')
    iUser = input('Please enter your email for login without the @google.com ')
    iEmail = '@gmail.com'
    iPass = getpass.getpass()

    elem = browser.find_element_by_id('enter_email')
    elem.send_keys(iUser + iEmail)

    elem = browser.find_element_by_id("enter_password")
    elem.send_keys(iPass)

    elem.send_keys(Keys.ENTER)

soup = BeautifulSoup(signIn(), 'lxml')




print(soup.prettify())