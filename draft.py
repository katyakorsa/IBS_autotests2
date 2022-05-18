



        # all_items = browser.find_element(By.XPATH, '(//span[contains(text(), "Посмотреть все")])[1]')
        # all_items.click()
        # # item1 = browser.find_element(By.XPATH, '//span[text()="Beats"]')
        # # item1.click()
        # #
        # # browser.find_element(By.XPATH, '(//span[contains(text(), "Посмотреть все")])[1]').click()
        # # browser.find_element(By.XPATH, '//span[text()="Samsung"]').click()
        # #
        # # browser.find_element(By.XPATH, '(//span[contains(text(), "Посмотреть все")])[1]').click()
        # # browser.find_element(By.XPATH, '(//span[text()="Xiaomi"])[2]').click()
        #
        price_element = browser.find_element(By.XPATH, '(//input[@type="text"])[3]')
        price_element.send_keys(Keys.BACKSPACE)
        price_element.send_keys(20000)
#  #4.  Ограничить цену – до 50 000
#
# # #5. Отметить чекбокс – Высокий рейтинг
#
#
# #6.  Из результатов поиска добавьте в корзину все нечетные товаров:
# #
# # def test_add_to_cart(browser):
# #     page = ProductPage(url="", browser)
# #     page.open()
# #     page.add_to_cart_button()
# #
# #     if add_to_cart_button()
