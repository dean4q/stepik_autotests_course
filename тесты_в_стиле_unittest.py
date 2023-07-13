import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class TestUnit(unittest.TestCase):

    def test_registration1(self):

            link = "http://suninjuly.github.io/registration1.html"
            browser = webdriver.Chrome()
            browser.get(link)

            firstName = browser.find_element(By.CSS_SELECTOR,
                                             "div.first_block > div.form-group.first_class > input.form-control.first")
            firstName.send_keys("Kseniia")

            lastName = browser.find_element(By.CSS_SELECTOR,
                                            "div.first_block > div.form-group.second_class > input.form-control.second")
            lastName.send_keys("Piak")

            email = browser.find_element(By.CSS_SELECTOR,
                                         "div.first_block > div.form-group.third_class > input.form-control.third")
            email.send_keys("kseniia.piak@mail.ru")

            button = browser.find_element(By.CSS_SELECTOR, "button.btn")
            button.click()

            time.sleep(1)

            welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
            welcome_text = welcome_text_elt.text

            self.assertEquals("Congratulations! You have successfully registered!", welcome_text, 'ошибка в регистрации')



    def test_registration2(self):

            link = "http://suninjuly.github.io/registration2.html"
            browser = webdriver.Chrome()
            browser.get(link)

            firstName = browser.find_element(By.CSS_SELECTOR,
                                             "div.first_block > div.form-group.first_class > input.form-control.first")
            firstName.send_keys("Kseniia")

            lastName = browser.find_element(By.CSS_SELECTOR,
                                            "div.first_block > div.form-group.second_class > input.form-control.second")
            lastName.send_keys("Piak")

            email = browser.find_element(By.CSS_SELECTOR,
                                         "div.first_block > div.form-group.third_class > input.form-control.third")
            email.send_keys("kseniia.piak@mail.ru")

            button = browser.find_element(By.CSS_SELECTOR, "button.btn")
            button.click()

            time.sleep(1)

            welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
            welcome_text = welcome_text_elt.text

            self.assertEquals("Congratulations! You have successfully registered!" ,welcome_text, 'ошибка в регистрации')



if __name__ == "__main__":
    unittest.main()