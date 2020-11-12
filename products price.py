import requests
from bs4 import BeautifulSoup
import pandas as pd

base = 'https://onlinevetpharmacy.com/'

headers = {
    'user-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
}
for x in range(1,10):
    r = requests.get(f'https://onlinevetpharmacy.com/product-category/accessories/page/{x}')

    soup = BeautifulSoup(r.content, 'lxml')
    productlist = soup.find_all('div', class_='caption')


    for item in productlist:
        for price in item.find_all('span', class_='price'):
                    print(price.text)
