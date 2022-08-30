from selenium.webdriver.common.by import By

from page_objectes.base_page import BasePage


class PriceRevisionPage(BasePage):
    __INPUT_AMOUNT=(By.XPATH,"//input[@data-testid='form-amount-input']")
    __INPUT_TEXT=(By.XPATH,"//textarea[@data-testid='form-desc-textarea']")
    __BTN_CONFIRM=(By.XPATH,"//button[@data-testid='confirm-button']")
    __BTN_AMOUNT_DECREASE=(By.XPATH,"//*[text()='减']")
    __BTN_AMOUNT_ADD=(By.XPATH,"//*[text()='加']")
    def price_revision_decrease(self):
        # self.do_find(self.__BTN_AMOUNT_DECREASE).click()
        self.do_send_keys("10",self.__INPUT_AMOUNT)
        self.do_send_keys("应收明细调整原因-减少",self.__INPUT_TEXT)
        self.do_find(self.__BTN_CONFIRM).click()
        # 填写价格调整增加
        # 填写价格调整减少
        # 点击确认
        # 跳转应收明细页

    def price_revision_add(self):
        self.do_find(self.__BTN_AMOUNT_ADD).click()
        self.do_send_keys("100",self.__INPUT_AMOUNT)
        self.do_send_keys("应收明细调整原因-增加",self.__INPUT_TEXT)
        self.do_find(self.__BTN_CONFIRM).click()
        # 填写价格调整增加
        # 填写价格调整减少
        # 点击确认
        # 跳转应收明细页


