from bs4 import BeautifulSoup
import requests

url = 'https://en.wikipedia.org/wiki/List_of_cancer_types'

html_text = requests.get(url).content
soup = BeautifulSoup(html_text,'lxml')
for i in soup.select('h2+ul'):
    for j in i.find_all('a'):
        print(j['href'])