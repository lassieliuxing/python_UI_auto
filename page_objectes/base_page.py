"""父类"""
from selenium import webdriver


class BasePage:
    _BASE_URL ="https://tpl-test.newchiwan.cn/"
    def __init__(self,base_driver=None):
        if base_driver:
            self.driver=base_driver
        else:
            self.driver=webdriver.Chrome()
            self.driver.implicitly_wait(3)
            self.driver.maximize_window()
        if not self.driver.current_url.startswith("http"):
            self.driver.get(self._BASE_URL)
    def do_find(self,by,locator=None):
        if locator:
            return self.driver.find_element(by=by,value=locator)
        else:
            return self.driver.find_element(*by)
    def do_finds(self,by,locator=None):
        if locator:
            return self.driver.find_elements(by=by,value=locator)
        else:
            return self.driver.find_elements(*by)
    def do_send_keys(self,value,by,locator=None):
        ele=self.do_find(by=by,value=locator)
        ele.clear()
        ele.send_keys(value)
    def do_quit(self):
        self.driver.quit()



