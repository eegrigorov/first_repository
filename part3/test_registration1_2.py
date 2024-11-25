import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestsRegistration(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def fill_form(self, link):
        browser = self.driver
        browser.implicitly_wait(5)
        browser.get(link)

        input1 = browser.find_element(By.CSS_SELECTOR, "input.form-control.first[required]")
        input1.send_keys("Elliot")
        input2 = browser.find_element(By.CSS_SELECTOR, "input.form-control.second[required]")
        input2.send_keys("Alderson")
        input3 = browser.find_element(By.CSS_SELECTOR, "input.form-control.third")
        input3.send_keys("gg@mail.ru")

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        return welcome_text

    def test_registration(self):
        link = 'http://suninjuly.github.io/registration1.html'
        registration_result = self.fill_form(link)

        self.assertEqual("Congratulations! You have successfully registered!", registration_result)

    def test_registration_bug(self):
        link = 'http://suninjuly.github.io/registration2.html'
        registration_result = self.fill_form(link)

        self.assertEqual("Congratulations! You have successfully registered!", registration_result)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()