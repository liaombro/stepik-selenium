from page_objects.product_page import ProductPage
from page_objects.locators import ProductPageLocators

def test_guest_can_add_product_to_basket(browser):
    product_page = ProductPage(browser, ProductPageLocators.URL)
    product_page.open()
    product_page.add_product_to_cart()
    product_page.should_be_success_message()
    product_page.cart_total_should_be_equal_to_product_price()