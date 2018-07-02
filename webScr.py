from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

myurl = "https://www.newegg.com/global/in/Product/ProductList.aspx?Submit=ENE&DEPA=0&Order=BESTMATCH&Description=graphics+card&ignorear=0&N=-1&isNodeId=1"
uClient = uReq(myurl)    # opening up connection , grabbing the page
pageHTML = uClient.read()
uClient.close()
pageSoup = soup(pageHTML,"html.parser")   # html parsing
containers = pageSoup.findAll("div",{"class":"item-container"})    #grab each product
fileName = "products.csv"
f = open(fileName,"w")
headers = "brand, productname, shipping\n"
f.write(headers)

for container in containers:
	brand = container.div.div.a.img["title"]
	title = container.findAll("a",{"class":"item-title"})
	productName = title[0].text
	ShippingContainer = container.findAll("li",{"class":"price-ship"})
	shipping = ShippingContainer[0].text.strip()

	print("brand: "+brand)
	print("product Name: "+productName)
	print("Shipping: "+shipping)
	f.write(brand+","+productName.replace(",","|")+","+shipping+"\n")

	
f.close()
