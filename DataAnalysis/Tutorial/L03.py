import urllib2
import time
import datetime


stocksToPull = "AAPL", "GOOG", "AMZN", "TSLA", "MSFT", "EBAY"

def pullData(stock):
    try:
        print "Currently pulling", stock
        print str(datetime.datetime.fromtimestamp(time.time()).strftime("%Y-%m-%d %H:%M:%S"))
        urlToVisit = "http://chartapi.finance.yahoo.com/instrument/1.0/" + stock + "/chartdata;type=quote;range=10d/csv"
        saveFileLine = "../DB/" + stock + ".txt"

        try:
            readExistingData = open(saveFileLine, "r").read()
            splitExisting = readExistingData.split("\n")
            mostRecentLine = splitExisting[-2]
            lastUnix = int(mostRecentLine.split(",")[0])

        except:
            lastUnix = 0
        
        saveFile = open(saveFileLine, "a")
        sourceCode = urllib2.urlopen(urlToVisit).read()
        splitSource = sourceCode.split("\n")

        for eachLine in splitSource:
            splitLine = eachLine.split(",")
            if len(splitLine)==6:
                if int(splitLine[0] > lastUnix):
                    if "values" not in eachLine:
                        lineToWrite = eachLine + "\n"
                        saveFile.write(lineToWrite)
        saveFile.close()

        print "Pulled" + stock
        print "sleeping..."
        print str(datetime.datetime.fromtimestamp(time.time()).strftime("%Y-%m-%d %H:%M:%S"))
        time.sleep(300)
        
    except Exception, e:
        print "main loop", str(e)

for eachStock in stocksToPull:
    pullData(eachStock)
