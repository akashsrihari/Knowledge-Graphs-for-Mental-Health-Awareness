from bs4 import BeautifulSoup
import json_lines
import json

f = open("SrihariAkash_Chinam_cdr.jl")

counter = 0
lister = []

for i in json_lines.reader(f):

	dicto={}

	#url for webpage
	dicto["url"] = i["url"]

	#Group title
	soup = BeautifulSoup(i["raw_content"],"lxml")
	if len(soup.find_all(attrs={"class":"group-title"}))>0:
		x = BeautifulSoup(str(soup.find_all(attrs={"class":"group-title"})[0]),"lxml")
		dicto["group_name"] = x.h2.text

	#Contact number
	if len(soup.find_all(attrs={"data-event-label":"Profile_PhoneLink"}))>0:
		soup1 = BeautifulSoup(str(soup.find_all(attrs={"data-event-label":"Profile_PhoneLink"})[0]),"lxml")
		dicto["contact_number"] = soup1.a.text

	#Issues handled
	if len(soup.find_all(attrs={"class":"profile-list-comma"}))>0:
		issues = BeautifulSoup(str(soup.find_all(attrs={"class":"profile-list-comma"})[0]),"lxml")
		liz = issues.text[8:].split(",")
		for i in range(len(liz)):
			liz[i] = liz[i].strip()
		dicto["issues_handled"] = ",".join(liz)

	#Address
	if len(soup.find_all(attrs={"itemprop":"address"}))>0:
		address = BeautifulSoup(str(soup.find_all(attrs={"itemprop":"address"})[0]),"lxml")
		liz = address.text.strip().split("\n")[:-1]
		for i in range(len(liz)):
			liz[i]=liz[i].strip()
		dicto["group_address"] = " ".join(liz)

	#Host name
	if len(soup.find_all(attrs={"itemprop":"name"})):
		host = BeautifulSoup(str(soup.find_all(attrs={"itemprop":"name"})[0]),"lxml")
		dicto["host_name"] = host.text.strip()
	lister.append(dicto)

print len(lister)
f.close()
f = open("wrapper.json","w")
json.dump(lister, f)
f.close()