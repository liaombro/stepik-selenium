from page_objects.product_page import ProductPage
from page_objects.locators import ProductPageLocators
import pytest

@pytest.mark.skip
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6", marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])

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

