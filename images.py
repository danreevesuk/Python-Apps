import urllib
import urllib.request
from bs4 import BeautifulSoup
import os
from string import ascii_lowercase
i=1
def make_soup(url):
    thepage= urllib.request.urlopen(url)
    soupdata = BeautifulSoup(thepage, "html.parser")
    return soupdata


for x in range(1,16):

    soup = make_soup(f"https://onlinevetpharmacy.com/product-category/dog-cat-feed/page/{x}")
    for img in soup.findAll('img'):
        temp=img.get('src')
        if temp[:1]=="/":
            image = "https://onlinevetpharmacy.com/" + temp
        else:
            image = temp

        print(image)

        nametemp = img.get('alt')
        if len(nametemp)==0:
            filename=str(i)
            i=i+1
        else:
            filename=nametemp


        imagefile = open(filename + ".jpeg", 'wb')
        imagefile.write(urllib.request.urlopen(image).read())
        imagefile.close()