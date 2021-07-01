def whatmobile_scraper(url):
	#for formatting
	from FormatText import FormatText
	#for getting request Module
	import requests
	#web scrapping moduel
	from bs4 import BeautifulSoup
	#URL where all data is stored
	url_mobile = url
	#for getting request for page
	page=requests.get(url_mobile)
	#soup will contain whole html file
	soup=BeautifulSoup(page.content,'html.parser')
	#for writing file
	import csv
	
	#print(soup) # its for printing whole xml file
	#formatted text
	print(FormatText.blue+FormatText.bold+FormatText.underline+"WhatMobile Scraper"+FormatText.end+"\n")
	
	#working
	
	
	specs=soup.find_all('td',class_='specs_box_inner')
	#for Mobile Name
	name=soup.title.text.strip().split(' ')
	index=name.index('Price')
	name=name[0:index]
	
	#for adding specifications
	l=[]
	for i in specs:
		l.append(i.text.strip())
	
	head=['Name']+l[0::2] 
	ans=[' '.join(name)]+l[1::2] +[head.pop()]
	head.append('Ratings')
	
	#make dictionary for deleting columns easily
	
	dic={}
	fixed_coulmns=['Name', 'OS', 'Weight', 'Colors', 'CPU', 'Chipset', 'Technology', 'Size', 'Resolution', 'Extra Features', 'Built-in', 'Main', 'Features', 'Front', 'Sensors', 'Capacity', 'Price in Rs.', 'Ratings', '']

	for i in range(len(head)):
		if head[i] in fixed_coulmns:
			dic[head[i]] = ans[i]
	

	val=dic['']
	dic['BatteryFeatures']=val
	del dic['']
	#checking present for 5G Band and NFC and Radio
	try:
		del dic['NFC']
	except:
		pass
	try:
		del dic['5G Band']
	except:
		pass
	try:
		del dic['Radio']
	except:
		pass
	try:
		del dic['Protection']
	except:
		pass
	try:
		del dic['Infrared']
	except:
		pass
				
	#again make it list 
	head=list(dic.keys())
	print(head)
	ans=list(dic.values())
	#			
#	#first time for saving
#	with open('MobileDB.csv','w',encoding='UTF8') as f:
#		writer=csv.writer(f)
#		writer.writerow(head)
#		writer.writerow(ans)
					
	#other times
	with open('MobileDB.csv','a',encoding='UTF8') as f:
		writer=csv.writer(f)
		writer.writerow(ans)
		
	

		
#main	
url='https://m.whatmobile.com.pk/Huawei_Mate-20-Pro'
whatmobile_scraper(url)