from selenium.webdriver.common.by import By

class BasePageLocators():
    PLACEHOLDER = (By.XPATH, '//input[@placeholder="Искать на Ozon"]')
    VIEW_ALL = (By.XPATH, '(//span[contains(text(), "Посмотреть все")])[1]')
    BEATS = (By.XPATH, '//span[text()="Beats"]')
    SAMSUNG = (By.XPATH, '//span[text()="Samsung"]')
    XIAOMI = (By.XPATH, '(//span[text()="Xiaomi"])[2]')
    PRICE = (By.XPATH, '(//input[@type="text"])[3]')

