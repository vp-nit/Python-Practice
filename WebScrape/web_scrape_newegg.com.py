import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20cards'

#opening up connection, Grabbing the page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

# html parsing
page_soup = soup(page_html, "html.parser")

filename = "products.csv"
f = open(filename,"w")
headers = "BRAND, PRODUCT DETAILS"
f.write(headers+'\n'+'\n')

# grabs each product
containers = page_soup.findAll("div",{"class":"item-container"})

for container in containers:
	brand_loc = container.findAll("a",{"class":"item-brand"})
	brand = brand_loc[0].img["title"]
	description = container.a.img["alt"]
	print('brand'+' '+brand)
	print('description'+' '+description)
	f.write(brand +',' + description.replace(',',' ') + '\n')

f.close()
