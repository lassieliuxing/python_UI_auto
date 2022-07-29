import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class Test_start:
    def setup_class(self):
        self.driver=webdriver.Chrome()
        self.driver.implicitly_wait(3)

    # def teardown_class(self):
    #     self.driver.quit()

    def test_login(self):
        self.driver.get("https://tpl-test.newchiwan.cn/")
        self.driver.find_element(by=By.ID,value="phone").send_keys("13900000000")
        self.driver.find_element(by=By.ID,value="password").send_keys("1111111l")
        self.driver.find_element(by=By.ID,value="code").send_keys("1111")
        time.sleep(1)
        self.driver.find_element(by=By.XPATH,value="//button[@data-testid='signin-sumbit-button']").click()
        self.driver.maximize_window()
        time.sleep(2)
    # def test_create_driver_without_vehicle(self):
    #     self.driver.find_element(by=By.XPATH,value="//span[text()='运力管理']").click()
    #     self.driver.find_element(by=By.XPATH,value="//span[text()='外协运力']").click()
    #     self.driver.find_element(by=By.XPATH,value="//div[text()='司机管理']").click()
    #     self.driver.find_element(by=By.XPATH,value="//span[text()='添加司机']").click()
    #     self.driver.find_element(by=By.XPATH,value="//input[@data-testid='create-drivers-name']").send_keys("司机姓名十")
    #     self.driver.find_element(by=By.XPATH,value="//input[@data-testid='create-drivers-phone']").send_keys("13211111111")
    #     self.driver.find_element(by=By.XPATH,value="//button[@data-testid='confirm-button']").click()
    #     result=self.driver.find_elements(by=By.XPATH, value="//*[text()='司机姓名十']")
    #     assert  result!=[]
    # def test_modify_driver(self):
    #     self.driver.find_element(by=By.XPATH, value="//span[text()='运力管理']").click()
    #     self.driver.find_element(by=By.XPATH, value="//span[text()='外协运力']").click()
    #     self.driver.find_element(by=By.XPATH, value="//div[text()='司机管理']").click()
    #     self.driver.find_element(by=By.XPATH, value="//span[text()='添加司机']").click()
    #     self.driver.find_element(by=By.XPATH, value="//input[@data-testid='create-drivers-name']").send_keys("司机姓名2")
    #     self.driver.find_element(by=By.XPATH, value="//input[@data-testid='create-drivers-phone']").send_keys(
    #         "13211111112")
    #     self.driver.find_element(by=By.XPATH, value="//button[@data-testid='confirm-button']").click()
    #
    #     self.driver.find_element(by=By.XPATH, value="//*[text()='司机姓名2']/../..//*[text()='编辑']").click()
    #     time.sleep(2)
    #     self.driver.find_element(by=By.XPATH, value="//input[@data-testid='create-drivers-name']").send_keys("司机姓名3")
    #     self.driver.find_element(by=By.XPATH, value="//input[@data-testid='create-drivers-phone']").send_keys(
    #         "13211111113")
    #     self.driver.find_element(by=By.XPATH, value="//button[@data-testid='confirm-button']").click()
    #     result=self.driver.find_elements(by=By.XPATH, value="//[text()='司机姓名3']")
    #     assert result!=[]

    # def test_toggle_enable_driver(self):
    #     self.driver.find_element(by=By.XPATH, value="//span[text()='运力管理']").click()
    #     self.driver.find_element(by=By.XPATH, value="//span[text()='外协运力']").click()
    #     self.driver.find_element(by=By.XPATH, value="//div[text()='司机管理']").click()
    #     self.driver.find_element(by=By.XPATH, value="//span[text()='添加司机']").click()
    #     self.driver.find_element(by=By.XPATH, value="//input[@data-testid='create-drivers-name']").send_keys("司机姓名2")
    #     self.driver.find_element(by=By.XPATH, value="//input[@data-testid='create-drivers-phone']").send_keys(
    #         "13211111112")
    #     self.driver.find_element(by=By.XPATH, value="//button[@data-testid='confirm-button']").click()
    #
    #     self.driver.find_element(by=By.XPATH, value="//*[text()='司机姓名2']/../..//button[@data-testid='driver-enable-switch']").click()
    #
    #




    def test_create_order(self):
        # 数据清理，通过接口清理
        self.driver.find_element(by=By.XPATH,value="//*[text()='受理开单']").click()
        self.driver.find_element(by=By.XPATH,value="//*[text()='创建受理单']").click()
        self.driver.find_element(by=By.ID,value="customerId").click()
        self.driver.find_element(by=By.XPATH,value="//*[text()='创建开单客户3']").click()
        self.driver.find_element(by=By.ID,value="clientCode").send_keys("202207220001")
        self.driver.find_element(by=By.ID,value="shipperName").send_keys("发货人")
        self.driver.find_element(by=By.ID,value="shipperPhone").send_keys("发货电话")
        self.driver.find_element(by=By.ID,value="shipperUnit").send_keys("发货单位")
        self.driver.find_element(by=By.ID,value="shipperAdress").send_keys("发货地址")
        self.driver.find_element(by=By.ID,value="takeDeliveryName").send_keys("收货人")
        self.driver.find_element(by=By.ID,value="takeDeliveryPhone").send_keys("收货电话")
        self.driver.find_element(by=By.ID,value="takeDeliveryUnit").send_keys("收货单位")
        self.driver.find_element(by=By.ID,value="takeDeliveryAdress").send_keys("收货地址")
        self.driver.find_element(by=By.XPATH,value="//input[@data-testid='cargoes-name-input']").send_keys("货物名称")
        # self.driver.find_element(by=By.ID,value="orderCrgoes_0_orderCargoesType").send_keys("orderCrgoes_0_orderCargoesType_list_0")

        self.driver.find_element(by=By.XPATH,value="//input[@data-testid='cargoes-weight-input']").send_keys("100")

        self.driver.execute_script("window.scrollTo(0,10000)")
        self.driver.find_element(by=By.XPATH,value="//div[text()='应收费用']/../../../div[2]/div/div/span").send_keys("200")
        self.driver.find_element(by=By.ID,value="create-order-submit-button").click()


