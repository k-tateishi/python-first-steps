import urllib.request
from bs4 import BeautifulSoup

req = urllib.request.urlopen('https://news.yahoo.co.jp/list')
soup = BeautifulSoup(req, 'html.parser')

ul = soup.find('ul', class_="list")
lis = ul.find_all(class_="ttl")

for item in lis:
    print(item.string)
