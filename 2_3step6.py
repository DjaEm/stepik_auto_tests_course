from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from math import log, sin


def formula(x):
    return log(abs(12 * sin(int(x))))


try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.TAG_NAME, "button").click()

    time.sleep(1)

    browser.switch_to.window(browser.window_handles[1])

    x = browser.find_element(By.ID, "input_value").text
    browser.find_element(By.ID, "answer").send_keys(str(formula(x)))

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()