

"""登录"""
from datetime import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from page_objectes.base_page import BasePage


class LoginPage(BasePage):

    def login(self):
        # 访问登录
        self.driver.get("https://tpl-test.newchiwan.cn/")
        # 输入”用户名“
        self.driver.find_element(by=By.ID, value="phone").send_keys("13900000000")
        # 输入”登陆密码“
        self.driver.find_element(by=By.ID, value="password").send_keys("1111111l")
        time.sleep(2)
        # 输入”验证码“
        self.driver.find_element(by=By.ID, value="code").send_keys("1111")
        # 点击”登录“
        ele = WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(
                (By.XPATH, "//button[@data-testid='signin-sumbit-button']")))
        ele.click()
        self.driver.maximize_window()
        time.sleep(2)
        # ==》首页
        from page_objectes.home_page import HomePage
        return HomePage(self.driver)