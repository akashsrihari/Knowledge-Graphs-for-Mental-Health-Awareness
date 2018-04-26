import requests
import json

headers={
    'Authorization': 'Bearer FtD2yNQAplHXvcK8m10Z4DjLzjwDOlA7p6GGmMxtKIR2U-PZh3cZACl_Our8noT9__MTfoCb9CJm5fSJva26kN7Dc1Grmu0tOwZVhWhWVuvguCIDbDVh00wHOAzdWnYx'
}
fp = open("Yelpurls2.txt","r")
fp1 = open("YelpData2.jl","w")

urls = fp.readlines()
urls = map(lambda x: x.strip(),urls)

for i in urls:
	print i
	r=requests.get(i, headers=headers)
	op = json.loads(r.text)
	for j in op["businesses"]:
		fp1.write(json.dumps(j)+"\n")

fp1.close()