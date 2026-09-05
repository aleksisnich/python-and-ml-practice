import csv

from lxml import html
import requests
from pprint import pprint
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['post']
info = db.info

full_link = []
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0"}
url = "https://gb.ru"
response = requests.get(url + '/posts', headers=header)
# создаем дерево
dom = html.fromstring(response.text)
post_list = []
post = dom.xpath("//div[@class='post-item event']")
for posts in post:
    post_info = {}
    name = ''.join(posts.xpath(".//a[@class='post-item__title h3 search_text']/text()"))
    link = ''.join([url] + posts.xpath(".//a[@class='post-item__title h3 search_text']/@href"))
    views = ''.join(posts.xpath('.//div/*[name() = "svg" and @class="svg-icon icon-views-mini "]/following-sibling::span/text()'))
    date = ''.join(posts.xpath('.//div[@class="small m-t-xs"]/text()'))
    comments = ''.join(posts.xpath(".//div/*[name() = 'svg' and @class='svg-icon icon-comments-mini ']/following-sibling::span/text()"))
    description = ''.join(posts.xpath(".//div[@class='small search_text post-description']/span/text()"))
    post_info['name'] = name
    post_info['link'] = link
    post_info['date'] = date
    post_info['views'] = views
    post_info['comments'] = comments
    post_info['description'] = description
    post_list.append(post_info)

for post in post_list:
        info.insert_one(post)

# with open('post_gb.csv', 'w') as f:
#     csv.writer(f).writerow(post_list)

pprint(post_list)