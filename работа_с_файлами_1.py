from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    firstName = browser.find_element(By.XPATH, "//body/div/form/div/input")
    firstName.send_keys("dean4q")

    lastName = browser.find_element(By.XPATH, "//body/div/form/div/input[2]")
    lastName.send_keys("star")

    email = browser.find_element(By.XPATH, "//body/div/form/div/input[3]")
    email.send_keys("sliutghlrg@mail.ru")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    upload_file = browser.find_element(By.ID, "file")
    upload_file.send_keys(file_path)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    time.sleep(30)


    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()