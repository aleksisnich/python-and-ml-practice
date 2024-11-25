import requests
import useragent
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from pprint import pprint

ua = UserAgent()
# url = "https://www.boxofficemojo.com/intl/?ref_=bo_nb_hm_tab"
url = "https://www.boxofficemojo.com"
headers = {"User-Agent": ua.chrome}
params = {"ref_": "bo_nb_hm_tab"}
session = requests.session() # чтобы все работало в рамках одной сессии
response = session.get(url+"/intl", params=params, headers=headers)

print(response.status_code)

soup = BeautifulSoup(response.text, "html.parser")
rows = soup.find_all('tr')
films =[]
for row in rows[2:]:
    film = {}
    try:
        # area_info = row.find("td", {'class': "mojo-field-type-area_id"}).find('a')
        area_info = row.find("td", {'class': "mojo-field-type-area_id"}).findChildren()[0]
        film['area'] = [area_info.getText(), url + area_info.get('href')]
    except:
        film['area'] = None
    try:
        weekend_info = row.find("td", {'class': "mojo-field-type-date_interval"}).findChildren()[0]
        film['weekend'] = [weekend_info.getText(), url + weekend_info.get('href')]
    except:
        film['weekend'] = None
    try:
        film['realeses'] = int(row.find("td", {'class': "mojo-field-type-positive_integer"}).getText())
    except:
        film['realeses'] = None
    try:
        frelease_info = row.find("td", {'class': "mojo-field-type-release"}).findChildren()[0]
        film['frelease'] = [frelease_info.getText(), url + frelease_info.get('href')]
    except:
        film['frelease'] = None
    try:
        distributor_info = row.find("td", {'class': "mojo-field-type-studio"}).findChildren()[0]
        film['distributor'] = [distributor_info.getText(), url + distributor_info.get('href')]
    except:
        # print("Exception with frelease, object =", film['frelease'])
        film['distributor'] = None
    # film['gross'] = row.find("td", {'class': "mojo-field-type-money"}).getText()
    films.append(film)

pprint(films)


