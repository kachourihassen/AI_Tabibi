# -*- coding: utf-8 -*-
from lib2to3.pgen2 import driver
from this import d
from tokenize import String
import scrapy
 
 
from urllib.parse import urlencode
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
 
import time
import csv
class MedSpider(scrapy.Spider):
    name = 'Doctorslounge'
    allowed_domains = ['www.patient.info/']

    opt = webdriver.ChromeOptions()
    time.sleep(1)
    driver= webdriver.Chrome(options=opt,executable_path="C:/Users/Kachouri/Desktop/Patient/chromedriver_win32/chromedriver.exe")
    a=[]
    writer = csv.writer(open("C:/Users/Kachouri/Desktop/Patient/Depression_url.csv", 'w'))
  
    for i in range(0,197): 
        driver.get("https://patient.info/forums/discuss/browse/depression-683?page="+str(i)+"#group-discussions")
        for my_elem in driver.find_elements_by_xpath("//h3[@class='post__title']/a"):
            writer.writerow(  [my_elem.get_attribute("href")] )
        #a.append([my_elem.get_attribute("href") for my_elem in driver.find_elements_by_xpath("//h3[@class='post__title']/a")])

    driver.quit()



