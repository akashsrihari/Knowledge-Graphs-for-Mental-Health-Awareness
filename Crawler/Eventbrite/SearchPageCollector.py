import re
import urlparse
from selenium import webdriver
from bs4 import BeautifulSoup, SoupStrainer
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.chrome.options import Options
import os
import json

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080")
chromedriver = "/Users/akashsrihari/Downloads/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=chromedriver)

link = "https://www.yelp.com/search?find_desc=therapists&find_loc=california"

event_links = []
wait = WebDriverWait(driver, 100)
driver.get(link)
fp = open("Yelp_therapists_source_pages.jl","w+")

for i in range(10000):

	try:
		print "i - ",i
		element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'regular-search-result')))
		dicto = {}
		dicto[str(i)] = driver.page_source.encode("utf-8")
		fp.write(json.dumps(dicto)+"\n")
		element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'u-decoration-none next pagination-links_anchor')))
		butt = driver.find_element_by_class_name("u-decoration-none next pagination-links_anchor")
		butt.click()

	except TimeoutException:
		print "Time out"
		break

	except WebDriverException:
		print "No more pages"
		break

fp.close()