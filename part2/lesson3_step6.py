from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.TAG_NAME, "button")
    input1.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    x_element = browser.find_element(By.CSS_SELECTOR, "[id='input_value']")
    x = x_element.text
    y = calc(x)

    input2 = browser.find_element(By.CSS_SELECTOR, "[id='answer']")
    input2.send_keys(y)

    input3 = browser.find_element(By.TAG_NAME, "button")
    input3.click()

finally:
    time.sleep(30)
    browser.quit()

