from time import sleep

from selenium.webdriver.common.by import By

from page_objectes.base_page import BasePage


class DispatchPage(BasePage):
    __INPUT_DRIVER_NAME=(By.XPATH,"//*[@id='rc_select_12']")
    __INPUT_DRIVER_PHONE=(By.XPATH,"//*[@data-testid='dispatch-waybill-drivers-phone-select']")
    __INPUT_VEHICLE=(By.XPATH,"//*[@id='rc_select_13']")
    __INPUT_DATA=(By.XPATH,"//*[@id='planLoadingAt']")
    __BTN_ADVANCE=(By.XPATH,"//button[@advance-checked='advance-checked']")
    __INPUT_ADVANCE_CASH=(By.XPATH,"//input[@data-testid='oil-payment-input']")
    __INPUT_ADVANCE_OILD=(By.XPATH,"//input[@data-testid='oil-amount-input']")
    __INPUT_DELIVER=(By.XPATH,"")

    def input_dispatch(self):

        self.do_send_keys("100",By.XPATH,"//*[@data-testid='oil-payment-input']")
        sleep(10)