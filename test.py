import requests
from bs4 import BeautifulSoup
url ='https://www.bbc.com/news/world-europe-45926754'
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html5lib')
article = soup.find_all('p')
#print(article[1].string)
for x in article:
    print(x.string)
