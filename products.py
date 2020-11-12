import requests
from bs4 import BeautifulSoup
import pandas as pd


headers = {
    'user-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
}
for x in range(1,16):
    r = requests.get(f'https://onlinevetpharmacy.com/product-category/dog-cat-feed/page/{x}')

    soup = BeautifulSoup(r.content, 'lxml')
    productlist = soup.find_all('div', class_='caption')

    productslinks = []

    for item in productlist:
        for link in item.find_all('h3', class_='woocommerce-loop-product__title'):
            for name in link.find_all('a', href=True):
                for price in item.find_all('span', class_='price'):
                    print(price.text)
