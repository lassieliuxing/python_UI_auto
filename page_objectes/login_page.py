

"""登录"""
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from page_objectes.base_page import BasePage
from utils.log_utils import logger


class LoginPage(BasePage):
    __INPUT_PHONE=(By.ID, "phone")
    __INPUT_PASSWORD=(By.ID, "password")
    __INPUT_CODE=(By.ID, "code")
    __BTN_LOGIN=(By.XPATH, "//button[@data-testid='signin-sumbit-button']")

    def login(self):
        logger.info("进入登陆页面")
        # 访问登录
        self.driver.get("https://tpl-test.newchiwan.cn/")
        # 输入”用户名“
        self.do_send_keys("13900000000",self.__INPUT_PHONE)
        # 输入”登陆密码“
        self.do_send_keys("1111111l",self.__INPUT_PASSWORD)
        time.sleep(2)
        # 输入”验证码“
        self.do_send_keys("1111",self.__INPUT_CODE)
        # 点击”登录“
        ele = WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(
                self.__BTN_LOGIN))
        ele.click()
        self.driver.maximize_window()
        time.sleep(2)
        # ==》首页
        from page_objectes.home_page import HomePage
        return HomePage(self.driver)