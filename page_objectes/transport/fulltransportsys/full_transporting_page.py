from selenium.webdriver.common.by import By

from page_objectes.base_page import BasePage


class FullTransportIngPage(BasePage):
    __BTN_OPERATE=()
    __BTN_CONFIRM_START=(By.XPATH,"//span[text()='确认发车']")
    __BTN_CONFIRMARRIVE=(By.XPATH,"//span[text()='确认到车']")
    __BTN_SIGN=()
    def confirm_start(self,waybillnum):
        self.do_find(By.XPATH,f"//tr[@data-row-key='{waybillnum}']//*[@data-testid='setting-icon']").click()
        self.do_find(By.XPATH,"//span[text()='确认发车']").click()
        return FullTransportIngPage(self.driver)

    def confirm_arrive(self,waybillnum):
        self.do_find(By.XPATH, f"//tr[@data-row-key='{waybillnum}']//*[@data-testid='setting-icon']").click()
        self.do_find(By.XPATH, "//span[text()='确认到车']").click()
        return FullTransportIngPage(self.driver)

    def confirm_sign(self,waybillnum):
        self.do_find(By.XPATH, f"//tr[@data-row-key='{waybillnum}']//*[@data-testid='setting-icon']").click()
        self.do_find(By.XPATH, "//span[text()='签收']").click()
        # return FullTransportIngPage(self.driver)

