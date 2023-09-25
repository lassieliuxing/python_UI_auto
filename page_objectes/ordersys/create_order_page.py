"""创建受理单页"""
import time
from nis import match

import allure
import switch
from selenium.webdriver import ActionChains
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By

from page_objectes.base_page import BasePage
from utils.data_utils import data_time
from utils.log_utils import logger


@allure.feature("创建受理单模块")
class CreateOrderPage(BasePage):
    # 货源信息
    __BTN_CUSTOMER_ID = (By.CSS_SELECTOR, "input[id='customerId']")
    __BTN_PROJECT_INFO = (By.CSS_SELECTOR, "div[data-testid='project-info-select']")
    __BTN_CLIENT_CODE = (By.CSS_SELECTOR, "input[id='clientCode']")
    __BTN_CLERK = (By.CSS_SELECTOR, "input[id='clerkId']")
    # 线路信息
    __BTN_COMMON_LINE = (By.CSS_SELECTOR, "span[class$='i-icon-assembly-line']")
    __CHECK_LINE_ITEM = (By.CSS_SELECTOR, "input[class='ant-radio-input']")
    __BTN_LINE_ITEM_CONFIRM = (By.CSS_SELECTOR, "div[class='ant-modal-footer'] button[class$='ant-btn-primary']")
    # 收发货信息
    __INPUT_SHIPPER_INFORM = (By.XPATH, "//div[@class='sc-fhVjgA gHdpBo'][.//div[contains(@style, '104,')]]")
    __INPUT_RECEIVER_INFORM = (By.XPATH, "//div[@class='sc-fhVjgA gHdpBo'][.//div[contains(@style, '219,')]]")
    __INPUT_NAME = (By.CSS_SELECTOR, "input[id='name']")
    __INPUT_PHONE = (By.CSS_SELECTOR, "input[id='phone']")
    __INPUT_COMPANY = (By.CSS_SELECTOR, "input[id='company']")
    __INPUT_ADDRESS = (By.CSS_SELECTOR, "input[id$='9']")
    __INPUT_SHIPPER = (By.CSS_SELECTOR, "input[placeholder='查找发货人']")
    __INPUT_RECEIVER = (By.CSS_SELECTOR, "input[placeholder='查找收货人']")
    __BTN_SEARCH_RECEIVER = (By.CSS_SELECTOR, "button[class$='ant-input-search-button']")
    __CHECK_INFORM_ITEM = (By.CSS_SELECTOR, "span[class$='ant-radio-checked'] input[class='ant-radio-input']")
    __BTN_INFORM_CONFIRM = (By.CSS_SELECTOR, "button[class='ant-btn ant-btn-primary sc-bRJSeJ eWGFCF']")
    # 货物信息
    __BTN_CARGOES=(By.CSS_SELECTOR,"span[class$='i-icon-notebook']")
    __CHECK_CARGOES_ITEM=(By.CSS_SELECTOR,"span[class$='ant-radio-checked']")
    __BTN_CARGOES_ITEM_CONFIRM=(By.CSS_SELECTOR,"div[class='ant-modal-footer'] button[class$='ant-btn-primary']")
    __INPUT_CARGOES_TYPE = (By.CSS_SELECTOR, "input[id$='cargoTypeCode']")
    __INPUT_CARGOES_NAME = (By.XPATH, "//input[@data-testid='new-cargo-name-input']")

    __INPUT_CARGOES_WEIGHT = (By.XPATH, "//input[@data-testid='new-order-total-weight-input']")
    __INPUT_CARGOES_KG = (By.XPATH, "//*[@id='cargo_0_totalWeight']/../span/div/div[2]")
    __INPUT_CARGOES_VOLUME = (By.XPATH, "//input[@data-testid='order-total-volume-input']")
    __INPUT_CARGOES_NUM = (By.XPATH, "//input[@data-testid='new-order-total-cargoes-num-input']")
    __INPUT_CARGOES_MONEY = (By.XPATH, "//input[@data-testid='cargoes-money-input']")

    # 结算规则
    __BTN_CACULATE_NUM=(By.CSS_SELECTOR,"input[data-testid='valuation-quantity-input']")
    __BTN_CACULATE_UNIT_TON=(By.CSS_SELECTOR,"input[data-testid='valuation-quantity-input']~span div div")
    __BTN_CACULATE_UNIT_VOLUM=(By.CSS_SELECTOR,"input[data-testid='valuation-quantity-input']~span div div:nth-child(2)")
    __BTN_CACULATE_UNIT_NUM=(By.CSS_SELECTOR,"input[data-testid='valuation-quantity-input']~span div div:nth-child(3)")
    __BTN_CACULATE_RULE=(By.CSS_SELECTOR,"span[class='ant-select-selection-item']")

    __BTN_SWITCH_UP=(By.CSS_SELECTOR,"button[id$='ceiling'] span[class='ant-switch-inner']")
    __INPUT_SWITCH_UP=(By.CSS_SELECTOR,"input[data-testid='valuation-rule-input']")
    __BTN_SWITCH_DOWN=(By.CSS_SELECTOR,"button[id='rule_floor'] div[class='ant-switch-handle']")
    __INPUT_SWITCH_DOWN=(By.CSS_SELECTOR,"input[id$='floorParam']")
    __BTN_ORDER_SUBMIT = (By.XPATH, "//button[@data-testid='create-order-submit-button']")

    @allure.story("创建成功")
    def create_order(self, customer_name, project_name):
        logger.info("进入创建受理单页面")
        self.driver.implicitly_wait(5)
        # 输入”所属信息“-客户企业名/客户单号
        self.do_find(self.__BTN_CUSTOMER_ID).click()

        self.do_find(By.XPATH, f"//*[text()='{customer_name}']").click()
        self.do_find(self.__BTN_PROJECT_INFO).click()
        # self.do_find(self.__BTN_INPUT_PROJECT_INFO).click()
        self.do_send_keys(f"23{data_time()}", self.__BTN_CLIENT_CODE)
        # 货物信息
        self.do_find(self.__BTN_COMMON_LINE).click()
        time.sleep(2)
        # self.do_find(By.XPATH, "//*[text()='常用线路0105']").click()
        self.do_find(By.XPATH, "//*[text()='常用线路单货物0116']").click()
        # 输入”发货信息“-发货人/电话/单位/地址
        self.do_send_keys(f"发货人{data_time()}", self.__INPUT_SHIPER_NAME)
        self.do_send_keys("13548798850", self.__INPUT_SHIPER_PHONE)
        self.do_send_keys(f"发货单位{data_time()}", self.__INPUT_SHIPER_UNIT)
        self.do_send_keys(f"发货地址{data_time()}", self.__INPUT_SHIPER_ADDRESS)
        # 输入”收货信息“-收货人/电话/单位/地址
        self.do_send_keys(f"收货人{data_time()}", self.__INPUT_DELIVER_NAME)
        self.do_send_keys("16488885798", self.__INPUT_DELIVER_PHONE)
        self.do_send_keys(f"收货单位{data_time()}", self.__INPUT_DELIVER_UNIT)
        self.do_send_keys(f"收货地址{data_time()}", self.__INPUT_DELIVER_ADRESS)
        # 输入”货物信息“-货物类型/货物名称/货物重量/货物体积/货物件数/货物价值
        # # 单条货物信息
        # self.do_find(self.__BTN_CARGOE_TYPE).click()
        # self.do_find(self.__BTN_INPUT_CARGOE_TYPE).click()
        # self.do_send_keys(f"货物名称{data_time()}",self.__INPUT_CARGOES_NAME)
        # self.do_send_keys("103.33",self.__INPUT_CARGOES_TOTAL_WEIGHT)

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
        input_ele = self.do_find(By.XPATH, "//input[@data-testid='form-fee-input']")
        action = ActionChains(self.driver)
        action.move_to_element(input_ele).double_click(input_ele).send_keys(2000).perform()

        # input_ele.send_keys(keys.BACK_SPACE).perform()

        # self.driver.execute_script("arguments[0].value=200;",input_ele)
        # input_ele.send_keys(200)
        # 点击”确认开单“
        self.do_find(self.__BTN_ORDER_SUBMIT).click()
        logger.info("创建受理单成功")
        # self.get_screen()
        # ==>受理单
        from page_objectes.transport.ordermanagesys.order_list_page import OrdersListPage
        return OrdersListPage(self.driver)

    def switchcase(self, a):
        switcher = {
            0: "",
            1: "",
            2: ""

        }
        return switcher.get(a, "default")
