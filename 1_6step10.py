from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    blocks = browser.find_elements(By.XPATH, "//div[contains(@class, 'block')]")
    for i in range(len(blocks)):
        form_groups = browser.find_elements(By.CSS_SELECTOR,
                                            f"[action='registration_result.html'] > div:nth-child({i + 1}) > div")
        for j in range(len(form_groups)):
            if browser.find_element(By.CSS_SELECTOR,
                                    f"[action='registration_result.html'] > div:nth-child({i + 1}) > div:nth-child({j + 1}) > label").text[-1] == "*":
                browser.find_element(By.CSS_SELECTOR,
                                     f"[action='registration_result.html'] > div:nth-child({i + 1}) > div:nth-child({j + 1}) > input").send_keys("Ivan")

    time.sleep(5)

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
