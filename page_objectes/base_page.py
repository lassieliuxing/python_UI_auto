"""父类"""
import time

import allure
from selenium import webdriver


class BasePage:
    __BASE_URL = "https:///tmsapp-test.newchiwan.com/"

    # 访问登录
    # option = Options()
    # option.debugger_address = "localhost:9222"
    # self.driver = webdriver.Chrome(options=option)
    def __init__(self, base_driver=None):
        if base_driver:
            self.driver = base_driver
        else:
            self.driver = webdriver.Chrome()
            self.driver.implicitly_wait(10)
            self.driver.maximize_window()
        if not self.driver.current_url.startswith("http"):
            self.driver.get(self.__BASE_URL)

    def do_find(self, by, locator=None):
        if locator:
            return self.driver.find_element(by, locator)
        else:
            return self.driver.find_element(*by)

    def do_finds(self, by, locator=None):
        if locator:
            return self.driver.find_elements(by, locator)
        else:
            return self.driver.find_elements(*by)

    def do_send_keys(self, value, by, locator=None):
        self.do_find(by, locator).send_keys(value)

    def do_quit(self):
        self.driver.quit()

    def get_screen(self):
        timestamp = int(time.time())
        image_path = f"./images/image_{timestamp}.PNG"
        self.driver.save_screenshot(image_path)
        allure.attach.file(image_path, name="picture",
                           attachment_type=allure.attachment_type.PNG)

    def wait_element_until_visible(self, locator: tuple):
        from selenium.webdriver.support.wait import WebDriverWait
        from selenium.webdriver.support import expected_conditions
        return WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator))
