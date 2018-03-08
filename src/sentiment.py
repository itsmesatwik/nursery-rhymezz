from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from rhymz.py import * 
analyzer = SentimentIntesityAnalyser()
def getScores():
    url  = "http://nurseryrhymes.org/nursery-rhymes.html"
    rhymes = scrapeRhymes(fixLinks(getListOfUrl(url)))
    sentimentScores = {}
    for rhyme in rhymes:
        sentimentScores[rhyme] = analyzer.polarity_scores(rhyme)
    return sentimentScores

def calculateOverallSentiment(dict):
    sentimentWeight = 0
    for rhyme in dict:
        sentimentWeight += (dict[rhyme]["pos"] + dict[rhyme["neg"] + dict[rhyme]["neu"])
    return sentimentWeight

def sentimentMeaning(weight):
    if (weight > 0.15):
        print("Rhyme is positive with a weight of " + weight)
    elif (weight < -0.15):
        print("Rhyme is dark with a weight of " + weight)
    else:
        print("Rhyme is neurtal with a weight of " + weight)

    
