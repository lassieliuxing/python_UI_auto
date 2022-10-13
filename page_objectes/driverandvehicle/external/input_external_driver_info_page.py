from selenium.webdriver.common.by import By

from page_objectes.base_page import BasePage
from utils.log_utils import logger


class InputExternalDriverInfoPage(BasePage):
    __INPUT_EXTERNAL_DRIVER_NAME=(By.XPATH,"//input[@data-testid='create-drivers-name']")
    __INPUT_EXTERNAL_DRIVER_PHONE=(By.XPATH,"//input[@data-testid='create-drivers-phone']")
    __BTN_EXTERNAL_DRIVER_CONFIRM=(By.XPATH,"//button[@data-testid='confirm-button']")
    def input_require_info(self):
        logger.info("进入外协运力司机输入信息页面")
        self.do_send_keys("司机姓名1",self.__INPUT_EXTERNAL_DRIVER_NAME)
        self.do_send_keys("13200000001",self.__INPUT_EXTERNAL_DRIVER_PHONE)
        self.do_find(self.__BTN_EXTERNAL_DRIVER_CONFIRM).click()
        from page_objectes.driverandvehicle.external.external_driver_list_page import ExternalDriverListPage
        return ExternalDriverListPage(self.driver)
    def input_all_info(self):
        pass
    def modify_info(self):
        pass