from time import sleep

from selenium.webdriver.common.by import By

from page_objectes.base_page import BasePage


class DispatchPage(BasePage):
    __INPUT_DRIVER_NAME
    __INPUT_DRIVER_PHONE
    __INPUT_VEHICLE
    __INPUT_DATA
    __BTN_ADVANCE
    __INPUT_ADVANCE
    __INPUT_DELIVER

    def input_dispatch(self):

        self.do_send_keys("100",By.XPATH,"//*[@data-testid='oil-payment-input']")
        sleep(10)