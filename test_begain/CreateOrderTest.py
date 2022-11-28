import logging
import time
from typing import List

import allure
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from page_objectes.login_page import LoginPage
from utils.data_utils import data_time


class Test_Order:

    def setup_class(self):
        self.home = LoginPage().login("18900000000","1111111l")


    def teardown_class(self):
        self.home.do_quit()

    def test_create_order(self):
        count = 1
        while count<=10:

            customer_name="企业客户2"
            cargoes_weight="100"
            cargoes_volume="0"
            cargoes_num="1"
            cargoes_money="55.5"
            order_fee="430"
            customer_num = f"20220826000{data_time()}"
            self.home\
                    .goto_create_order()\
                    .create_order(customer_name,customer_num,order_fee)
            count=count+1
            # res=listpage.get_operate_result()
            # assert "创建成功"==res
            # print(res)





