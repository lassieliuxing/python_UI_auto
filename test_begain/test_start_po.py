import logging
import time

import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from page_objectes.login_page import LoginPage


class Test_start_po:
    def setup_class(self):
        self.home = LoginPage().login()


    def test_create_order(self):
        res=self.home\
            .goto_create_order()\
            .create_order()\
            .get_operate_result()
        print(res)
