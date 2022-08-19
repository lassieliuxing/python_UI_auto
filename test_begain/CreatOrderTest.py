import logging
import time

import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from page_objectes.login_page import LoginPage


class Test_Order:
    def setup_class(self):
        self.home = LoginPage().login("13900000000","1111111l")
    def teardown_class(self):
        self.home.do_quit()

    def test_create_order(self):

        customer_name="创建开单客户3"
        cargoes_weight="100"
        cargoes_volume="0"
        cargoes_num="1"
        cargoes_money="55.5"
        order_fee="200"
        # list=[1,2,3,4,5,6,7,8,9]
        # for i in list:
        # customer_num = f"2022081900{3}"
        customer_num = "20220819004"
        self.home\
                .goto_create_order()\
                .create_order(customer_name,customer_num,cargoes_weight,cargoes_volume,cargoes_num,cargoes_money,order_fee)
        # res=listpage.get_operate_result()
        # assert "创建成功"==res
        # print(res)
    # def test_more_order(self):
    #     list=[2, 3, 4, 5, 6,]
    #     for i in list:
    #         self.test_create_order(i)

