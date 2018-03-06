import urllib
from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'http://www.nurseryrhymes.org/nursery-rhymes.html'
response = urlopen(url)
html = response.read()
def getListOfUrl:
    soup = BeautifulSoup(html, "html.parser")
    list = []
    for link in soup.find_all('a', href = True):
        list.append( link['href'])
    return list

def fixLinks(links):
    fixedLinks = []
    for link in links:
        if (!link.startswith('http')):
            fixedLinks.append("http://www.nurseryrhumes.org/" + link)
    return fixedLinks
