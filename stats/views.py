from django.shortcuts import render
import requests 
from bs4 import BeautifulSoup
import os 
import numpy as np
extract_contents = lambda row: [x.text.replace('\n', '') for x in row] 
URL = 'https://www.mohfw.gov.in/'
response = requests.get(URL).content 
soup = BeautifulSoup(response, 'html.parser') 
header = extract_contents(soup.tr.find_all('th')) 
stats = [] 
all_rows = soup.find_all('tr') 

for row in all_rows[1:]: 
	stat = extract_contents(row.find_all('td')) 
	if stat: 
		if len(stat) == 5: 
			# last row 
			stat = ['', *stat] 
			stats.append(stat) 
		elif len(stat) == 4: 
			stats.append(stat) 

totalcase = stats[-1]
stats.remove(stats[-1]) 
# Create your views here. 
def index(request):
	mylist = 'http://127.0.0.1:8000'
	return render(request, "index.html", {'mykey':mylist})

def show_stats(request):
	mylist = 'http://127.0.0.1:8000'
	data = stats
	total = totalcase
	return render(request, "stats.html", {'mykey':mylist,'mydata':data, 'maxcase':total})

def show_supplies(request):
	mylist = 'http://127.0.0.1:8000'
	return render(request, "supplies.html", {'mykey':mylist})
