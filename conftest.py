import time
import pytest
from selenium import webdriver
from selenium.webdriver import ChromeOptions

@pytest.fixture(scope='function', autouse=True)
def faker_seed():
    return int(time.time())


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help="Choose user interface language for websites. ")


@pytest.fixture(scope ='function')
def browser(request):
    language = request.config.getoption("language")
    print(f"Selected language: {language}")
    options = ChromeOptions()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    driver = webdriver.Chrome(options=options)
    yield driver
    time.sleep(3)
    driver.quit()
