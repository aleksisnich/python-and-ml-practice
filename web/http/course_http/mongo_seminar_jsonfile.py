# import requests
# response = requests.get("https://gbcdn.mrgcdn.ru/uploads/asset/5560965/attachment/357f7ccb20abaeedb8ccfda8e1045098.json")
#
# with open('data.json', 'wb') as f:
#     f.write(response.content)

from pymongo import MongoClient
from pprint import pprint
from pymongo.errors import *
import json

client = MongoClient('localhost', 27017)
db = client['crashes']
info = db.info
count_duplicated = 0

with open("crash-data.json", "r") as f:
    data = json.load(f)

for feature in data['features']:
    _id = feature.get('properties').get('tamainid')
    try:
        info.insert_one(feature)
    except:
        count_duplicated += 1
        print(feature)
print(count_duplicated)

# count = info.count_documents({})

# for doc in info.find({'properties.lat': {'$gt': 35.0, '$lt': 36.0},
#                       'properties.lon': {'$gt': -79.0, '$lt': -78.0}}):
#     pprint(doc)

# for doc in info.find({'properties.lat': {'$gt': 35.0, '$lt': 36.0}}):
#     pprint(doc)


