# selenium-related
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup as bs
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

# other necessary ones
import urllib.request
from bs4 import BeautifulSoup as bs
import pandas as pd
import json
import time
import re
import datetime
import csv

# set options as you wish
option = Options()
option.add_argument("--disable-infobars")
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")

 
    
browser = webdriver.Chrome(executable_path="C:/Users/Kachouri/Desktop/AI/Patient/geckodriver-v0.31.0-win32/chromedriver.exe", options=option)
browser.get("http://facebook.com")
browser.maximize_window()
wait = WebDriverWait(browser, 30)
email_field = wait.until(EC.visibility_of_element_located((By.NAME, 'email')))
email_field.send_keys('95116095')
pass_field = wait.until(EC.visibility_of_element_located((By.NAME, 'pass')))
pass_field.send_keys('A4KHqcQLxvzCS9K')
pass_field.send_keys(Keys.RETURN)

time.sleep(1)
writer = csv.writer(open("C:/Users/Kachouri/Desktop/facebookdata.csv", 'w'))
with open('C:/Users/Kachouri/Desktop/musae_facebook_target.csv',encoding="utf8") as fp:
    reader = csv.reader(fp, delimiter=",", quotechar='"')
    for row in reader:
        try:
            inputElesearch = browser.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[2]/div[3]/div/div/div[1]/div/div/label/input")
            inputElesearch.send_keys(str(row[2]))
            inputElesearch.send_keys(Keys.ENTER)
            time.sleep(5)
            soup=bs(browser.page_source,"html.parser")
            all_posts1=soup.find_all("a",{"class":"x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz x1heor9g xt0b8zv x1s688f xq9mrsl"})
            all_posts2=soup.find_all("a",{"class":"x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz xt0b8zv xzsf02u x1s688f"})


            if(not str(all_posts1)):
                link = re.findall(r'facebook.com(/\S*)?"', str(all_posts1))[0]
                link = str(link).replace("['", "")
                link =str(link).replace("']", "")
                print("helllllllo   dddddd   "+"https://facebook.com"+ str(link))
                try:
                    writer.writerow("https://facebook.com"+ str(link) )
                except:
                    writer.writerow( [] )

            else:
                link = re.findall(r'facebook.com(/\S*)?"', str(all_posts2))[0]
                link = str(link).replace("['", "")
                link =str(link).replace("']", "")
                print("helllllllo   dddddd   "+"https://facebook.com"+ str(link))
                try:
                    writer.writerow("https://facebook.com"+ str(link) )
                except:
                    writer.writerow( [] )

        except:
            pass


#browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")


