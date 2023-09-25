import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class Test_start:
    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)

    def teardown_class(self):
        self.driver.quit()

    def test_login(self):
        self.driver.get("https://tpl-test.newchiwan.cn/")
        self.driver.find_element(by=By.ID, value="phone").send_keys("13900000000")
        self.driver.find_element(by=By.ID, value="password").send_keys("1111111l")
        self.driver.find_element(by=By.ID, value="code").send_keys("1111")
        time.sleep(1)
        self.driver.find_element(by=By.XPATH, value="//button[@data-testid='signin-sumbit-button']").click()
        self.driver.maximize_window()
        time.sleep(2)

    def test_create_driver_without_vehicle(self):
        self.driver.find_element(by=By.XPATH, value="//span[text()='运力管理']").click()
        self.driver.find_element(by=By.XPATH, value="//span[text()='外协运力']").click()
        self.driver.find_element(by=By.XPATH, value="//div[text()='司机管理']").click()
        self.driver.find_element(by=By.XPATH, value="//span[text()='添加司机']").click()
        self.driver.find_element(by=By.XPATH, value="//input[@data-testid='create-drivers-name']").send_keys(
            "司机姓名十")
        self.driver.find_element(by=By.XPATH, value="//input[@data-testid='create-drivers-phone']").send_keys(
            "13211111111")
        self.driver.find_element(by=By.XPATH, value="//button[@data-testid='confirm-button']").click()
        result = self.driver.find_elements(by=By.XPATH, value="//*[text()='司机姓名十']")
        assert result != []

    def test_modify_driver(self):
        self.driver.find_element(by=By.XPATH, value="//span[text()='运力管理']").click()
        self.driver.find_element(by=By.XPATH, value="//span[text()='外协运力']").click()
        self.driver.find_element(by=By.XPATH, value="//div[text()='司机管理']").click()
        self.driver.find_element(by=By.XPATH, value="//span[text()='添加司机']").click()
        self.driver.find_element(by=By.XPATH, value="//input[@data-testid='create-drivers-name']").send_keys(
            "司机姓名2")
        self.driver.find_element(by=By.XPATH, value="//input[@data-testid='create-drivers-phone']").send_keys(
            "13211111112")
        self.driver.find_element(by=By.XPATH, value="//button[@data-testid='confirm-button']").click()

        self.driver.find_element(by=By.XPATH, value="//*[text()='司机姓名2']/../..//*[text()='编辑']").click()
        time.sleep(2)
        self.driver.find_element(by=By.XPATH, value="//input[@data-testid='create-drivers-name']").send_keys(
            "司机姓名3")
        self.driver.find_element(by=By.XPATH, value="//input[@data-testid='create-drivers-phone']").send_keys(
            "13211111113")
        self.driver.find_element(by=By.XPATH, value="//button[@data-testid='confirm-button']").click()
        result = self.driver.find_elements(by=By.XPATH, value="//[text()='司机姓名3']")
        assert result != []

    def test_toggle_enable_driver(self):
        self.driver.find_element(by=By.XPATH, value="//span[text()='运力管理']").click()
        self.driver.find_element(by=By.XPATH, value="//span[text()='外协运力']").click()
        self.driver.find_element(by=By.XPATH, value="//div[text()='司机管理']").click()
        self.driver.find_element(by=By.XPATH, value="//span[text()='添加司机']").click()
        self.driver.find_element(by=By.XPATH, value="//input[@data-testid='create-drivers-name']").send_keys(
            "司机姓名2")
        self.driver.find_element(by=By.XPATH, value="//input[@data-testid='create-drivers-phone']").send_keys(
            "13211111112")
        self.driver.find_element(by=By.XPATH, value="//button[@data-testid='confirm-button']").click()

        self.driver.find_element(by=By.XPATH,
                                 value="//*[text()='司机姓名2']/../..//button[@data-testid='driver-enable-switch']").click()
