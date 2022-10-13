from selenium.webdriver.common.by import By

from page_objectes.base_page import BasePage


class InputCustomerInfoPage(BasePage):
    __INPUT_CUATOMER_NAME=(By.XPATH,"//input[@data-testid='name-input']")
    __BTN_CUSTOMER_CONFIRM=(By.XPATH,"//button[@data-testid='confirm-button']")
    def input_require_info(self):
        self.do_send_keys("客户企业名",self.__INPUT_CUATOMER_NAME)
        self.do_find(self.__BTN_CUSTOMER_CONFIRM).click()
        from page_objectes.customersys.customer_list_page import CustomerListPage
        return CustomerListPage(self.driver)

    def input_all_info(self):
        pass
    