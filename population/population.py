import requests
from math import radians, cos, sin, asin, sqrt

response = requests.get("https://cdn.jsdelivr.net/gh/apilayer/restcountries@3dc0fb110cd97bce9ddf27b3e8e1f7fbe115dc3c/src/main/resources/countriesV2.json")
dataset = response.json()
data={}
for i in dataset:
	data[i['population']] = i['latlng']

pop=[]
for i in data.keys():
	pop.append(i)
pop.sort()

reqcord = []
poplim = 550
for i in range(len(pop)):
	if pop[i] >= poplim:
		for j in range(i,i+20):
			reqcord.append(data[pop[j]])
		break
s=0
for i in range(20):
	cord1 = reqcord[i]
	for j in range(i+1, 20):
		cord2 = reqcord[j]
	
		if len(cord1) == 0:
			lon1=0
			lat1=0
			lon2 = radians(cord2[1])
			lat2 = radians(cord2[0])
		elif len(cord2) == 0:
			lon2=0
			lat2=0
			lon1 = radians(cord1[1])
			lat1 = radians(cord1[0])
		else:
			lon1 = radians(cord1[1])
			lon2 = radians(cord2[1])
			lat1 = radians(cord1[0])
			lat2 = radians(cord2[0])
			
		
		dlon = lon2 - lon1
		dlat = lat2 - lat1
		a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
		c = 2 * asin(sqrt(a))
		r = 6371
		s += round((c*r),2)
		
print(round(s,2))
				
		 	
