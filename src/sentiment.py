from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from rhymz.py import * 
analyzer = SentimentIntesityAnalyser()

url = "http://nurseryrhymes.org/nursery-rhymes.html"
rhymes = scrapeRhymes(fixLinks(getListOfUrl(url)))
sentimentScores = {}
for rhyme in rhymes:
    sentimentScores[rhyme] = analyzer.polarity_scores(rhyme)

