from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver


browser = webdriver.Chrome("C:\chromedriver_win32\chromedriver")
hyperlink = "http://automationpractice.com/index.php"


class AutomationSearchPage:

    SEARCH_INPUT = (By.ID, 'search_query_top')

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(hyperlink)

    def search(self, phrase):
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        search_input.send_keys(phrase + Keys.RETURN)


class AutoLogin:

    login_link = "http://automationpractice.com/index.php?controller=authentication&back=my-account"

    def __init__(self, function):
        self.function = function
        self.driver = browser

    def login(self):
        self.driver.get(AutoLogin.login_link)
        email = self.driver.find_element_by_name("email")
        email.clear()
        email.send_keys("hamza@example.com")
        email = self.driver.find_element_by_name("passwd")
        email.clear()
        email.send_keys("test123")
        sbmt_button = self.driver.find_element_by_id("SubmitLogin")
        sbmt_button.click()

    def __call__(self):

        self.login()
        self.function()


phrase = "blouse"

# search_page = AutomationSearchPage(browser)

# search_page.load()
# search_page.search(phrase)


@AutoLogin
def something():
    pass


something()
