from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "https://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    x_element = browser.find_element(By.CSS_SELECTOR, "[id='input_value']")
    x = x_element.text
    y = calc(x)

    input0 = browser.find_element(By.CSS_SELECTOR, "[id='answer']")
    input0.send_keys(y)
    input1 = browser.find_element(By.CSS_SELECTOR, "[id='robotCheckbox']")
    input1.click()
    input2 = browser.find_element(By.CSS_SELECTOR, "[id='robotsRule']")
    input2.click()
    input3 = browser.find_element(By.TAG_NAME, "button")
    input3.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла