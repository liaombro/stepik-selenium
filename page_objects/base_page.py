

class BasePage:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        url = self.url
        self.browser.get(url)
    