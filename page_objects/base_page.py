from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.webdriver import WebDriver
class BasePage:
    def __init__(self, browser : WebDriver, url : str, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)


    def open(self):
        url = self.url
        self.browser.get(url)
        
    def is_element_present(self, locator):
        try:
            self.browser.find_element(*locator)
        except (NoSuchElementException):
            return False
        return True

    