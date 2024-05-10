import time
import keyboard
import os
import psutil
from selenium import webdriver
from pywinauto import Application
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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
            cmd_line=fr"{self.get_path() + self.browser} --remote-debugging-port=8989 --user-dir-profile=Default --start-maximized")

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

                return url

    def __set_driver(self):

        if self.browser == 'msedge.exe':
            options = webdriver.EdgeOptions()
            options.add_experimental_option('debuggerAddress', 'localhost:8989')
            driver = webdriver.Edge(options=options)

        elif self.browser == 'chrome.exe':
            options = webdriver.ChromeOptions()
            options.add_experimental_option('debuggerAddress', 'localhost:8989')
            driver = webdriver.Chrome(options=options)

        elif self.browser == 'firefox.exe':
            options = webdriver.FirefoxOptions()
            driver = webdriver.Firefox(options=options)
        else:
            return NotImplementedError

        return driver

    def go_to_url(self, url: str):

        if self.get_cmd_line() is True:
            driver = self.__set_driver()
            driver.switch_to.new_window('tab')
            driver.get(url)

        else:
            self.kill_process()
            driver = self.__set_driver()
            driver.close()
            driver = self.__set_driver()
            driver.switch_to.new_window('tab')
            driver.get(url)

    def get_site_login_user(self):
        url = self.get_url()
        driver = self.__set_driver()
        driver.get(url)
        validate = WebDriverWait(driver, timeout=2).until(EC.presence_of_element_located((By.ID, 'username')))

        return validate.is_displayed()
