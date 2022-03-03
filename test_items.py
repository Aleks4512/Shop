from idlelib import browser
from selenium.webdriver.common.by import By
import time

class TestBasket:
    def test_checked_button_add_baskets(self, browser):
        browser.implicitly_wait(2)
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        browser.get(link)
        # place for command "time.sleep(30)"
        
        list_of_names_buttons = browser.find_elements(By.CSS_SELECTOR, ".btn-add-to-basket")
        assert len(list_of_names_buttons), "button 'Add to basket' not found on the page !"
