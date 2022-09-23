"""创建受理单页"""
import time

import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By

from page_objectes.base_page import BasePage
from utils.log_utils import logger

@allure.feature("创建受理单模块")
class CreateOrderPage(BasePage):
    __BTN_CUSTOMERID=(By.ID, "customerId")
    # __BTN_CUSTOMRNAME=(By.XPATH, "//*[text()='创建开单客户3']")
    __INPUT_CLIENTCODE=(By.ID, "clientCode")
    __INPUT_SHIPER_NAME=(By.ID, "shipperName")
    __INPUT_SHIPER_PHONE=(By.ID, "shipperPhone")
    __INPUT_SHIPER_UNIT=(By.ID, "shipperUnit")
    __INPUT_SHIPER_ADDRESS=(By.ID, "shipperAddress")
    __INPUT_DELIVER_NAME = (By.ID, "takeDeliveryName")
    __INPUT_DELIVER_PHONE = (By.ID, "takeDeliveryPhone")
    __INPUT_DELIVER_UNIT = (By.ID, "takeDeliveryUnit")
    __INPUT_DELIVER_ADRESS = (By.ID, "takeDeliveryAddress")
    __INPUT_CARGOES_NAME=(By.XPATH, "//input[@data-testid='cargoes-name-input']")
    __INPUT_CARGOES_WEIGHT=(By.XPATH, "//input[@data-testid='cargoes-weight-input']")
    __INPUT_CARGOES_VOLUME=(By.XPATH, "//input[@data-testid='cargoes-volume-input']")
    __INPUT_CARGOES_NUM=(By.XPATH, "//input[@data-testid='cargoes-num-input']")
    __INPUT_CARGOES_MONEY=(By.XPATH, "//input[@data-testid='cargoes-money-input']")
    __INPUT_CARGOES_TOTAL_WEIGHT=(By.XPATH,"//input[@data-testid='cargo-total-weight-input']")
    __INPUT_CARGOES_TOTAL_VOLUME=(By.XPATH,"//input[@data-testid='cargo-total-volume-input']")
    __INPUT_CARGOES_TOTAL_NUMBER=(By.XPATH,"//input[@data-testid='cargo-total-number-input']")
    __INPUT_FEE=(By.XPATH, "//input[@data-testid='form-fee-input']")
    __BTN_ORDER_SUBMIT=(By.XPATH, "//button[@data-testid='create-order-submit-button']")


    @allure.story("创建成功")
    def create_order(self,customer_name,customer_num,order_fee):
        logger.info("进入创建受理单页面")
        # 输入”所属信息“-客户企业名/客户单号
        self.do_find(self.__BTN_CUSTOMERID).click()

        self.do_find(By.XPATH, f"//*[text()='{customer_name}']").click()
        self.do_send_keys(customer_num,self.__INPUT_CLIENTCODE)
        # 输入”发货信息“-发货人/电话/单位/地址
        self.do_send_keys("发货人",self.__INPUT_SHIPER_NAME)
        self.do_send_keys("发货电话",self.__INPUT_SHIPER_PHONE)
        self.do_send_keys("发货单位2222222222222222222222222222222",self.__INPUT_SHIPER_UNIT)
        self.do_send_keys("发货地址11111111111111111111111111111111",self.__INPUT_SHIPER_ADDRESS)
        # 输入”收货信息“-收货人/电话/单位/地址
        self.do_send_keys("收货人",self.__INPUT_DELIVER_NAME)
        self.do_send_keys("收货电话",self.__INPUT_DELIVER_PHONE)
        self.do_send_keys("收货单位3333333333333333",self.__INPUT_DELIVER_UNIT)
        self.do_send_keys("收货地址44444444444444444",self.__INPUT_DELIVER_ADRESS)
        # 输入”货物信息“-货物类型/货物名称/货物重量/货物体积/货物件数/货物价值
        self.do_send_keys("货物名称",self.__INPUT_CARGOES_NAME)
        self.do_send_keys("103.33",self.__INPUT_CARGOES_TOTAL_WEIGHT)
        # self.do_send_keys(cargoes_weight,self.__INPUT_CARGOES_WEIGHT)
        # self.do_send_keys(cargoes_volume,self.__INPUT_CARGOES_VOLUME)
        # self.do_send_keys(cargoes_num,self.__INPUT_CARGOES_NUM)
        # self.do_send_keys(cargoes_money,self.__INPUT_CARGOES_MONEY)
        # 输入”费用信息“
        self.driver.execute_script(
            """document.querySelector("[data-testid='create-order-submit-button']").scrollIntoView()""")
        time.sleep(2)
        # ele = self.driver.execute_script(
        #     """document.querySelector("[data-testid='form-fee-input']").value=''"""
        # )
        # ele.send_keys(200)
        # self.driver.execute_script(
        #     """ document.querySelector("[data-testid='form-fee-input']").focus()
        #         document.execCommand('insertText', true, 200)"""
        # )


        # self.do_find(By.XPATH,"//input[@data-testid='form-fee-input']").clear()
        # self.do_send_keys(order_fee,self.__INPUT_FEE)
        input_ele=self.do_find(By.XPATH,"//input[@data-testid='form-fee-input']")
        action = ActionChains(self.driver)
        action.move_to_element(input_ele).double_click(input_ele).send_keys(200).perform()

        # input_ele.send_keys(keys.BACK_SPACE).perform()

        # self.driver.execute_script("arguments[0].value=200;",input_ele)
        # input_ele.send_keys(200)
        # 点击”确认开单“
        self.do_find(self.__BTN_ORDER_SUBMIT).click()
        # self.get_screen()
        # ==>受理单
        from page_objectes.transport.ordermanagesys.order_list_page import OrdersListPage
        return OrdersListPage(self.driver)