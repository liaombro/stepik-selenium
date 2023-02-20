from selenium.webdriver.common.by import By
from page_objects.main_page import MainPage
link = "http://selenium1py.pythonanywhere.com/"

def test_guest_can_go_to_login_page(browser):
    main_page = MainPage(browser, link)
    main_page.open()
    main_page.go_to_login_page()
    
def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    main_page = MainPage(browser, link)
    main_page.open()
    main_page.should_be_login_link()
