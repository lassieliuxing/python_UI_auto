from selenium.webdriver.common.by import By

from page_objectes.base_page import BasePage
from utils.log_utils import logger


class CustomerListPage(BasePage):
    __BTN_CREATE_CUATOMER=(By.XPATH,"//span[text()='添 加']")
    def create_customer(self):
        logger.info("进入客户管理添加页面")
        self.do_find(self.__BTN_CREATE_CUATOMER).click()
        from page_objectes.customersys.input_customer_info_page import InputCustomerInfoPage
        return InputCustomerInfoPage(self.driver)
    def search_customer(self):
        pass