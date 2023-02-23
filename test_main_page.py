import pytest

from selenium.webdriver.common.by import By
from page_objects.basket_page import BasketPage
from page_objects.main_page import MainPage
from page_objects.login_page import LoginPage
from page_objects.locators import BasketPageLocators, MainPageLocators, LoginPageLocators, ProductPageLocators
from page_objects.product_page import ProductPage

@pytest.mark.login_guest
class TestLoginFromMainPage:
    def test_guest_can_go_to_login_page(self, browser):
        main_page = MainPage(browser, MainPageLocators.URL)
        main_page.open()
        
        main_page.go_to_login_page()
        
        login_page = LoginPage(browser, LoginPageLocators.URL)
        login_page.should_be_login_page()
        
    def test_guest_should_see_login_link(self, browser):
        main_page = MainPage(browser, MainPageLocators.URL)
        
        main_page.open()
        
        main_page.should_be_login_link()

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    main_page = MainPage(browser, MainPageLocators.URL)
    main_page.open()
    
    main_page.go_to_basket_page()
    
    basket_page = BasketPage(browser, BasketPageLocators.URL)
    basket_page.should_be_empty_cart()
    
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    product_page = ProductPage(browser, ProductPageLocators.URL)
    product_page.open()
    
    product_page.go_to_basket_page()
    
    basket_page = BasketPage(browser, BasketPageLocators.URL)
    basket_page.should_be_empty_cart()