from selenium.webdriver.common.by import By

from page_objectes.base_page import BasePage


class DispatchListPage(BasePage):
    def get_order_list(self):
        pass
    def diapstch_order(self,ordernum):
        self.do_find(By.XPATH,f"//a[text()={ordernum}]//..//..//button//span[text()='调度']").click()
        from page_objectes.transport.diapstchsys.dispatch_page import DispatchPage
        return DispatchPage(self.driver)


