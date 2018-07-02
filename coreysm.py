from bs4 import BeautifulSoup
import requests

source = requests.get("http://coreyms.com").text
soup = BeautifulSoup(source,"lxml")
for article in soup.findAll("article"):
	try:
		headline = article.h2.a.text
		summary = article.find('div',{'class':'entry-content'}).p.text
		VidSrc = article.find('iframe',{'class':'youtube-player'})['src']
		VidId = VidSrc.split('/')[4]
		link = f'http://youtube.com/watch?v={VidId}'
	except Exception e as:
		link = ''
		raise e	
	print(headline)
	print(summary)
	print(link)
	print()