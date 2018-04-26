from bs4 import BeautifulSoup, SoupStrainer
import json_lines
import json
from time import strftime, gmtime, localtime
import re

f = open("Eventbrite.jl","r")

counter = 0
lister = []

fp = open("ParsedEventBrite.jl","w")
for i in json_lines.reader(f):
	dicto={}

	counter += 1
	print counter

	#url for webpage
	dicto["url"] = i["url"].strip()

	#Group title
	soup = BeautifulSoup(i["raw_content"],"lxml")

	if len(soup.find_all(attrs={"class":"listing-hero-title"}))>0:
		x = BeautifulSoup(str(soup.find_all(attrs={"class":"listing-hero-title"})[0]),"lxml")
		dicto["event_name"] = x.h1.text

	if len(soup.find_all(attrs={"class":"listing-hero-header"}))>0:
		x = BeautifulSoup(str(soup.find_all(attrs={"class":"listing-hero-header"})),"lxml")
		if len(x.find_all(attrs={"class":"listing-hero-date"}))>0:
			x = BeautifulSoup(str(x.find_all(attrs={"class":"listing-hero-date"})),"lxml")
			if x.time != None:
				if x.time["datetime"] != None:
					dicto["date"] = x.time["datetime"]

	if len(soup.find_all(attrs={"class":"event-details"}))>0:
		x = BeautifulSoup(str(soup.find_all(attrs={"class":"event-details"})),"lxml")
		if len(x.find_all(attrs={"class":"event-details__data"}))>0:
			x = BeautifulSoup(str(x.find_all(attrs={"class":"event-details__data"})[1]),"lxml")
			address = x.find_all("p")[-3:-1]
			if len(address) == 2:
				temp_dicto = {}
				temp_dicto["street"] = address[0].text.strip()
				a = address[1].text.strip().split(",")
				if len(a) == 2:
					temp_dicto["city"] = a[0].strip()
					temp_dicto["zip"] = a[1][-6:].strip()
					temp_dicto["state"] = a[1].strip()[0:2]
				dicto["address"] = temp_dicto

	if len(soup.find_all(attrs={"class":"js-display-price"}))>0:
		x = BeautifulSoup(str(soup.find_all(attrs={"class":"js-display-price"})),"lxml")
		dicto["price"] = x.div.text.replace("\\n","").replace("\\t","").replace("\\u2013","-")

	if len(soup.find_all(attrs={"class":"l-mar-top-3"}))>0:
		x = BeautifulSoup(str(soup.find_all(attrs={"class":"l-mar-top-3"})),"lxml")
		if len(x.find_all(attrs={"class":"js-d-scroll-to"}))>0:
			x = BeautifulSoup(str(x.find_all(attrs={"class":"js-d-scroll-to"})),"lxml")
			dicto["organiser"] = x.a.text.replace("\\n","").replace("\\t","").replace("\\","").replace("by","").strip()

	fp.write(json.dumps(dicto)+"\n")