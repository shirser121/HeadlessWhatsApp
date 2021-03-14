from selenium import webdriver
import pathlib
import os
import re


class RunHeadless:
    def apdata_path(self):
        username = self.__dir_name
        if os.name == 'nt':  # ווינדוס
            apdata = os.getenv('APPDATA')
            user_dir = "user-data-dir=" + \
                       re.findall(".+.\Dta\D", apdata)[0] + \
                       r'Local\Chromium\User Data\Default\{0}'.format(username)
            user_dir = user_dir.replace("\\", "\\" * 2)
        else:  # other (unix)
            path = str(pathlib.Path().absolute())
            user_dir = 'user-data-dir={0}/{1}'.format(path, username)

        return user_dir

    #   אם רוצים להריץ headless
    def chrome_driver(self, user_agent=0):
        usr_path = self.apdata_path()
        options = webdriver.ChromeOptions()
        if user_agent != 0:
            options.add_argument('--headless')
            options.add_argument('--hide-scrollbars')
            options.add_argument('--disable-gpu')
            options.add_argument("--log-level=3")
            options.add_argument('--user-agent={}'.format(user_agent))
        options.add_argument('--no-sandbox')
        options.add_argument(usr_path)
        driver = webdriver.Chrome(options=options)
        return driver

    #   מקבל את הנתונים של המשתמש כדי שיהיה אפשר להפעיל בלי שפותחים כרום פיזי
    def whatsapp_QR(self, level):
        driver = self.chrome_driver()
        user_agent = driver.execute_script("return navigator.userAgent;")
        driver.get("https://web.whatsapp.com/")
        if level == "0":
            print("Scan QR Code, And then Enter")
            input()
        print("Logged In")
        driver.close()
        return user_agent

    def get_browser(self):
        return self.__browser

    def __init__(self, level="0"):
        if level == "0":
            print("The current user dir is 'selenium'")
            print("To keep this dir [1], for Default [2], for else enter dir name")
            self.__dir_name = input()
        else:
            self.__dir_name = level

        if self.__dir_name == "1":
            self.__dir_name = "selenium"
        elif self.__dir_name == "2":
            self.__dir_name = "Default"

        user = self.whatsapp_QR(level)
        self.__browser = self.chrome_driver(user)


if __name__ == "__main__":
    obg = RunHeadless()
    browser = obg.get_browser()
    browser.get("https://web.whatsapp.com/")
    print("You have headless WhatsApp!")
    print("here the body of the page:\n" + browser.find_element_by_tag_name("body").get_attribute("innerHTML"))
    input("press enter to close")
    browser.close()
