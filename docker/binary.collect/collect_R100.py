import pymongo
import websocket
import json
import time
from pymongo import MongoClient
# from pymongo import Connection


def on_open(ws):
    json_data = json.dumps({'ticks':'R_100'})
    ws.send(json_data)

def on_message(ws, message):
    response = json.loads(message)['tick']
    epoch = response['epoch']
    quote = response['quote']
    print(str(epoch) + " - " + str(quote))
    savetoDB("ticks", response)

    #print(response)

    # get current timestamp
    #timestamp1 = time.time()
    # convert from human readable date to timestamp
    #timestamp2 = int(time.mktime(time.strptime('2000-01-01 12:34:00', '%Y-%m-%d %H:%M:%S'))) - time.timezone

    # convert from timestamp to human readable date
    #localTimeString = time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.localtime(epoch))

    # Replace time.localtime with time.gmtime for GMT time.
    #gmtTimeString = time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.gmtime(epoch))

    #print(timestamp1)
    #print(localTimeString)
    #print(gmtTimeString)

    # print('ticks update: %s' % message)

def savetoDB(collectName, tickResponse):
    client = MongoClient()
    # connection = Connection("192.168.99.100", 27017)
    db = client["Binary"]
    # db = connection["Binary"]
    collection = db[collectName]
    result = collection.insert_one(tickResponse)
    # ollection.insert(tickResponse)
    # update records to db
    print(result.inserted_id)


if __name__ == "__main__":
    apiUrl = "wss://ws.binaryws.com/websockets/v3?app_id=1089"
    ws = websocket.WebSocketApp(apiUrl, on_message = on_message, on_open = on_open)
    ws.run_forever()