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


def on_open(ws):
    json_data = json.dumps({'ticks':'R_50'})
    ws.send(json_data)

def on_message(ws, message):
    response = json.loads(message)['tick']
    epoch = response['epoch']
    quote = response['quote']
    
    # save history to list
    # saveToList(int(float(quote)*10000))
    saveToList(quote)
    # if 
    showStatistics(quote, 5)

    # 
    #print(response)

    # get current timestamp
    #timestamp1 = time.time()
    # convert from human readable date to timestamp
    #timestamp2 = int(time.mktime(time.strptime('2000-01-01 12:34:00', '%Y-%m-%d %H:%M:%S'))) - time.timezone

    # convert from timestamp to human readable date
    #localTimeString = time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.localtime(epoch))

    # Replace time.localtime with time.gmtime for GMT time.
    #gmtTimeString = time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.gmtime(epoch))
    if matchResult(4, 5):
        print(str(epoch) + " - " + str(quote) + " - " + "bet even")
        betList.append(True)
    else:
        print(str(epoch) + " - " + str(quote))
        betList.append(False)
    #print(timestamp1)
    #print(localTimeString)
    #print(gmtTimeString)

    # savetoDB("ticks", response)
    # print('ticks update: %s' % message)

def savetoDB(collectName, tickResponse):

    # update records to db
    client = MongoClient()
    db = client.Binary

    result = db.get_collection(collectName).insert_one(tickResponse)
    print(result.inserted_id)


if __name__ == "__main__":

    apiUrl = "wss://ws.binaryws.com/websockets/v3?app_id=1089"
    ws = websocket.WebSocketApp(apiUrl, on_message = on_message, on_open = on_open)
    ws.run_forever()