from pymongo import MongoClient
from pprint import pprint
from pymongo.errors import *

client = MongoClient('localhost', 27017)
db = client['users']
# persons = db.persons
# dublicates = db.dublicates


# doc = {'_id': 'a39r49r3t43jitrjiu',
#        'author': 'Peter',
#        'age': 38,
#        'text': 'is cool! Wilberrry',
#        'tags': ['cool', 'hot', 'ice'],
#        'date': '14.06.1983'}

# try:
#     persons.insert_one(doc)
# except DuplicateKeyError as e:
#     dublicates.insert_one(doc)

# если использовать persons.insert_many(doc), то работа закончится на элементе с ошибкой, поэтому лучше использвать one

# for doc in persons.find():
#     pprint(doc)

# for doc in dublicates.find():
#     pprint(doc)

# result = persons.find()
# print(result)

# for doc in persons.find({"$or": [{'author': 'Peter'}, {'age': 28}]}):
#     pprint(doc)
# for doc in persons.find({'age': {'$gt': 30}}):
#     pprint(doc)
# регулярные выражения:
# for doc in persons.find({'author': {'$regex': 'P.'}}).sort("age", -1): # -1 сортироовка по убыванию
#     pprint(doc)

# persons.update_one({'author': 'Peter'}, {'$set': {'author': 'Petya'}})
# persons.replace_one({'author': 'Petya'}, {'author': 'Peter'})
# persons.delete_one({'author': 'Petya'})

# for doc in persons.find():
#     pprint(doc)



