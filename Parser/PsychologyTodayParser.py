from bs4 import BeautifulSoup
import json_lines
import json

f = open("PsychologyToday_All.jl")

counter = 0
lister = []

fp = open("ParsedPsychologyToday.jl","w")

for i in json_lines.reader(f):

	counter += 1
	print counter

	dicto={}

	#url for webpage
	dicto["url"] = i["url"]

	#Group title
	soup = BeautifulSoup(i["raw_content"],"lxml")
	if len(soup.find_all(attrs={"class":"groups-section"}))>0:
		x = BeautifulSoup(str(soup.find_all(attrs={"class":"groups-section"})[0]),"lxml")
		x = BeautifulSoup(str(x.find_all(attrs={"class":"group-title"})[0]),"lxml")
		if x.h2 != None:
			dicto["group_name"] = x.h2.text
		elif x.h3 != None:
			dicto["group_name"] = x.h3.text.split("\n")[0]

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
		temp_dicto = {}
		if len(address.find_all(attrs={"itemprop":"streetAddress"}))>0:
			temp_dicto["street"] = BeautifulSoup(str(address.find_all(attrs={"itemprop":"streetAddress"})),"lxml").span.text.replace("\\n","").strip()
		if len(address.find_all(attrs={"itemprop":"postalcode"}))>0:
			temp_dicto["zip"] = BeautifulSoup(str(address.find_all(attrs={"itemprop":"postalcode"})),"lxml").span.text.replace("\\n","").strip()
		if len(address.find_all(attrs={"itemprop":"addressLocality"}))>0:
			temp_dicto["city"] = BeautifulSoup(str(address.find_all(attrs={"itemprop":"addressLocality"})),"lxml").span.text.replace("\\n","").strip()
		if len(address.find_all(attrs={"itemprop":"addressRegion"}))>0:
			temp_dicto["state"] = BeautifulSoup(str(address.find_all(attrs={"itemprop":"addressRegion"})),"lxml").span.text.replace("\\n","").strip()
		dicto["address"] = temp_dicto

	#Host name
	if len(soup.find_all(attrs={"itemprop":"name"})):
		host = BeautifulSoup(str(soup.find_all(attrs={"itemprop":"name"})[0]),"lxml")
		dicto["organiser"] = host.text.strip()

	fp.write(json.dumps(dicto)+"\n")

f.close()
fp.close()