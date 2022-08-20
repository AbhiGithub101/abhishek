from bs4 import BeautifulSoup
import requests

def find_all_city():
    cities_list = []
    url = 'https://www.swiggy.com/'
    header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Safari/537.36 Edg/104.0.1293.54"}
    response_code = requests.get(url,headers=header)
    html_code = response_code.content
    soup = BeautifulSoup(html_code,'lxml')

    cities = soup.find_all('a','_3TjLz b-Hy9')
    for city in cities:
        city = city['href']
        link = 'https://www.swiggy.com'+city
        cities_list.append(link)
    return cities_list