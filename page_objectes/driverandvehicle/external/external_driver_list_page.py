from selenium.webdriver.common.by import By

from page_objectes.base_page import BasePage
from utils.log_utils import logger


class ExternalDriverListPage(BasePage):
    __BTN_ENTERNAL_CREATE_DRIVER = (By.XPATH, "//span[text()='添 加']")
    __BTN_ENTERNAL_SEARCH_DRIVER = (By.XPATH, "//button[@data-testid='submit']")
    __BTN_ENTERNAL_RESET_DRIVER = (By.XPATH, "//span[text()='重置']")
    __INPUT_ENTERNAL_DRIVER_NAME = (By.XPATH, "//input[@data-testid='drivers-name-input']")
    __INPUT_ENTERNAL_DRIVER_PHONE = (By.XPATH, "//input[@data-testid='drivers-phone-input']")
    __BTN_ENTERNAL_DRIVERE_SWITCH = (By.XPATH, "//button[@data-testid='driver-enable-switch']")

    def create_driver(self):
        logger.info("进入外协运力司机管理页面")
        self.do_find(self.__BTN_ENTERNAL_CREATE_DRIVER).click()
        from page_objectes.driverandvehicle.external.input_external_driver_info_page import InputExternalDriverInfoPage
        return InputExternalDriverInfoPage(self.driver)

    def search_driver(self):
        logger.info("查询外协司机")
        self.do_send_keys("司机名称", self.__INPUT_ENTERNAL_DRIVER_NAME)
        self.do_send_keys("司机手机", self.__INPUT_ENTERNAL_DRIVER_PHONE)

    def modify_driver(self):
        from page_objectes.driverandvehicle.external.input_external_driver_info_page import InputExternalDriverInfoPage
        return InputExternalDriverInfoPage(self.driver)

    def switch_driver(self):
        logger.info("禁用启用司机")
        pass
