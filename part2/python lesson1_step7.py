from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "https://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))


    input0 = browser.find_element(By.CSS_SELECTOR, "[id='treasure']")
    x = input0.get_attribute("valuex")
    y = calc(x)

    input1 = browser.find_element(By.CSS_SELECTOR, "[id='answer']")
    input1.send_keys(y)
    input2 = browser.find_element(By.CSS_SELECTOR, "[id='robotCheckbox']")
    input2.click()
    input3 = browser.find_element(By.CSS_SELECTOR, "[id='robotsRule']")
    input3.click()
    input4 = browser.find_element(By.TAG_NAME, "button")
    input4.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла