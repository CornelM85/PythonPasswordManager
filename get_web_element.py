from selenium import webdriver


class GetElement:

    def __init__(self):
        self.driver = webdriver.Edge()

    def get_url(self):
        return self.driver.current_url
