from selenium.webdriver.common.by import By

from page_objectes.base_page import BasePage


class FullTransportAllPage(BasePage):
    def get_waybill_status(self):
        self.do_find(By.XPATH,"//tr[@data-row-key='CW2022081177008404']//td[3]")
