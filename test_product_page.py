from pages.product_page import ProductPage
from pages.login_page import LoginPage
from pages.locators import ProductPageLocators, LoginPageLocators

import pytest
from faker import Faker

URL_LIST = ProductPageLocators.URL_LIST
URL_LIST[6] = pytest.param(URL_LIST[6], marks=pytest.mark.xfail) 
@pytest.mark.parametrize('link', ProductPageLocators.URL_LIST)

def test_guest_can_add_product_to_basket(browser, link):
    product_page = ProductPage(browser, link)
    product_page.open()
    
    product_page.add_product_to_cart()
    
    product_page.should_be_success_message()
    product_page.cart_total_should_be_equal_to_product_price()
    
@pytest.mark.xfail    
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    product_page = ProductPage(browser, ProductPageLocators.URL)
    product_page.open()
    
    product_page.add_product_to_cart()
    
    product_page.is_not_element_present(ProductPageLocators.SUCCESS_MESSAGE)
    
def test_guest_cant_see_success_message(browser):
    product_page = ProductPage(browser, ProductPageLocators.URL)
    
    product_page.open()
    
    product_page.is_not_element_present(ProductPageLocators.SUCCESS_MESSAGE)
 
@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    product_page = ProductPage(browser, ProductPageLocators.URL)
    product_page.open()
    
    product_page.add_product_to_cart()
    
    product_page.is_disappeared(ProductPageLocators.SUCCESS_MESSAGE)

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    
    page.open()
    
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    product_page = ProductPage(browser, ProductPageLocators.URL)
    product_page.open() 
    
    product_page.go_to_login_page()
    
    login_page = LoginPage(browser, LoginPageLocators)
    login_page.should_be_login_page()

class TestUserAddToBasketFromProductPage:
    
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser, faker):
        
        login_page = LoginPage(browser, LoginPageLocators.URL)
        login_page.open()
        email = faker.email()
        password = faker.name()
        
        login_page.register_new_user(email, password)
        
        login_page.should_be_authorized_user()

    @pytest.mark.new
    def test_user_can_add_product_to_basket(self, browser):
        product_page = ProductPage(browser, ProductPageLocators.URL)
        product_page.open()
        
        product_page.add_product_to_cart()
        
        product_page.should_be_success_message()
        product_page.cart_total_should_be_equal_to_product_price()
    
    def test_user_cant_see_success_message(self, browser):
        product_page = ProductPage(browser, ProductPageLocators.URL)
        
        product_page.open()
        
        product_page.is_not_element_present(ProductPageLocators.SUCCESS_MESSAGE)

