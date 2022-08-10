from selenium.webdriver.common.by import By

from page_objectes.base_page import BasePage


class DispatchListPage(BasePage):
    def get_order_list(self):
        pass
    def diapstch_order(self):
        self.do_find(By.XPATH,"//tbody[@class='ant-table-tbody']//tr[1]//button//span[text()='调度']").click()
        from page_objectes.dispatch_page import DispatchPage
        return DispatchPage(self.driver)


