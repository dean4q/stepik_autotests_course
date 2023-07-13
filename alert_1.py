from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math
link = 'http://suninjuly.github.io/alert_accept.html'
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    alert = browser.switch_to.alert
    alert.accept()
    field = browser.find_element(By.ID,'answer')
    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text
    y = calc(x)
    field.send_keys(y)
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:


    # успеваем скопировать код за 30 секунд
    time.sleep(1000)
    # закрываем браузер после всех манипуляций
    browser.quit()
print()