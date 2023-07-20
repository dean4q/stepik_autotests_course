import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
import passw
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Firefox()
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestAuth():

    @pytest.mark.parametrize('link1', ['https://stepik.org/lesson/236895/step/1',
                                       'https://stepik.org/lesson/236896/step/1',
                                       'https://stepik.org/lesson/236897/step/1',
                                       'https://stepik.org/lesson/236898/step/1',
                                       'https://stepik.org/lesson/236899/step/1',
                                       'https://stepik.org/lesson/236903/step/1',
                                       'https://stepik.org/lesson/236904/step/1',
                                       'https://stepik.org/lesson/236905/step/1'])
    def test_find_b1(self, browser, link1):

        link = link1
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
        time.sleep(5)
        answer_field = browser.find_element(By.CLASS_NAME, "ember-text-area")
        otvet = str(math.log(int(time.time() + 0.018)))
        answer_field.send_keys(otvet)

        button5 = WebDriverWait(browser, 15).until(EC.element_to_be_clickable((By.CLASS_NAME, "submit-submission")))
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
