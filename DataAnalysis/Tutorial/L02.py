import urllib2
import time

stocksToPull = "AAPL", "GOOG", "AMZN", "TSLA", "MSFT", "EBAY"

def pullData(stock):
    try:
        fileLine = "../DB/" + stock + ".txt"
        urlToVisit = "http://chartapi.finance.yahoo.com/instrument/1.0/" + stock + "/chartdata;type=quote;range=10d/csv"
        sourceCode = urllib2.urlopen(urlToVisit).read()
        splitSource = sourceCode.split("\n")

        for eachLine in splitSource:
            splitLine = eachLine.split(",")
            if len(splitLine) == 6:
                if "values" not in eachLine:
                    saveFile = open(fileLine, "a")
                    lineToWrite = eachLine + "\n"
                    saveFile.write(lineToWrite)
        print "Pulled", stock
        print "sleeping"
        time.sleep(1)

    except Exception, e:
        print "main loop", str(e)

for eachStock in stocksToPull:
    pullData(eachStock)
