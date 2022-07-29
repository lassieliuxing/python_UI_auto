"""首页"""
import logging

from selenium.webdriver.common.by import By

from page_objectes.base_page import BasePage
from utils.log_utils import logger


class HomePage(BasePage):
    __BTN_ORDER=(By.XPATH, "//*[text()='受理开单']")
    __BTN_CREATE_ORDER=(By.XPATH, "//*[text()='创建受理单']")

    def goto_create_order(self):
        logger.info("进入创建受理单页面")
        # 点击菜单”受理单“
        self.do_find(self.__BTN_ORDER).click()
        # 点击菜单”创建受理单“
        self.do_find(self.__BTN_CREATE_ORDER).click()
        # ==》创建页
        from page_objectes.create_order_page import CreateOrderPage
        return CreateOrderPage(self.driver)