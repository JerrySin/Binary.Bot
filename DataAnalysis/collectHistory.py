import websocket
import json
#import thread
import time
#from pymongo import MongoClient
# from pymongo import Connection


def on_open(ws):
    #def run(*args):
        #for i in range(3):
            #time.sleep(1)
            # 'Tue, 01 Nov 2016 00:00:00 +0000 - epoch: 1477972800'
    json_data = json.dumps({"ticks_history": "R_50", "end": "1477972800", "count": 10})
    ws.send(json_data)
        #time.sleep(1)
    #ws.close()
        #print("thread terminating...")
    #thread.start_new_thread(run, ())


def on_message(ws, message):
    response = json.loads(message)["history"]
    prices = response["prices"]
    times = response["times"]
    for i in range(len(prices)):
        print(str(times[i]) + " - " + str(prices[i]))
    time.sleep(1)
    epoch = 1477973800
    print("=============== {0} ===============".format(epoch))
    json_data = json.dumps({"ticks_history": "R_50", "end": epoch, "count": 10})
    ws.send(json_data)
    #ws.close()
    #savetoDB("ticks", response)
    #print(response)

def on_error(ws, error):
    print(error)


def on_close(ws):
    print("### closed ###")


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
    #websocket.enableTrace(True)
    ws = websocket.WebSocketApp(apiUrl,
                                on_message = on_message,
                                on_open = on_open,
                                on_error = on_error,
                                on_close = on_close)
    ws.run_forever()