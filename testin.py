

try:

    import sys
    import os

    from fp.fp import FreeProxy
    from fake_useragent import UserAgent
    from bs4 import BeautifulSoup
    from selenium import webdriver
    from selenium.webdriver import Chrome
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.by import By
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.common.action_chains import ActionChains
    from selenium.webdriver.support import expected_conditions as ec
    from selenium.common.exceptions import TimeoutException
    import time
    import re

    print('all module are loaded ')

except Exception as e:

    print("Error ->>>: {} ".format(e))


class Spoofer(object):

    def __init__(self, country_id=['NL'], rand=True, anonym=True):
        self.country_id = country_id
        self.rand = rand
        self.anonym = anonym
        self.userAgent, self.ip = self.get()

    def get(self):
        ua = UserAgent()
        proxy = FreeProxy(country_id=self.country_id, rand=self.rand, anonym=self.anonym).get()
        # ip = proxy.split("://")[1]
        ip = '20.81.106.180:8888'


        return ua.random, ip


class DriverOptions(object):

    def __init__(self):

        self.options = Options()
        self.options.add_argument('--no-sandbox')
        self.options.add_argument('--start-maximized')
        # self.options.add_argument('--start-fullscreen')
        self.options.add_argument('--single-process')
        self.options.add_argument('--disable-dev-shm-usage')
        self.options.add_argument("--incognito")
        self.options.add_argument('--disable-blink-features=AutomationControlled')
        self.options.add_argument('--disable-blink-features=AutomationControlled')
        self.options.add_experimental_option('useAutomationExtension', False)
        self.options.add_experimental_option("excludeSwitches", ["enable-automation"])
        self.options.add_argument("disable-infobars")

        self.helperSpoofer = Spoofer()

        self.options.add_argument('user-agent={}'.format(self.helperSpoofer.userAgent))
        self.options.add_argument('--proxy-server=%s' % self.helperSpoofer.ip)


class WebDriver(DriverOptions):

    def __init__(self, path='C:\\Users\\AA\\Desktop\\chromedriver.exe'):
        DriverOptions.__init__(self)
        self.driver_instance = self.get_driver()

    def get_driver(self):

        print("""
        IP:{}
        UserAgent: {}
        """.format(self.helperSpoofer.ip, self.helperSpoofer.userAgent))

        PROXY = self.helperSpoofer.ip
        webdriver.DesiredCapabilities.CHROME['proxy'] = {
            "httpProxy":PROXY,
            "ftpProxy":PROXY,
            "sslProxy":PROXY,
            "noProxy":None,
            "proxyType":"MANUAL",
            "autodetect":False
        }
        webdriver.DesiredCapabilities.CHROME['acceptSslCerts'] = True

        path = os.path.join(os.getcwd(), 'C:\\Users\\AA\\Desktop\\chromedriver.exe')

        driver = webdriver.Chrome(executable_path=path, options=self.options)
        driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
            "source":
                "const newProto = navigator.__proto__;"
                "delete newProto.webdriver;"
                "navigator.__proto__ = newProto;"
        })

        return driver


def main():

    driver= WebDriver()
    driverinstance = driver.driver_instance
    driverinstance.get("https://www.kickstarter.com/projects/devonianapps/1733357548/edit/rewards")
    
    wait = WebDriverWait(driverinstance, 15)
    wait.until(ec.visibility_of_element_located((By.ID, "user_session_email")))

    email = driverinstance.find_element_by_id('user_session_email')
    email.send_keys('mammothinteractive@gmail.com')

    time.sleep(1)

    password = driverinstance.find_element_by_id('user_session_password')
    password.send_keys('useablebrowngeranium')

    time.sleep(2)

    password.send_keys(Keys.ENTER)
    for i in range(0,3):
        time.sleep(10)
        checkNumber = driverinstance.find_element_by_xpath('//*[@id="app"]/div[3]/div[1]/div[2]/div[1]/div/div[4]/div[1]/div[2]/div/div[3]')
        check = str(checkNumber.text)
        x = re.findall('[0-9]+', check)
        a = int(x[0])
        b = int(x[1])
        if a < 9 and a == 8 :
            b = b+1
        elif a == 7:
            b = b+2
        elif a == 6:
            b = b+3
        elif a == 5:
            b = b+4
        elif a == 4:
            b = b+5
        elif a == 3:
            b = b+6    
        elif a == 2:
            b = b+7
        else:
            pass

        print(b)

        driverinstance.find_element_by_xpath('//*[@id="app"]/div[3]/div[1]/div[2]/div[1]/div/div[4]/div[2]/div[2]/div/button[1]/span').click()
        time.sleep(5)

        backertLimit = driverinstance.find_element_by_id('backer-limit')
        backertLimit.send_keys(Keys.CONTROL + 'a')
        backertLimit.send_keys(b)
        
        time.sleep(3)


        driverinstance.find_element_by_xpath('//*[@id="app"]/div[1]/nav/div[2]/div/span[2]/button').click()

        time.sleep(60)
        driverinstance.refresh()



if __name__ == "__main__":
    main()