from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    field = browser.find_element(By.ID,'answer')
    x_element = browser.find_element(By.CSS_SELECTOR, 'div.container > form > div > label > #input_value')
    x = x_element.text
    y = calc(x)
    field.send_keys(y)
    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    i_am_robot = browser.find_element(By.ID, 'robotCheckbox')
    i_am_robot.click()
    robot_rule = browser.find_element(By.ID, 'robotsRule')
    robot_rule.click()


    button.click()

    print(y)
finally:


    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
print()