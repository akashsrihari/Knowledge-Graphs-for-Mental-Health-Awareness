import json

fp = open("cities.json","r")
lines = json.load(fp)

for i in lines:
	# print "https://api.yelp.com/v3/businesses/search?term=therapists&latitude="+str(i["latitude"])+"&longitude="+str(i["longitude"])
	# print "https://api.yelp.com/v3/businesses/search?term=psychiatrists&latitude="+str(i["latitude"])+"&longitude="+str(i["longitude"])
	# print "https://api.yelp.com/v3/businesses/search?term=mental%20health&latitude="+str(i["latitude"])+"&longitude="+str(i["longitude"])
	print "https://api.yelp.com/v3/businesses/search?term=support%20groups&latitude="+str(i["latitude"])+"&longitude="+str(i["longitude"])