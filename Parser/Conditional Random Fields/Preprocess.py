from bs4 import BeautifulSoup
import json_lines
import json
import nltk
from nltk.tokenize import RegexpTokenizer
from nltk import word_tokenize, pos_tag, ne_chunk
from nltk import conlltags2tree, tree2conlltags

"""

DO NOT RUN THIS FILE

IT WILL RESET ALL VALUES OF train_data.txt and test_data.txt to "irrelevant"

THIS FILE WAS MEANT TO INITIALIZE VALUES AND PART OF SPEECH

"""

tokenizer = RegexpTokenizer(r'[a-zA-Z]+')
fpr = open("train_text.txt")
fpr1 = open("train_data.txt","w+")
counter = 0
content = fpr.readlines()
for line in content:
	print counter
	counter += 1
	op = pos_tag(tokenizer.tokenize(line))
	for ips in op:
		fpr1.write(ips[0].encode("utf-8")+" "+ips[1].encode("utf-8")+" "+"irrelevant"+"\n")
fpr.close()
fpr1.close()


tokenizer = RegexpTokenizer(r'[a-zA-Z]+')
fpr = open("test_text.txt")
fpr1 = open("test_data.txt","w+")
counter = 0
content = fpr.readlines()
for line in content:
	print counter
	counter += 1
	op = pos_tag(tokenizer.tokenize(line))
	for ips in op:
		fpr1.write(ips[0].encode("utf-8")+" "+ips[1].encode("utf-8")+" "+"irrelevant"+"\n")
fpr.close()
fpr1.close()
