from selenium.webdriver.common.by import By

class BasePageLocators():
    placeholder = (By.XPATH, '//input[@placeholder="Искать на Ozon"]')
    view_all = (By.XPATH, '(//span[contains(text(), "Посмотреть все")])[2]')
    beats = (By.XPATH, '//span[@class = "ys5"][contains(text(), "Beats")]')
    samsung = (By.XPATH, '//span[@class = "ys5"][contains(text(), "Samsung")]')
    xiaomi = (By.XPATH, '//span[@class = "ys5"][contains(text(), "Xiaomi")]')
    price = (By.XPATH, '(//input[@type="text"])[3]')

