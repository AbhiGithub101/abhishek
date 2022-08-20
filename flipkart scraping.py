from bs4 import BeautifulSoup
import requests
import pandas as pd

flipkart = {}
name_list = []
price_list = []
rating_list = []

for page in range(1,10):
    url = f'https://www.flipkart.com/search?q=phone&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page={page}'

    response_code = requests.get(url)
    html_text = response_code.content

    soup = BeautifulSoup(html_text,'lxml')

    #scraping
    phones = soup.find_all('div','_3pLy-c row')

    for phone in phones:
        name = phone.find('div','_4rR01T').get_text()
        price = int(phone.find('div','_30jeq3 _1_WHN1').get_text().replace('₹','').replace(',',''))
        rating = phone.find('div','_3LWZlK')
        if(rating==None):
            rating = 0
        else:
            rating = float(rating.get_text())
        name_list.append(name)
        price_list.append(price)
        rating_list.append(rating)


flipkart['Name'] = name_list
flipkart['Price'] = price_list
flipkart['Rating'] = rating_list

flpkrt = pd.DataFrame(flipkart,columns=['Name','Price','Rating'])
flpkrt.to_csv('Flipkart.csv')

