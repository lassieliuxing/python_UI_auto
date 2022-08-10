from time import sleep

from selenium.webdriver.common.by import By

from page_objectes.base_page import BasePage


class DispatchPage(BasePage):
    def input_dispatch(self):
        self.do_send_keys("100","//*[@data-testid='oil-payment-input']")
        sleep(10)