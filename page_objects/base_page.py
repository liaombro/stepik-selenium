from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException

from page_objects.locators import BasePageLocators
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

    def is_not_element_present(self, locator, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(
                expected_conditions.presence_of_element_located(locator))
        except TimeoutException:
            return True

        return False
    
    def is_disappeared(self, locator, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).until_not(
                expected_conditions.presence_of_element_located(locator))
        except TimeoutException:
            return False

        return True

    def go_to_login_page(self):
        login_link_locator = BasePageLocators.LOGIN_LINK
        login_link = self.browser.find_element(*login_link_locator)
        login_link.click() 

    def should_be_login_link(self):
        login_link_locator = BasePageLocators.LOGIN_LINK
        assert self.is_element_present(login_link_locator), "Login link is not presented"

    