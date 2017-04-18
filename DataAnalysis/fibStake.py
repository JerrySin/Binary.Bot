import json
import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# import pprint
# from odo import odo

# data = odo('mongodb://localhost/db::collection', pd.DataFrame)
# Environment variables 
# host = "127.0.0.1"
# port = "27017"
fromDate = "2017-03-20 12:00:00"
ts = int(time.mktime(time.strptime(fromDate, '%Y-%m-%d %H:%M:%S'))) - time.timezone
#query = {"epoch":{"$gt":ts}}
query = {}
# uniqueKey = "epoch"
skipRecords = 0
limitRecords = 2000
# '%Y-%m-%d %H:%M:%S'

def normal(n, amount):
    result = []
    for i in range(n):
        result.append([i, i * amount])
    print(result)
    return result

def fib(n, amount):
    result = []
    a, b = 0, 1        
    while a < n:
        result.append(a * amount)
        a, b = b, a+b
    print(result)
    return result




def ploting():
    # Expand the cursor and construct the DataFrame
    plotingData = []
    # result = read_plotingData(query, skipRecords, limitRecords)
    for r in read_plotingData(query, skipRecords, limitRecords):
        plotingData.append(float(r['quote']))
    
    # result = json.loads(result)
    # pprint.pprint(list(result))
    print(plotingData)

    #df = pd.read_json(list(result))
    #df = pd.DataFrame(list(result))
    df = pd.DataFrame(plotingData)
    # Delete the _id
    # if no_id:
    #del df['_id']

    df.plot()
    plt.show()
# ticks = db[collectionName]

# result = db[collectionName].create_index([(uniqueKey, pymongo.ASCENDING)], unique=True)
#sorted(list(db[collectionName].index_information()))





# def readData():
    
#     # convert from human readable date to timestamp
#     # ts = int(time.mktime(time.strptime(fromDate, '%Y-%m-%d %H:%M:%S'))) - time.timezone
#     # query = ticks.find({"epoch":{"$gt":ts}}).sort("epoch")

#     query = ticks.find().limit(returnRecords).sort("epoch")
#     plotCollection = query
#     with open("test.txt","w") as f:
#         f.write(str(query))

#     # print(plotCollection)
#     for p in plotCollection:
#         pprint.pprint(p)
    #df = pd.read_json(plotCollection, typ='series')
    #print(df)
    # df['quote'].plot()
    # plt.show()

# def get(tick_id):
#     tick = ticks.find_one({'_id':ObjectId(tick_id)})

# def printData():
#     df = pd.read_csv("Volatility 100 Index (1t).csv")
#     print df.head(10)

#     print "\nMax Index:"
#     print get_max_index(df)
#     print "\nMin Index:"
#     print get_min_index(df)
#     print "\nDifference:"
#     print get_diff_index(df)
#     print "\nMean Index:"
#     print get_mean_index(df)

#     df['Volatility 100 Index'].plot()
#     plt.show()

# def get_max_index(df1):
#     return df1['Volatility 100 Index'].max()

# def get_min_index(df1):
#     return df1['Volatility 100 Index'].min()

# def get_diff_index(df1):
#     return abs(df1['Volatility 100 Index'].max()-df1['Volatility 100 Index'].min())

# def get_mean_index(df1):
#     return df1['Volatility 100 Index'].mean()


def _connect_mongo(host, port, username, password, db):
    """ A util for making a connection to mongo """
    if username and password:
        mongo_uri = 'mongodb://%s:%s@%s:%s/%s' % (username, password, host, port, db)
        conn = MongoClient(mongo_uri)
    else:
        conn = MongoClient(host, port)

    return conn[db]


def read_mongo(db, collection, query={}, host='localhost', port=27017, username=None, password=None, no_id=True):
    """ Read from Mongo """
    # Connect to MongoDB
    db = _connect_mongo(host=host, port=port, username=username, password=password, db=db)

    # Make a query to the specific DB and Collection
    cursor = db[collection].find(query)

    return cursor


def read_plotingData(query, skip, limit, db='Binary', collection = 'ticks'):
    """ Read from Mongo with condition """
    cursor = read_mongo(db, collection, query).skip(skip).limit(limit)

    return cursor

if __name__ == "__main__":
    #ploting()
    df = pd.DataFrame({'Fib':fib(30,64), 'Normal':normal(9,64)}, columns=['Fib', 'Normal'])

    df.plot()
    #plt.xlim(0, 16)
    plt.xticks(range(0,8,1))
    #plt.xscale('symlog')
    plt.xlabel('time(h)')
    plt.ylabel('profit')
    plt.title('Fibonacci')
    plt.show()
    
