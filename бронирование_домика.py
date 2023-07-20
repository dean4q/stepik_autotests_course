from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"),"100"))
button = browser.find_element(By.CSS_SELECTOR, "button.btn")

button.click()
field = browser.find_element(By.ID, 'answer')
x_element = browser.find_element(By.ID, 'input_value')
x = x_element.text
y = calc(x)
field.send_keys(y)
button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.ID, "solve")))

button.click()
time.sleep(30)