from selenium.webdriver.common.by import By

from page_objectes.base_page import BasePage


class InputCarrierInfoPage(BasePage):
    __INPUT_CARRIER_INFO_NAME = (By.XPATH, "//input[@id='carrierName']")
    __INPUT_CARRIER_INFO_CODE = (By.XPATH, "//input[@id='creditCode']")
    __INPUT_CARRIER_INFO_ADDRESS = (By.XPATH, "//input[@id='companyAddress']")
    __BTN_CARRIER_INFO_CONFIRM = (By.XPATH, "//button[@data-testid='confirm-button']")
    def create_require_input(self):
        self.do_send_keys("承运商2", self.__INPUT_CARRIER_INFO_NAME)
        self.do_send_keys("统一社会信用代码1", self.__INPUT_CARRIER_INFO_CODE)
        self.do_send_keys("公司地址1", self.__INPUT_CARRIER_INFO_ADDRESS)
        self.do_find(self.__BTN_CARRIER_INFO_CONFIRM).click()
        from page_objectes.carriersys.carrier_list_page import CarrierManagePage
        return CarrierManagePage(self.driver)
    def create_all_input(self):
        pass


