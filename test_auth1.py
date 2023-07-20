
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
import passw
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
link = 'https://stepik.org/lesson/236895/step/1'

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()
class TestAuthorization():
    def test_find_b1(self, browser, ):

        browser.get(link)
        browser.implicitly_wait(15)
        button = browser.find_element(By.ID, "ember33")
        button.click()

        login_field = browser.find_element(By.ID, "id_login_email")
        browser.implicitly_wait(15)
        self.l = passw.login
        login_field.send_keys(self.l)
        password = browser.find_element(By.ID, "id_login_password")
        browser.implicitly_wait(15)
        self.p = passw.password
        password.send_keys(self.p)

        button3 = browser.find_element(By.CLASS_NAME, "sign-form__btn")
        button3.click()
        browser.implicitly_wait(15)
    def test_2(self,browser):
        answer = browser.find_element(By.CLASS_NAME, "ember-text-area")
        otvet = str(math.log(int(time.time())))
        answer.send_keys(otvet)

        # button4 = browser.find_element(By.CLASS_NAME, "submit-submission")
        button5 = WebDriverWait(browser, 15).until(EC.element_to_be_clickable((By.CLASS_NAME, "submit-submission")))
        browser.implicitly_wait(15)
        button5.click()
        true_answer = WebDriverWait(browser, 15).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "smart-hints__hint"))).text
        print(true_answer)

        if true_answer != "Correct!":
            with open('result.txt', 'a') as file:
                file.write(true_answer)
        assert true_answer == "Correct!"
        if __name__ == "__main__":
            pytest.main()

        time.sleep(100)









    #html/body/div[4]/div/div/div/div[2]/div/div/div/div[2]/div/div/div[2]/div/div[3]