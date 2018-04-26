from selenium import webdriver
from bs4 import BeautifulSoup, SoupStrainer
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.chrome.options import Options
from time import localtime, strftime
import os
import json

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080")
chromedriver = "/Users/akashsrihari/Downloads/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=chromedriver)

fp = open("allEventbriteLinks.txt","r")
links = fp.readlines()
fp.close()
fp = open("Eventbrite.jl","w")
for i in range(len(links)):
	if len(links[i]) > 0:
		print i, len(links)
		driver.get(links[i])
		temp = {}
		temp["url"] = links[i]
		temp["raw_content"] = driver.page_source.encode("utf-8")
		temp["timestamp_crawl"] = strftime("%Y-%m-%dT%H:%M:%SZ", localtime())
		fp.write(json.dumps(temp))
		fp.write("\n")
fp.close()