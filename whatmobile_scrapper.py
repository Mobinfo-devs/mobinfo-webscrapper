
def whatmobile_scraper(url):
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
	
	
	#working
	
	specs=soup.find_all('td',class_='specs_box_inner')
	#for Mobile Name
	name=soup.title.text.strip().split(' ')
	index=name.index('Price')
	name=name[0:index]
	name=' '.join(name)
	
	#for adding specifications
	l=[]
	for i in specs:
		l.append(i.text.strip())
	
	head=['Name']+l[0::2] 
	ans=[name]+l[1::2] +[head.pop()]
	head.append('Ratings')
	# print(head,ans)
	
	#make dictionary for deleting columns easily
	
	dic={}
	fixed_coulmns=['Name', 'OS','UI', 'Weight', 'Colors', 'CPU', 'Chipset', 'Technology', 'Size', 'Resolution', 'Extra Features', 'Built-in', 'Main', 'Features', 'Front', 'Sensors', 'Capacity', 'Price in Rs.', 'Ratings']

	for i in range(len(head)):
		if head[i] in fixed_coulmns:
			dic[head[i]] = ans[i]
	
				
	#again make it list 
	head=list(dic.keys())
	ans=list(dic.values())
	#	
	# #first time for saving
	# with open('MobileDB.csv','w',encoding='UTF8') as f:
	# 	writer=csv.writer(f)
	# 	writer.writerow(head)
	# 	writer.writerow(ans)
					
	# other times
	with open('MobileDB.csv','a',encoding='UTF8') as f:
		writer=csv.writer(f)
		writer.writerow(ans)
		
	

		
#main	
# url='https://m.whatmobile.com.pk/Samsung_Galaxy-Z-Fold-2'
# whatmobile_scraper(url)

with open('links.txt', 'r') as f:
	for link in f:
		whatmobile_scraper(link.strip())
