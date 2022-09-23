import logging
from time import sleep

from selenium.webdriver.common.by import By

from page_objectes.base_page import BasePage
from utils.log_utils import logger


class CarrierManagePage(BasePage):
    __INPUT_CARRIER_NAME=(By.XPATH,"//input[@data-testid='carrier-search-name-input']")
    __INPUT_CARRIER_PERSON=(By.XPATH,"//input[@data-testid='carrier-search-contactname-input']")
    __INPUT_CARRIER_PHONE=(By.XPATH,"//input[@data-testid='carrier-search-contactphone-input']")
    __BTN_CARIER_ADD=(By.XPATH,"//span[text()='添 加']")
    __BTN_CARIER_QUERY=(By.XPATH,"//span[text()='查询']")
    __BTN_CARIER_CLEAR=(By.XPATH,"//span[text()='重置']")


    def create_carrier(self):
        logger.info("点击进入承运商添加页")
        # self.do_find(By.XPATH,"//span[text()='添 加']").click()
        self.do_find(self.__BTN_CARIER_ADD).click()
        sleep(2)
        from page_objectes.carriersys.input_carrier_info_page import InputCarrierInfoPage
        return InputCarrierInfoPage(self.driver)


    def search_carrier(self):
        self.do_send_keys("承运商1",self.__INPUT_CARRIER_NAME)
        self.do_send_keys("",self.__INPUT_CARRIER_PERSON)
        self.do_send_keys("",self.__INPUT_CARRIER_PHONE)
        self.do_find(self.__BTN_CARIER_QUERY).click()


    def update_carrier(self):
        pass

    def toggle_carrier(self):
        pass