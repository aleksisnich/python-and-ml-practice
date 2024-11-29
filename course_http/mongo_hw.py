from pymongo import MongoClient
from pymongo.errors import *
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from pprint import pprint
import json

ua = UserAgent()
# url = "https://books.toscrape.com"
url = "https://books.toscrape.com"
headers = {"User-Agent": ua.chrome}
params = {'page': 1}
session = requests.session() # чтобы все работало в рамках одной сессии
response = session.get(url, params=params, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")
books = soup.find_all('li', {'class': 'col-xs-6'})

client = MongoClient('localhost', 27017)
db = client['books']
info = db.info
count_duplicated = 0
count_book = 0

# all_books = []
# for book in books:
#         book_info = {}
#         try:
#             book_info['name'] = [book.h3.a['title'], url + book.find('a').get('href')]
#         except:
#             book_info['name'] = None
#         try:
#             price_info = book.find("p", {'class': "price_color"})
#             book_info['price'] = float(price_info.getText()[2:])
#         except:
#             book_info['price'] = None
#         try:
#             stock_url = url + '/' + book.find("div", {'class': "image_container"}).find('a').get('href')
#             stock_headers = {"User-Agent": ua.chrome}
#             # stock_session = requests.session()  # чтобы все работало в рамках одной сессии
#             stock_response = requests.get(stock_url, headers=stock_headers)
#             stock_soap = BeautifulSoup(stock_response.text, 'html.parser')
#             stock = int(stock_soap.find("p", {'class': "instock availability"}).getText('stock').strip().split()[3].split('(')[1])
#             book_info['stock'] = stock
#         except:
#             book_info['stock'] = None
#         try:
#             description = stock_soap.find('meta', attrs={'name': 'description'})['content'].split('\n')[1]
#             book_info['description'] = description
#         except:
#             book_info['description'] = None
#         all_books.append(book_info)


# for book in all_books:
#     try:
#         info.insert_one(book)
#         count_book += 1
#     except:
#         count_duplicated += 1
#         print(book)
#     pprint(book)
#
# print("Количество книг: ", count_book)
# print("Количество дубликатов книг: ", count_duplicated)

# Поиск книг, стоимость который больше 50
# for doc in info.find({'price': {'$gt': 50.0}}):
#     pprint(doc)

# Поиск книг по различным параметрам
# for doc in info.find({"$or": [{'name': 'A Light in the Attic'}, {'stock': 20}]}):
#     pprint(doc)

# регулярные выражения:
# for doc in info.find({'name': {'$regex': 'A'}}).sort("stock", -1): # -1 сортироовка по убыванию
#     pprint(doc)
