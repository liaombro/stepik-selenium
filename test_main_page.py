from selenium.webdriver.common.by import By
from page_objects.main_page import MainPage
from page_objects.login_page import LoginPage
from page_objects.locators import MainPageLocators, LoginPageLocators

def test_guest_can_go_to_login_page(browser):
    main_page = MainPage(browser, MainPageLocators.URL)
    main_page.open()
    main_page.go_to_login_page()
    login_page = LoginPage(browser, LoginPageLocators.URL)
    login_page.should_be_login_page()
    
def test_guest_should_see_login_link(browser):
    main_page = MainPage(browser, MainPageLocators.URL)
    main_page.open()
    main_page.should_be_login_link()
