import unittest
import time
from selenium import webdriver


hyperlink = "http://automationpractice.com/index.php"


# class FindLink(unittest.TestCase):

#     def setUp(self):
#         self.driver = webdriver.Chrome("C:\chromedriver_win32\chromedriver")

#     def test_link(self):
#         self.driver.get(hyperlink)
#         product = self.driver.find_elements_by_partial_link_text(
#             'product')
#         # Test atleast we have one link with name  "Product"
#         self.assertIsNotNone(product)

#     def tearDown(self):
#         self.driver.quit()


# ===============================================================================


class Searching(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("C:\chromedriver_win32\chromedriver")

    def test_link(self):
        self.driver.get(hyperlink)
        bar = self.driver.find_element_by_id("search_query_top")
        # Test atleast we have one link with name that
        self.assertIsNotNone(bar)

        bar.send_keys("blouse")

        self.driver.implicitly_wait(2)

        sbmit = self.driver.find_element_by_name("submit_search")

        sbmit.click()

        result = self.driver.find_element_by_class_name("heading-counter")

        print(result.text)

    def tearDown(self):
        self.driver.quit()


# ===============================================================================

# class FindProduct(unittest.TestCase):

#     def setUp(self):
#         self.driver = webdriver.Chrome("C:\chromedriver_win32\chromedriver")

#     def test_link(self):
#         self.driver.get(hyperlink)
#         product = self.driver.find_element_by_xpath(
#             "//a[@data-id-product='2']")

#         product.click()

#         self.driver.implicitly_wait(3)

#         link = self.driver.find_element_by_xpath(
#             '//a[contains(@href,"http://automationpractice.com/index.php?controller=order")]')

#         link.click()

#             # self.driver.implicitly_wait(10)
#             # sec_link = self.driver.find_element_by_xpath(
#             #     '//a[contains(@href, "http://automationpractice.com/index.php?controller=order&step=1")]')

#             # sec_link.click()

#         self.driver.implicitly_wait(30)
#     def tearDown(self):
#         self.driver.quit()
# ==============================================================================
login_link = "http://automationpractice.com/index.php?controller=authentication&back=my-account"


# class TestLogin(unittest.TestCase):

#     def setUp(self):
#         self.driver = webdriver.Chrome("C:\chromedriver_win32\chromedriver")

#     def test_search_by_text(self):
#         self.driver.get(login_link)
#         email = self.driver.find_element_by_name("email")
#         email.clear()
#         email.send_keys("hamza@example.com")
#         email = self.driver.find_element_by_name("passwd")
#         email.clear()
#         email.send_keys("test123")
#         # sbmt_button = self.driver.find_element_by_xpath(
#         #     './/button[@class="btn btn-default login_form_button"]')
#         sbmt_button = self.driver.find_element_by_id("SubmitLogin")
#         sbmt_button.click()
#         time.sleep(2)
#         # self.asserttrue(
#         #     "hamza@example.com" in self.driver.find_element_by_xpath("//a[@title='view my customer account']")
#         #     )

#     def tearDown(self):
#         self.driver.quit()


if __name__ == '__main__':
    unittest.main()
