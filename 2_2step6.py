from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select
from math import log, sin


def formula(x):
    return log(abs(12*sin(x)))


try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x = int(browser.find_element(By.ID, "input_value").text)
    y = formula(x)

    form = browser.find_element(By.CLASS_NAME, "form-control")
    form.send_keys(str(y))

    cb = browser.find_element(By.ID, "robotCheckbox")
    browser.execute_script("return arguments[0].scrollIntoView(true);", cb)
    cb.click()

    rb = browser.find_element(By.ID, "robotsRule")
    rb.click()

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()