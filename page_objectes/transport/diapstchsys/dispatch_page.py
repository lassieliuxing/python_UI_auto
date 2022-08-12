from time import sleep

from selenium.webdriver.common.by import By

from page_objectes.base_page import BasePage


divText="//*[text()='{0}']"


class DispatchPage(BasePage):
    __INPUT_DRIVER_NAME=(By.XPATH,"//div[@data-testid='dispatch-waybill-drivers-select']//span[1]")
    __INPUT_DRIVER_PHONE=(By.XPATH,"//*[@data-testid='dispatch-waybill-drivers-phone-select']")
    __INPUT_VEHICLE=(By.XPATH,"//*[@id='rc_select_24']")
    __BTN_DATA=(By.XPATH,"//*[@id='planLoadingAt']")
    __INPUT_DATA_TIME_NOW=(By.XPATH,"//*[text()='此刻']")
    __BTN_ADVANCE=(By.XPATH,"//button[@data-testid='advance-checked']")
    __INPUT_ADVANCE_CASH=(By.XPATH,"//input[@data-testid='advance-oil-payment-input']")
    __INPUT_ADVANCE_OILD=(By.XPATH,"//input[@data-testid='advance-oil-amount-input']")
    __INPUT_DELIVER_CASH=(By.XPATH,"//input[@data-testid='reach-oil-payment-input']")
    __INPUT_DELIVER_OILD=(By.XPATH,"//input[@data-testid='reach-oil-amount-input']")
    __BTN_BANLANCE = (By.XPATH, "//button[@data-testid='final-checked']")
    __INPUT_BANLANCE_CASH = (By.XPATH, "//input[@data-testid='final-oil-payment-input']")
    __INPUT_BANLANCE_OILD = (By.XPATH, "//input[@data-testid='final-oil-amount-input']")
    __BTN_RECEIPT=(By.XPATH,"//button[@id='receipt']")
    __BTN_ADD=(By.XPATH,"//button[@data-testid='confirm-button']")
    __BTN_CANCEL=(By.XPATH,"//button[@data-testid='cancel-button']")


    def input_dispatch_with_deliver(self):
        # 只填写到付款

        self.do_find(self.__INPUT_DRIVER_NAME).click()
        # self.do_find(By.XPATH,"//*[text()='签收测试司机']").click()
        self.do_find(By.XPATH,divText.format("签收测试司机")).click()
        self.do_find(self.__BTN_DATA).click()
        self.do_find(self.__INPUT_DATA_TIME_NOW).click()
        self.do_send_keys("100",self.__INPUT_DELIVER_CASH)
        self.do_send_keys("200",self.__INPUT_DELIVER_OILD)
        self.do_find(self.__BTN_ADD).click()
        sleep(10)
        from page_objectes.transport.diapstchsys.dispatch_list_page import DispatchListPage
        return DispatchListPage(self.driver)

    def input_dispatch_with_advance_and_deliver(self):
        # 只填写到付款
        self.do_find(self.__INPUT_DRIVER_NAME).click()
        self.do_find(By.XPATH, "//*text()='签收测试司机").click()
        self.do_find(self.__BTN_DATA).click()
        self.do_find(self.__INPUT_DATA_TIME_NOW).click()
        self.do_find(self.__BTN_ADVANCE).click()
        self.do_send_keys("300",self.__INPUT_ADVANCE_CASH)
        self.do_send_keys("440",self.__INPUT_ADVANCE_OILD)
        self.do_send_keys("100", self.__INPUT_DELIVER_CASH)
        self.do_send_keys("200", self.__INPUT_DELIVER_OILD)
        self.do_find(self.__BTN_ADD).click()
        sleep(10)
    def input_dispatch_with_advance_and_deliver_and_banlance(self):
        # 只填写到付款
        self.do_find(self.__INPUT_DRIVER_NAME).click()
        self.do_find(By.XPATH, "//*text()='签收测试司机").click()
        self.do_find(self.__BTN_DATA).click()
        self.do_find(self.__INPUT_DATA_TIME_NOW).click()
        self.do_find(self.__BTN_ADVANCE).click()
        self.do_send_keys("300",self.__INPUT_ADVANCE_CASH)
        self.do_send_keys("440",self.__INPUT_ADVANCE_OILD)
        self.do_send_keys("100", self.__INPUT_DELIVER_CASH)
        self.do_send_keys("200", self.__INPUT_DELIVER_OILD)
        self.do_find(self.__BTN_BANLANCE).click()
        self.do_send_keys("500",self.__INPUT_BANLANCE_CASH)
        self.do_send_keys("600",self.__INPUT_BANLANCE_OILD)
        self.do_find(self.__BTN_ADD).click()
        sleep(10)
    def input_dispatch_with_deliver_and_banlance(self):
        # 只填写到付款
        self.do_find(self.__INPUT_DRIVER_NAME).click()
        self.do_find(By.XPATH, "//*text()='签收测试司机").click()
        self.do_find(self.__BTN_DATA).click()
        self.do_find(self.__INPUT_DATA_TIME_NOW).click()
        self.do_send_keys("100", self.__INPUT_DELIVER_CASH)
        self.do_send_keys("200", self.__INPUT_DELIVER_OILD)
        self.do_find(self.__BTN_BANLANCE).click()
        self.do_send_keys("500",self.__INPUT_BANLANCE_CASH)
        self.do_send_keys("600",self.__INPUT_BANLANCE_OILD)
        self.do_find(self.__BTN_ADD).click()
        sleep(10)
    def input_dispatch_with_advance_and_deliver_and_banlance_and_receipt(self):
        # 只填写到付款
        self.do_find(self.__INPUT_DRIVER_NAME).click()
        self.do_find(By.XPATH, "//*text()='签收测试司机").click()
        self.do_find(self.__BTN_DATA).click()
        self.do_find(self.__INPUT_DATA_TIME_NOW).click()
        self.do_find(self.__BTN_ADVANCE).click()
        self.do_send_keys("300",self.__INPUT_ADVANCE_CASH)
        self.do_send_keys("440",self.__INPUT_ADVANCE_OILD)
        self.do_send_keys("100", self.__INPUT_DELIVER_CASH)
        self.do_send_keys("200", self.__INPUT_DELIVER_OILD)
        self.do_find(self.__BTN_BANLANCE).click()
        self.do_send_keys("500",self.__INPUT_BANLANCE_CASH)
        self.do_send_keys("600",self.__INPUT_BANLANCE_OILD)
        self.do_find(self.__BTN_RECEIPT).click()
        self.do_find(self.__BTN_ADD).click()
        sleep(10)
