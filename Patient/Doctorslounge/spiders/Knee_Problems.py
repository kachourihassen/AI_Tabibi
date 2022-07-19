from lib2to3.pgen2 import driver
from this import d
from tokenize import String
import scrapy
from urllib.parse import urlencode
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import re
import time
import csv
from selenium.webdriver.common.by import By


class MedSpider(scrapy.Spider):
    options = webdriver.ChromeOptions()
    
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    options.add_argument("--profile-directory=pySelenium")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--disable-default-apps")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("-no-sandbox")
    options.add_argument("--disable-infobars")
    options.add_argument("--dns-prefetch-disable")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-notifications")
    options.add_argument("--ignore-certificate-errors-spki-list")
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--ignore-ssl-errors")
    options.add_argument("--allow-insecure-localhost")
    options.add_argument("--ignore-urlfetcher-cert-requests")
    options.add_experimental_option('useAutomationExtension',False)
    options.add_argument("log-level=3")
    caps = webdriver.DesiredCapabilities.CHROME.copy()
    caps['acceptInsecureCerts'] = True
    caps['acceptSslCerts'] = True
    
    writer = csv.writer(open("C:/Users/Kachouri/Desktop/Patient/Data/Knee_Problems_question.csv", 'w'))
    driver= webdriver.Chrome(desired_capabilities=caps,options=options,executable_path="C:/Users/Kachouri/Desktop/Patient/chromedriver_win32/chromedriver.exe")
    with open('C:/Users/Kachouri/Desktop/Patient/Knee_Problems_url.csv') as fp:
        reader = csv.reader(fp, delimiter=",", quotechar='"')
        for row in reader:
            try:
                driver.get(str(row[0]))
            except:
               pass
           
            try:
                writer.writerow( [ (driver.find_element(By.CLASS_NAME, 'post__content')).text] )
            except:
                writer.writerow( [] )
            
             


    driver.quit()
