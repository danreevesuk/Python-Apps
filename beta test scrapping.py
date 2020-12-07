import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.chrome.options import Options


driver = webdriver.Chrome('C:\\Users\\AA\\Desktop\\chromedriver.exe')
driver.maximize_window()
driver.get('http://www.bestlifecentral.com/admin/')
search_box = driver.find_element_by_id("username")
search_box.send_keys('steve')
search_box = driver.find_element_by_id("password")
search_box.send_keys('skyforcE7')
search_box.send_keys(Keys.ENTER)
time.sleep(5) 
# search_box.send_keys(Keys.ESCAPE)
webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
time.sleep(2) 

driver.find_element_by_link_text("Active Associates").click()
time.sleep(1) 
driver.find_element_by_css_selector("a.tooltip").click()
time.sleep(1)
label = driver.find_elements_by_tag_name("label")
inp = driver.find_elements_by_tag_name("input")
# d = dict(zip(label, inp))


for labels,inps in zip(label,inp):
    if labels.text == 'Preferred language' or labels.text == 'Password' or labels.text == 'Current Photo' or labels.text =='Change Photo' or labels.text == 'Country':
        continue 

    print(labels.text,':',inps.get_attribute('value'))





time.sleep(10) 
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)


# for labels in label:
#     print(labels.text)
# for inps in inp:
#     print(inps.get_attribute('value'))




# element_text = inp.text
# element_attribute_value = inp.get_attribute('value')

# print (inp)
# print ('inp.text: {0}'.format(element_text))
# print ('inp.get_attribute(\'value\'): {0}'.format(element_attribute_value))



# base = 'http://www.bestlifecentral.com/admin/user/edit/31987'

# headers = {
#     'user-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
# }

# r = requests.get(f'http://www.bestlifecentral.com/admin/user/edit/31987')

# soup = BeautifulSoup(r.content, 'lxml')
# form = soup.find('form')
# find = form.find('input')
# print(find)


# form = BeautifulSoup.find('form')
# print(form.find_all('input'))


# for x in range(1,10):
#     r = requests.get(f'https://onlinevetpharmacy.com/product-category/accessories/page/{x}')

#     soup = BeautifulSoup(r.content, 'lxml')
#     productlist = soup.find_all('div', class_='caption')


#     for item in productlist:
#         for price in item.find_all('span', class_='price'):
#                     print(price.text)


# search_box.send_keys(Keys.ENTER)
# time.sleep(2) 
# driver.find_element_by_link_text("Sorry, this brand doesn't deliver here").click()
# time.sleep(10) 
# driver.find_element_by_css_selector('div.CategoriesList_CategoryView__Container__3Wf33').click()
# time.sleep(2) 
# driver.find_element_by_css_selector('div.radiocontrol_indicator').click()
# driver.find_element_by_tag_name('textarea').send_keys('HA HA HA! I AM A BOT SEND ME FOOOOD')
# time.sleep(3) 
# driver.find_element_by_css_selector("button.button.button--default.undefined.undefined").click()
# driver.find_element_by_link_text("LOGIN TO CHECKOUT").click()
# time.sleep(2) 
# email= driver.find_element_by_id("email").send_keys('sma3797@gmail.com')
# password = driver.find_element_by_id("password").send_keys('asdasd') 
# time.sleep(6) 
# driver.find_element_by_css_selector("button.button.button--default.undefined.undefined").click()
# time.sleep(5) 
# driver.find_element_by_class_name('DeliveryAddress_SavedCards__2mAqG').click()
# time.sleep(5) 
# driver.find_element_by_css_selector("div.Subtotal_Subtotal_Button__atNYU").click()
