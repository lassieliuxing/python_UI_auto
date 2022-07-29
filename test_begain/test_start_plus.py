import logging
import time

import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Test_start:
    def setup_class(self):
        self.driver=webdriver.Chrome()
        self.driver.implicitly_wait(3)

    def teardown_class(self):
        self.driver.quit()
    def get_screen(self):
        timestamp=int(time.time())
        #创建好image路径
        image_path=f"./images/image_{timestamp}.PNG"
        #截图
        self.driver.save_screenshot(image_path)
        #将截图放到报告中
        allure.attach.file(image_path,name="picture",attachment_type=allure.attachment_type.PNG)


    def test_create_order(self):
        self.driver.get("https://tpl-test.newchiwan.cn/")
        self.driver.find_element(by=By.ID, value="phone").send_keys("13900000000")
        self.driver.find_element(by=By.ID, value="password").send_keys("1111111l")
        time.sleep(2)
        self.driver.find_element(by=By.ID, value="code").send_keys("1111")
        ele=WebDriverWait(self.driver,5).until(
            expected_conditions.element_to_be_clickable(
                (By.XPATH,"//button[@data-testid='signin-sumbit-button']")))
        ele.click()
        self.driver.maximize_window()
        time.sleep(2)
        #
        # def click_exception(by,element,max_attempts=5):
        #     def _inner(driver):
        #         #多次点击按钮
        #         actul_attempts = 0 #实际点击次数
        #         while actul_attempts<max_attempts:
        #             actul_attempts += 1
        #             try:
        #                 #如果点击过程报错，执行except，并继续循环
        #                 #没有报错，直接return循环结束
        #                 driver.find_element(by, element).click()
        #                 return True
        #             except Exception:
        #                 print("在点击时报错")
        #                 # 当大于最大次数，结束循环，抛出异常
        #         raise Exception("超出最大点击次数")
        #     return  _inner()
        # # 数据清理，通过接口清理,清理脏数据
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
        self.driver.find_element(by=By.XPATH,value="//input[@data-testid='cargoes-weight-input']").send_keys("100")

        self.driver.execute_script("""document.querySelector("[data-testid='create-order-submit-button']").scrollIntoView()""")
        time.sleep(3)

        self.driver.find_element(by=By.XPATH, value="//input[@data-testid='form-fee-input']").send_keys("200")

        self.driver.find_element(by=By.XPATH,value="//button[@data-testid='create-order-submit-button']").click()
        self.get_screen()
        res=self.driver.find_elements(by=By.XPATH,value="//*[text()='创建开单客户3']")
        logging.info(f"断言获取到的实际结果为{res}")
        assert res !=[]


