import websocket
import json
import time
# from pymongo import MongoClient

# list stores odd or even
tempList = []

# list stores bet advice
betList = []
countWin = 0
countLoss = 0


epoch = 1492502800
now = 1492577072

def isOdd(quote):
    return int(quote[-1]) % 2 !=0

def saveToList(quote):
    # if odd append True
    # even number: n % 2 == 0
    # odd number: n % 2 != 0
    tempList.append(isOdd(quote))

def matchResult(failTimes = 3, ticks = 5):
    length = len(tempList)
    if length > failTimes * ticks:
        r = True
        for i in range(failTimes):
            # print("----" + str(tempList[-i*ticks-1]))
            r = tempList[-i*ticks-1] and r
        return r
    else:
        if length == failTimes * ticks:
            print("======= Begin =======")
        return False

# def purchase(stake):

def showStatistics(quote, ticks = 5):
    global countWin, countLoss
    if len(betList) > ticks:
        if not isOdd(quote) and betList[-ticks]:
            countWin += 1
        elif isOdd(quote) and betList[-ticks]:
            countLoss += 1
        
    print("Win: {0} / Loss: {1}".format(countWin, countLoss))
    # print(countWin)
    # + " - Loss: " + str(countLoss))

def retrieve_history_data(count = 5000):
    global epoch
    json_data = json.dumps({"ticks_history": "R_50", "end": epoch, "count": count})
    print("=============== {0} ===============".format(epoch))
    epoch += count*2
    ws.send(json_data)

def on_open(ws):
    #json_data = json.dumps({'ticks':'R_50'})
    #ws.send(json_data)
    retrieve_history_data()

def on_message(ws, message):
    # time exceed 
    if epoch-10000 > time.time():
        ws.close()
        return
    #response = json.loads(message)['tick']
    #epoch = response['epoch']
    #quote = response['quote']

    response = json.loads(message)["history"]
    prices = response["prices"]
    times = response["times"]
    for i in range(len(prices)):
            analysis(times[i], prices[i])
    time.sleep(1)
    retrieve_history_data()


def analysis(epoch, quote):
    ticks = 5

    # save history to list
    saveToList(quote)
    # if 
    showStatistics(quote, ticks)

    if matchResult(6, ticks):
        print(str(epoch) + " - " + str(quote) + " - " + "bet even")
        betList.append(True)
    else:
        print(str(epoch) + " - " + str(quote))
        betList.append(False)


def savetoDB(collectName, tickResponse):

    # update records to db
    client = MongoClient()
    db = client.Binary

    result = db.get_collection(collectName).insert_one(tickResponse)
    print(result.inserted_id)

    # savetoDB("ticks", response)
    # print('ticks update: %s' % message)

def timeStamp(timeString):
    # get current timestamp
    #timestamp1 = time.time()
    # convert from human readable date to timestamp
    timestamp2 = int(time.mktime(time.strptime(timeString, '%Y-%m-%d %H:%M:%S'))) - time.timezone
    return timestamp2
    # convert from timestamp to human readable date
    #epoch = 1477972800
    # 'Tue, 01 Nov 2016 00:00:00 +0000 - epoch: 1477972800'
    #localTimeString = time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.localtime(epoch))

    # Replace time.localtime with time.gmtime for GMT time.
    #gmtTimeString = time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.gmtime(epoch))

    #print(timestamp1)
    #print(localTimeString)
    #print(gmtTimeString)

if __name__ == "__main__":
    # timeStamp()
    epoch = timeStamp("2017-04-01 00:00:00")
    apiUrl = "wss://ws.binaryws.com/websockets/v3?app_id=1089"
    ws = websocket.WebSocketApp(apiUrl, on_message = on_message, on_open = on_open)
    ws.run_forever()