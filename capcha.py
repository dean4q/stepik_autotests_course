from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    field = browser.find_element(By.ID,'answer')
    x_element = browser.find_element(By.CSS_SELECTOR, 'div.container > form > div > label > #input_value')
    x = x_element.text
    y = calc(x)
    field.send_keys(y)
    i_am_robot = browser.find_element(By.ID, 'robotCheckbox')
    i_am_robot.click()
    robot_rule = browser.find_element(By.ID, 'robotsRule')
    robot_rule.click()
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    print(y)
finally:


    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
print()