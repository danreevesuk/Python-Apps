import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome('C:\\Users\\AA\\Desktop\\chromedriver.exe')


driver.maximize_window()
driver.get('http://www.bestlifecentral.com/admin/')
search_box = driver.find_element_by_id("username")
search_box.send_keys('steve')
search_box = driver.find_element_by_id("password")
search_box.send_keys('skyforcE7')
search_box.send_keys(Keys.ENTER)
time.sleep(3) 
# search_box.send_keys(Keys.ESCAPE)
webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
time.sleep(2) 


Subscribed_List = []
BestLife_ID_List = []
Name_List = []
Last_Name_List = []
Joint_Owner_List = []
Direct_Sponsor_List = []
Site_ID_List = []

Ship_Country_List = []
Ship_Street_Address_List = []
Ship_Apartment_List = []
Ship_City_List = []
Ship_State_List = []
Ship_Zip_List = []

Auto_ship_date_List = []
Autoship_List = []

Telephone_List = []
Cellphone_List = []
Email_List = []
Country_List = []
Street_Address_List = []
Apartment_List = []
City_List = []
State_List = []
Zip_List = []


for L in range(400,1,-1):
    driver.get('http://www.bestlifecentral.com/admin/users/usersList/?page='+str(L))
    time.sleep(1) 

    i = 1
    try:
        pass
        while i < 21:
            i = str(i)
            driver.find_element_by_xpath('//*[@id="sort-table"]/tbody/tr['+ i +']/td[6]/a[1]/span').click()

            #BESTLIFE INFO

            Subscribed = driver.find_element_by_xpath('//*[@id="page-content-wrapper"]/div[2]/div/div[2]/div[1]/div/ul/li[1]/div/input').get_attribute('value')
            BestLife_ID = driver.find_element_by_xpath('//*[@id="bestlife_information_form"]/ul/li[1]/div/input').get_attribute('value')
            Name = driver.find_element_by_xpath('//*[@id="bestlife_information_form"]/ul/li[2]/div/input').get_attribute('value')
            Last_Name = driver.find_element_by_xpath('//*[@id="bestlife_information_form"]/ul/li[3]/div/input').get_attribute('value')
            Joint_Owner = driver.find_element_by_xpath('//*[@id="bestlife_information_form"]/ul/li[4]/div/input').get_attribute('value')
            Direct_Sponsor = driver.find_element_by_xpath('//*[@id="bestlife_information_form"]/ul/li[5]/div/input').get_attribute('value')
            Site_ID = driver.find_element_by_xpath('//*[@id="bestlife_information_form"]/ul/li[7]/div/input').get_attribute('value')

            #SHIPPING

            Ship_Country = driver.find_element_by_xpath('//*[@id="shipping_country"]').get_attribute('value')
            Ship_Street_Address = driver.find_element_by_xpath('//*[@id="page-content-wrapper"]/div[2]/div/div[1]/div[2]/div/form/ul/li[2]/div/input').get_attribute('value')
            Ship_Apartment = driver.find_element_by_xpath('//*[@id="page-content-wrapper"]/div[2]/div/div[1]/div[2]/div/form/ul/li[3]/div/input').get_attribute('value')
            Ship_City = driver.find_element_by_xpath('//*[@id="page-content-wrapper"]/div[2]/div/div[1]/div[2]/div/form/ul/li[4]/div/input').get_attribute('value')
            Ship_State = driver.find_element_by_xpath('//*[@id="page-content-wrapper"]/div[2]/div/div[1]/div[2]/div/form/ul/li[5]/div/input').get_attribute('value')
            Ship_Zip = driver.find_element_by_xpath('//*[@id="page-content-wrapper"]/div[2]/div/div[1]/div[2]/div/form/ul/li[6]/div/input').get_attribute('value')

            #AUTOSHIP

            Auto_ship_date = driver.find_element_by_xpath('//*[@id="page-content-wrapper"]/div[2]/div/div[2]/div[1]/div/ul/li[8]/div/input').get_attribute('value')
            Autoship = driver.find_element_by_xpath('//*[@id="page-content-wrapper"]/div[2]/div/div[2]/div[1]/div/ul/li[9]/div/input').get_attribute('value')

            #CONTACT INFORMATION

            Telephone = driver.find_element_by_xpath('//*[@id="phone"]').get_attribute('value')
            Cellphone = driver.find_element_by_xpath('//*[@id="mobile"]').get_attribute('value')
            Email = driver.find_element_by_xpath('//*[@id="page-content-wrapper"]/div[2]/div/div[3]/div[1]/div/form/ul/li[3]/div/input').get_attribute('value')
            Country = driver.find_element_by_xpath('//*[@id="country"]').get_attribute('value')
            Street_Address = driver.find_element_by_xpath('//*[@id="page-content-wrapper"]/div[2]/div/div[3]/div[1]/div/form/ul/li[5]/div/input').get_attribute('value')
            Apartment = driver.find_element_by_xpath('//*[@id="page-content-wrapper"]/div[2]/div/div[3]/div[1]/div/form/ul/li[6]/div/input').get_attribute('value')
            City = driver.find_element_by_xpath('//*[@id="page-content-wrapper"]/div[2]/div/div[3]/div[1]/div/form/ul/li[7]/div/input').get_attribute('value')
            State = driver.find_element_by_xpath('//*[@id="page-content-wrapper"]/div[2]/div/div[3]/div[1]/div/form/ul/li[8]/div/input').get_attribute('value')
            Zip = driver.find_element_by_xpath('//*[@id="page-content-wrapper"]/div[2]/div/div[3]/div[1]/div/form/ul/li[9]/div/input').get_attribute('value')


        # ====================================

            for L in range(int(i)):
                data1 = Subscribed_List.append(Subscribed)
                data2 = BestLife_ID_List.append(BestLife_ID)
                data3 = Name_List.append(Name)
                data4 = Last_Name_List.append(Last_Name)
                data5 = Joint_Owner_List.append(Joint_Owner)
                data6 = Direct_Sponsor_List.append(Direct_Sponsor)
                data7 = Site_ID_List.append(Site_ID)

                data8 = Ship_Country_List.append(Ship_Country)
                data9 = Ship_Street_Address_List.append(Ship_Street_Address)
                data10 = Ship_Apartment_List.append(Ship_Apartment)
                data11 = Ship_City_List.append(Ship_City)
                data12 = Ship_State_List.append(Ship_State)
                data13 = Ship_Zip_List.append(Ship_Zip)

                data14 = Auto_ship_date_List.append(Auto_ship_date)
                data15 = Autoship_List.append(Autoship)

                data16 = Telephone_List.append(Telephone)
                data17 = Cellphone_List.append(Cellphone)
                data18 = Email_List.append(Email)
                data19 = Country_List.append(Country)
                data20 = Street_Address_List.append(Street_Address)
                data21 = City_List.append(City)
                data22 = State_List.append(State)
                data23 = Zip_List.append(Zip)



                user = {'Subscribed date': Subscribed_List,
                    'BestLife ID':BestLife_ID_List,
                    'Name':Name_List,
                    'Last_Name':Last_Name_List,
                    'Joint_Owner':Joint_Owner_List,
                    'Direct_Sponsor':Direct_Sponsor_List,
                    'Site_ID':Site_ID_List,
                    'Ship_Country':Ship_Country_List,
                    'Ship_Street_Address':Ship_Street_Address_List,
                    'Ship_Apartment':Ship_Apartment_List,
                    'Ship_City':Ship_City_List,
                    'Ship_State':Ship_State_List,
                    'Ship_Zip':Ship_Zip_List,
                    'Auto_ship_date':Auto_ship_date_List,
                    'Autoship':Autoship_List,
                    'Telephone':Telephone_List,
                    'Cellphone':Cellphone_List,
                    'Email':Email_List,
                    'Country':Country_List,
                    'Street_Address':Street_Address_List,
                    'City':City_List,
                    'State':State_List,
                    'Zip':Zip_List
                    }
                break

            driver.back()
            i = int(i)
            i = i+1
    except NoSuchElementException:
        continue
    df = pd.DataFrame(user, columns= ['Subscribed date','BestLife ID','Name','Last_Name','Joint_Owner','Direct_Sponsor','Site_ID','Ship_Country','Ship_Street_Address','Ship_Apartment','Ship_City','Ship_State','Ship_Zip','Auto_ship_date','Autoship','Telephone','Cellphone','Email','Country','Street_Address','City','State','Zip'])
    df.to_csv (r'C:\Users\AA\Desktop\Scrape.csv', index = False, header=True)
    # print(df)

    time.sleep(5)


