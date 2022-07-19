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
    f = open("C:/Users/Kachouri/Desktop/text.txt", "a")
    driver= webdriver.Chrome(desired_capabilities=caps,options=options,executable_path="C:/Users/Kachouri/Desktop/Patient/chromedriver_win32/chromedriver.exe")
    try:
        response=driver.get("https://taager.com/home?fbclid=IwAR3uzg1-SH1EwYry31tPnrnkGMptHv1AuvAsg92ZR_-lPiy66IZ1qsv_uzc")
    except:
        pass
    aa=driver.page_source.encode("utf-8")
    f.write(str(aa))
    
    print("################",driver.page_source)
    


    driver.quit()
