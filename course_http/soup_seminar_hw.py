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

all_books = []
for book in books:
        book_info = {}
        try:
            book_info['name'] = [book.h3.a['title'], url + book.find('a').get('href')]
        except:
            book_info['name'] = None
        try:
            price_info = book.find("p", {'class': "price_color"})
            book_info['price'] = float(price_info.getText()[2:])
        except:
            book_info['price'] = None
        try:
            stock_url = url + '/' + book.find("div", {'class': "image_container"}).find('a').get('href')
            stock_headers = {"User-Agent": ua.chrome}
            stock_session = requests.session()  # чтобы все работало в рамках одной сессии
            stock_response = stock_session.get(stock_url, headers=stock_headers)
            stock_soap = BeautifulSoup(stock_response.text, 'html.parser')
            stock = int(stock_soap.find("p", {'class': "instock availability"}).getText('stock').strip().split()[3].split('(')[1])
            book_info['stock'] = stock
        except:
            book_info['stock'] = None
        try:
            description = stock_soap.find('meta', attrs={'name': 'description'})['content'].split('\n')[1]
            book_info['description'] = description
        except:
            book_info['description'] = None
        all_books.append(book_info)
with open('all_books.json', 'w') as f:
    json.dump(all_books, f, indent=4)

pprint(all_books)

