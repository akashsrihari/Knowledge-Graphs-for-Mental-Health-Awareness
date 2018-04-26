import json
import json_lines
from nltk.metrics import edit_distance

fp = open("YelpData.jl","r")
fp2 = open("ParsedEventBrite.jl", "r")

file1 = fp.readlines()
file2 = fp2.readlines()

liz = []
liz2 = []
statename_to_abbr = {'District of Columbia': 'DC','Alabama': 'AL','Montana': 'MT','Alaska': 'AK','Nebraska': 'NE','Arizona': 'AZ','Nevada': 'NV','Arkansas': 'AR','New Hampshire': 'NH','California': 'CA','New Jersey': 'NJ','Colorado': 'CO','New Mexico': 'NM','Connecticut': 'CT','New York': 'NY','Delaware': 'DE','North Carolina': 'NC','Florida': 'FL','North Dakota': 'ND','Georgia': 'GA','Ohio': 'OH','Hawaii': 'HI','Oklahoma': 'OK','Idaho': 'ID','Oregon': 'OR','Illinois': 'IL','Pennsylvania': 'PA','Indiana': 'IN','Rhode Island': 'RI','Iowa': 'IA','South Carolina': 'SC','Kansas': 'KS','South Dakota': 'SD','Kentucky': 'KY','Tennessee': 'TN','Louisiana': 'LA','Texas': 'TX','Maine': 'ME','Utah': 'UT','Maryland': 'MD','Vermont': 'VT','Massachusetts': 'MA','Virginia': 'VA','Michigan': 'MI','Washington': 'WA','Minnesota': 'MN','West Virginia': 'WV','Mississippi': 'MS','Wisconsin': 'WI','Missouri': 'MO','Wyoming': 'WY'}
abbr_to_statename = {v: k for k, v in statename_to_abbr.iteritems()}

fp3 = open("LinkedEntities_Yelp_EventBrite.jl","w")

counter = 0

for i1 in file1:
	counter += 1
	i = json.loads(i1)
	print counter

	for j1 in file2:

		j = json.loads(j1)

		if "address" in j and "location" in i:
			if "state" in j["address"] and "state" in i["location"] and len(j["address"]["state"])>0 and len(i["location"]["state"])>0 and j["address"]["state"] in statename_to_abbr:
				if (1-float(edit_distance(statename_to_abbr[j["address"]["state"]].lower(),i["location"]["state"].lower()))/max(len(statename_to_abbr[j["address"]["state"]]),len(i["location"]["state"]))) < 1:
					continue
			if "city" in j["address"] and "city" in i["location"] and len(j["address"]["city"])>0 and len(i["location"]["city"])>0:
				if (1-float(edit_distance(j["address"]["city"].lower(),i["location"]["city"].lower()))/max(len(j["address"]["city"]),len(i["location"]["city"]))) < 0.8:
					continue
			if "zip" in j["address"] and "zip" in i["location"] and len(j["address"]["zip"])>0 and len(i["location"]["zip_code"])>0:
				if (1-float(edit_distance(j["address"]["zip"].lower(),i["location"]["zip"].lower()))/max(len(j["address"]["zip"]),len(i["location"]["zip"]))) < 1:
					continue

		dicto={}
		if "name" in i:
			
			if "organiser" in j:
				if (1-float(edit_distance(j["organiser"].lower(),i["name"].lower()))/max(len(j["organiser"]),len(i["name"]))) > 0.75:
					dicto = dict(j)
					dicto["yelp_name"] = i["name"]
					dicto["yelp_url"] = i["url"]
					dicto["yelp_rating"] = i["rating"]
					dicto["yelp_id"] = i["id"]

			if "event_name" in j and len(dicto)==0:
				if (1-float(edit_distance(j["event_name"].lower(),i["name"].lower()))/max(len(j["event_name"]),len(i["name"]))) > 0.75:
					dicto = dict(j)
					dicto["yelp_name"] = i["name"]
					dicto["yelp_url"] = i["url"]
					dicto["yelp_rating"] = i["rating"]
					dicto["yelp_id"] = i["id"]

		if len(dicto)>0:
			fp3.write(json.dumps(dicto)+"\n")

fp3.close()
fp2.close()
fp.close()