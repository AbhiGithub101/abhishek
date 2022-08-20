from bs4 import BeautifulSoup
import requests
from cancerf import *

url = 'https://en.wikipedia.org/wiki/Lung_cancer#Non-small_cell_lung_carcinoma'
html_text = requests.get(url).content
soup = BeautifulSoup(html_text,'lxml')
info_box = soup.find('table',class_ = 'infobox')
info_rows = info_box.find_all('tr')

disease = {}
for index,row in enumerate(info_rows):
    if(index==0):
        disease['Cancer Type'] = row.find('th').get_text()
    else:
        content_key = '' if(row.find('th')==None) else row.find('th').get_text(" ",strip=True)
        if(content_key!=''):
            disease[content_key] = get_content_value(row.find('td'))

#get info-box for all movies

