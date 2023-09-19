from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from math import log, sin
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def formula(x):
    return log(abs(12 * sin(int(x))))


try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    x = browser.find_element(By.ID, "input_value").text
    browser.find_element(By.ID, "answer").send_keys(str(formula(x)))

    browser.find_element(By.ID, "solve").click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()