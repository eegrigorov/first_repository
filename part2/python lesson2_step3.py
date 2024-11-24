from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

link = "https://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.CSS_SELECTOR, "[id='num1']")
    x = x_element.text
    y_element = browser.find_element(By.CSS_SELECTOR, "[id='num2']")
    y = y_element.text
    z = (int(x)+int(y))
    select = Select(browser.find_element(By.CSS_SELECTOR, "[id='dropdown']"))
    select.select_by_value(str(z))

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла