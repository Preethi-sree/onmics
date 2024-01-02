import requests
from bs4 import BeautifulSoup
html=requests.get("https://books.toscrape.com/index.html")
data= html.text.encode('utf8')
soup=BeautifulSoup(data,"html.parser")

tag=soup.find("div",class_="quotes")
quote_list=tag.find_all("div",class_="quotes")

for quote in quote_list:
    d=quote.find("div", class_="quoteText")
    author=d.find("span",class_="authorOrTitle")
    print(author.text.encode('utf8'),"----->",d.text.encode('utf8'))