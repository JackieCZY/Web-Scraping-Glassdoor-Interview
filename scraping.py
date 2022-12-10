#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 16:55:21 2022

@author: chenzhiyi
"""
# %%%%%%

import datetime
import os
import pandas as pd
import re
import time
import requests
# libraries to crawl websites
from bs4          import BeautifulSoup
from selenium     import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# %%%%%%

pd.set_option('display.max_rows', 10)
pd.set_option('display.max_columns', 5)
pd.set_option('display.max_colwidth', 10)
pd.set_option('display.width',800)
path = "/Users/chenzhiyi/Documents/BUS 256A"
os.chdir(path)

driver = webdriver.Chrome(executable_path="/Users/chenzhiyi/Documents/BUS 256A/chromedriver")
driver.get("https://www.glassdoor.com/profile/login_input.htm")
#driver.close()


# %%%%%%

# links

links = ['https://www.glassdoor.com/Interview/Amazon-Data-Analyst-Interview-Questions-EI_IE6036.0,6_KO7,19.htm?filter.jobTitleFTS=Data+Analyst',
         'https://www.glassdoor.com/Interview/Bloomberg-L.P.-data-analyst-Interview-Questions-EI_IE3096.0,14_KO15,27.htm?filter.jobTitleFTS=data+analyst',
         'https://www.glassdoor.com/Interview/Google-Data-Analyst-Interview-Questions-EI_IE9079.0,6_KO7,19.htm?filter.jobTitleFTS=Data+Analyst',
         'https://www.glassdoor.com/Interview/Uber-Data-Analyst-Interview-Questions-EI_IE575263.0,4_KO5,17.htm?filter.jobTitleFTS=Data+Analyst',
         'https://www.glassdoor.com/Interview/Meta-Data-Analyst-Interview-Questions-EI_IE40772.0,4_KO5,17.htm?filter.jobTitleFTS=Data+Analyst']


# %%%%%%

# login

username = "example@email.com"
password = "Password"

def login_glassdoor(username, password):
    try:
        #find and click the signIn button locate in the website
        #driver.find_elements(By.XPATH, "//*[@id='SignInButton']")[0].click()
        #find where to enter the username
        user_field = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.NAME, "username")))
        #put the username you enter to the box
        time.sleep(5)
        user_field.send_keys(username)
        time.sleep(5)
        #find the continue button and click
        #glassdoor requires users to enter the username first and click continue to enter password
        driver.find_elements(By.XPATH, "//*[@id='InlineLoginModule']/div/div[1]/div/div/div/div/form/div[2]/button")[0].click()
        time.sleep(5)
        #place to enter the password
        pw_field = driver.find_element(By.XPATH, "//*[@id='inlineUserPassword']")
        #place to click login
        login_button = driver.find_element(By.XPATH, "//*[@id='InlineLoginModule']/div/div[1]/div/div/div/div/form/div[2]/button/span")
        
        time.sleep(5)
        #enter the password in the box
        pw_field.send_keys(password)
        time.sleep(5)
        #click the login button
        login_button.click()
    except TimeoutException:
        print("login failed")
        
login_glassdoor(username, password)

# %%%%%%

interview_one=[]

for link in links:
    time.sleep(5)
    driver.get(link)
    time.sleep(5)
    while True:
        reviews=WebDriverWait(driver, 30).until(EC.visibility_of_all_elements_located((By.XPATH, "//div[@class='col-12']")))
        for i in range(len(reviews)):
            interview_review = {}
            interview_review["scrapping date"] = datetime.datetime.now()
            interview_review["url"] = driver.current_url
            soup = BeautifulSoup(reviews[i].get_attribute('innerHTML'))
            try:
                title = soup.find('h2', attrs={'class':'mt-0 mb-xxsm css-93svrw el6ke055'}).text
            except:
                title = ""
            interview_review['title'] = title
            try:
                offer = soup.find_all('span', {'class':'mb-xxsm'})[0].text
            except:
                offer = ""
            interview_review["offer"] = offer
            try:
                experience = soup.find_all('span',{'class':'mb-xxsm'})[1].text
            except:
                experience = ""
            interview_review["experience"] = experience
            try:
                difficulty = soup.find_all('span',{'class':'mb-xxsm'})[2].text
            except:
                difficulty = ""
            interview_review["difficulty"] = difficulty
            try:
                interview = soup.find_all('p')[2].text
                #interview = soup.find('p', {'class':'css-w00cnv mt-xsm mb-std'}).text
            except:
                interview = ""
            interview_review["interview"] = interview
            try:
                question = soup.find('span', attrs = {'class':'d-inline-block mb-sm'}).text   
            except:
                question = ""
            interview_review["question"] = question
            try:
                application = soup.find('p', attrs={'class':'mt-xsm mb-std'}).text 
            except:
                application = ""
            interview_review["application"] = application   
            interview_one.append(interview_review)
        try:
            next_button = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='EmployerInterviews']/div[4]/div/div[1]/button[2]")))   
        except TimeoutException:
            break
        next_button.click()
        time.sleep(5)


df = pd.DataFrame(interview_one)
df.to_csv("interview_review.csv")
