#proj2.py
from bs4 import BeautifulSoup
import urllib.request, urllib.error, urllib.parse
from urllib.request import urlopen
import requests
import ssl
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#### Problem 1 ####
print('\n*********** PROBLEM 1 ***********')
print('New York Times -- First 10 Story Headings\n')
base_url=urllib.request.urlopen('https://www.nytimes.com/',context=ctx)
html=base_url.read()
soup=BeautifulSoup(html,'html.parser')
i=0
for story_heading in soup.find_all(class_="story-heading"): 
	if i<10:
		if story_heading.a: 
			print(story_heading.a.text.replace("\n", " ").strip())
			i+=1
		else:
			print(story_heading.contents[0].strip())
			i+=1
### Your Problem 1 solution goes here


#### Problem 2 ####
print('\n*********** PROBLEM 2 ***********')
print('Michigan Daily -- MOST READ\n')
base_url=urllib.request.urlopen('https://www.michigandaily.com',context=ctx)
html=base_url.read()
soup=BeautifulSoup(html,'html.parser')
t_div=soup.find_all(class_='view-most-read')
contents=t_div[0].find_all('a')
for c in contents:
	print(c.get_text().replace('\n','').strip())
### Your Problem 2 solution goes here


#### Problem 3 ####
print('\n*********** PROBLEM 3 ***********')
print("Mark's page -- Alt tags\n")
base_url=urllib.request.urlopen('http://newmantaylor.com/gallery.html',context=ctx)
html=base_url.read()
soup=BeautifulSoup(html,'html.parser')
imgs=soup.find_all('img')
for img in imgs:
	print(img.get('alt','No alternative text provided!'))
### Your Problem 3 solution goes here


#### Problem 4 ####
print('\n*********** PROBLEM 4 ***********')
print("UMSI faculty directory emails\n")
def get_email(url,n):
	req=urllib.request.Request(url, None, {'User-Agent': 'SI_CLASS'})
	base_url=urllib.request.urlopen(req,context=ctx)
	html=base_url.read()
	soup=BeautifulSoup(html,'html.parser')
	contacts=soup.find_all(class_='field-item')
	k=n
	for contact in contacts:
		hrefs=contact.find_all('a',text='Contact Details')
		for href in hrefs:
			href=href.get('href')
			req=urllib.request.Request('https://www.si.umich.edu'+href,None,{'User-Agent': 'SI_CLASS'})
			url=urllib.request.urlopen(req,context=ctx)
			html=url.read()
			soup=BeautifulSoup(html,'html.parser')
			divs=soup.find_all(class_='field-item')
			try:
				print(str(k)+' '+divs[4].find('a').get_text())
			except:
				print(str(k)+' '+divs[3].find('a').get_text())
			k+=1
	return k
page1='https://www.si.umich.edu/directory?field_person_firstname_value=&field_person_lastname_value=&rid=4'
page2=page1+'&page=1'
page3=page1+'&page=2'
page4=page1+'&page=3'
page5=page1+'&page=4'
page6=page1+'&page=5'
n2=get_email(page1,1)
n3=get_email(page2,n2)
n4=get_email(page3,n3)
n5=get_email(page4,n4)
n6=get_email(page5,n5)
get_email(page6,n6)
### Your Problem 4 solution goes here
