import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from pprint import pprint

ua = UserAgent()
# url = "https://gb.ru/posts"
url = "https://gb.ru"
headers = {"User-Agent": ua.chrome}
params = {'page': 1}
session = requests.session() # чтобы все работало в рамках одной сессии

all_posts = []
while True:
    response = session.get(url + "/posts", params=params, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    posts = soup.find_all('div', {'class': 'post-item'})
    if not posts:
        break
    for post in posts:
        post_info = {}
        try:
            name_info = post.find("div", {'class': "text-left v-padder m-r m-l"}).findChildren()[0]
            post_info['name'] = [name_info.getText(), url + name_info.get('href')]

        except:
            post_info['name'] = None
        try:
            date_info = post.find("div", {'class': "small m-t-xs"})
            post_info['date'] = date_info.getText()
        except:
            post_info['date'] = None
        try:
            description_info = post.find("div", {'class': "m-t-sm"}).findChildren()[0]
            post_info['description'] = description_info.getText()
        except:
            post_info['description'] = None

        all_posts.append(post_info)
    print(f"Обработана {params['page']} страница")
    params['page'] += 1

pprint(all_posts)

