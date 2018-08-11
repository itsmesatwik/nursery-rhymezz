import urllib
from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import os
url = 'http://www.nurseryrhymes.org/nursery-rhymes.html'

#gets a list of all the urls from the landing page of rhymes website
response = urlopen(url)
html = response.read()
soup = BeautifulSoup(html, "html.parser")
list = []
for link in soup.find_all('a', href = True):
    list.append( link['href'])

#filters the links of rhymes and fixes them by completing the links for bs4
fixedLinks = []
for link in list:
    if (link.startswith('http') == False):
        fixedLinks.append("http://www.nurseryrhumes.org/" + link)

#gets the actual rhymes from the fixed links and adds them to a list
rhymes = []
for link in links:
    try:
        response = urlopen(link)
    except:
        continue
    html = response.read()
    soup = BeautifulSoup(html, "html5lib")
    print(soup.find(id = "nursery-rhymes-lyrics").get_text())
    rhymes.append(soup.find(id = "nursery-rhymes-lyrics").get_text())
