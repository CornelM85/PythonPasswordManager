import time
import keyboard
import os
import requests
import psutil
import urllib.request
from selenium import webdriver
from pywinauto import Application
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class Browser:
    BROWSERS = ['msedge.exe', 'chrome.exe', 'firefox.exe']

    def __init__(self):
        if self.set_name() is None:
            self.open()

        else:
            self.browser = self.set_name()

    def get_name(self):
        browsers_running = set()
        for process in psutil.process_iter():
            for browser in self.BROWSERS:
                if browser in process.name():
                    browsers_running.add(browser)

        if len(browsers_running) > 1:
            return list(browsers_running)
        elif len(browsers_running) == 1:
            return list(browsers_running)
        else:
            return None

    def get_path(self):
        for root, dirs, files in os.walk('C:\\'):
            for file in files:
                if file.endswith(self.browser):
                    path = root + '\\'
                    return path

    def get_cmd_line(self):
        for process in psutil.process_iter():
            if self.browser in process.name():
                for arg in process.cmdline():
                    if arg == '--remote-debugging-port=8989':
                        return True

    def set_name(self):
        choice = ''
        if self.get_name() is None:
            self.browser = 'msedge.exe'

        elif len(self.get_name()) > 1:
            print(f'Choose a browser from list: {self.get_name()}')
            for i, element in enumerate(self.get_name()):
                print(f'{i} for {element}')

            while choice == '':
                choice = input('Your choice: ')

            print(self.get_name()[int(choice)])
            return self.get_name()[int(choice)]

        else:
            return self.get_name()[0]

    def open(self):
        browser = Application(backend='uia')
        browser.start(
            cmd_line=fr"{self.get_path() +
                         self.browser} --remote-debugging-port=8989 --user-dir-profile=Default --start-maximized")

    def kill_process(self):
        for process in psutil.process_iter():
            try:
                if self.browser in process.name():
                    process.kill()
            except psutil.NoSuchProcess:
                pass

        else:
            self.open()
            time.sleep(1)
            keyboard.send('ctrl+shift+t')

    def get_url(self):
        browsers = ['Chrome', 'Edge', 'Firefox']

        for browser in browsers:
            if browser in self.get_path():
                browser_app = Application(backend='uia')

                browser_app.connect(title_re=f".*{browser}.*")

                dlg = browser_app.top_window()

                url = dlg.child_window(control_type="Edit", found_index=0).get_value()

                if 'login' in url:

                    return url

                else:
                    return 'Not a login page!'

    def __set_driver(self, headless=False):

        if self.browser == 'msedge.exe':
            options = webdriver.EdgeOptions()
            if headless is True:
                options.add_argument('--headless')
            else:
                options.add_experimental_option('debuggerAddress', 'localhost:8989')
            driver = webdriver.Edge(options=options)

        elif self.browser == 'chrome.exe':
            options = webdriver.ChromeOptions()
            if headless is True:
                options.add_argument('--headless')
            else:
                options.add_experimental_option('debuggerAddress', 'localhost:8989')
            driver = webdriver.Chrome(options=options)

        elif self.browser == 'firefox.exe':
            options = webdriver.FirefoxOptions()
            if headless is True:
                options.add_argument('--headless')
            driver = webdriver.Firefox(options=options)
        else:
            return NotImplementedError

        return driver

    def go_to_url(self, url: str):

        if self.get_cmd_line() is True:
            driver = self.__set_driver()
            driver.switch_to.new_window('tab')

        else:
            self.kill_process()
            driver = self.__set_driver()
            driver.close()
            driver = self.__set_driver()
            driver.switch_to.new_window('tab')

        driver.get(url)

        for name in ['username', 'user_name', 'email', 'text']:
            nr_of_elements = len(driver.find_elements(By.CSS_SELECTOR, f"//input[type='{name}']"))
            if nr_of_elements == 1:
                driver.find_element(By.CSS_SELECTOR, f"input[type='{name}']").send_keys(Keys.CONTROL + 'A')
                driver.find_element(By.CSS_SELECTOR, f"input[type='{name}']").send_keys('username')
            elif nr_of_elements > 1:
                driver.find_element(By.XPATH, "//form[@method='post']//input[1]").send_keys(Keys.CONTROL + 'A')
                driver.find_element(By.XPATH, "//form[@method='post']//input[1]").send_keys('username')

        driver.find_element(By.CSS_SELECTOR, "input[type='password']").send_keys('123456789')

    def get_site_icon(self, url):
        driver = self.__set_driver(headless=True)
        driver.get(url)
        elements_list = driver.find_elements(By.CSS_SELECTOR, "link[rel$='icon']")
        if len(elements_list) >= 1:
            icon_url = elements_list[0].get_attribute('href')
            if not os.path.isfile(f'/Images/{self.set_icon_name(url)}'):
                r = requests.get(icon_url)
                with open(f'Images/{self.set_icon_name(url)}', 'wb') as f:
                    f.write(r.content)

        driver.quit()

    def set_icon_name(self, url):
        if 'https://www.' in url:
            url = url.removeprefix('https://www.')
        else:
            url = url.removeprefix('https://')

        for i in range(len(url)):
            if url[i] == '.':
                image_name = url[0:i] + '.png'
                return image_name
