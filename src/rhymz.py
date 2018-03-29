import urllib
from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import os

url = 'http://www.nurseryrhymes.org/nursery-rhymes.html'

#gets a list of all the urls from the landing page of rhymes website
def getListOfUrl(url):
    response = urlopen(url)
    html = response.read()
    soup = BeautifulSoup(html, "html.parser")
    list = []
    for link in soup.find_all('a', href = True):
        list.append( link['href'])
    return list

#filters the links of rhymes and fixes them by completing the links for bs4
def fixLinks(links):
    fixedLinks = []
    for link in links:
        if (link.startswith('http') == False):
            fixedLinks.append("http://www.nurseryrhumes.org/" + link)
    return fixedLinks

#gets the actual rhymes from the fixed links and adds them to a list
def scrapeRhymes(links):
    rhymes = []
    for link in links:
        response = urlopen(link)
        html = response.read()
        soup = BeautifulSoup(html, "html.parser")
        print(soup.find(id = "nursery-rhymes-lyrics").get_text())
        rhymes.append(soup.find(id = "nursery-rhymes-lyrics").get_text())
    return rhymes

# call function
def printRhymes():
    rhymes = scrapeRhymes(fixLinks(getListOfUrl(url)))
    for text in rhymes:
        print(text)


