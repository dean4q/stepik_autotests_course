from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

link = 'http://suninjuly.github.io/selects2.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    n = browser.find_element(By.ID, 'num1')
    num1 = n.get_attribute('span')
    b = int(n.text)

    m = browser.find_element(By.ID, 'num2')
    num2 = n.get_attribute('span')
    a = int(m.text)
    print(a, b)
    rez = a + b

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(rez))

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:


    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
print()