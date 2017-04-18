import websocket
import json
import time
# from pymongo import MongoClient

# change list to tuple
tempList = []

def saveToList(quote):
    tempList.append(quote)

def matchResult(failTimes = 3, ticks = 5):
    # even number: n%2==0
    # odd number: n%2!=0
    if len(tempList) > failTimes * ticks:
        r = True
        for i in range(failTimes):
            r = (int(float(tempList[-i*ticks-1])*10000) % 2 !=0 and r)
        return r
    else:
        return False

def on_open(ws):
    json_data = json.dumps({'ticks':'R_50'})
    ws.send(json_data)

def on_message(ws, message):
    response = json.loads(message)['tick']
    epoch = response['epoch']
    quote = response['quote']
    
    # save history to list
    saveToList(quote)

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
    if matchResult(3, 5):
        print(str(epoch) + " - " + str(quote) + " - " + "bet even")
    else:
        print(str(epoch) + " - " + str(quote))
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