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
        listpage=self.home\
            .goto_create_order()\
            .create_order("创建开单客户3","20220810001","100","0","1","55.5","200")
        res=listpage.get_operate_result()
        assert "创建成功"==res
        print(res)

