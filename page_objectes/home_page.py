"""首页"""
import logging
from time import sleep

from selenium.webdriver.common.by import By

from page_objectes.base_page import BasePage
from utils.log_utils import logger


class HomePage(BasePage):
    __BTN_ORDER=(By.XPATH, "//*[text()='受理开单']")
    __BTN_CREATE_ORDER=(By.XPATH, "//*[text()='创建受理单']")
    __BTN_TRANSPORTSYS=(By.XPATH,"//*[text()='运输管理']")
    __BTN_DISPATCH=(By.XPATH,"//*[text()='调度计划']")

    def goto_create_order(self):
        logger.info("进入创建受理单页面")
        # 点击菜单”受理单“
        self.do_find(self.__BTN_ORDER).click()
        # 点击菜单”创建受理单“
        self.do_find(self.__BTN_CREATE_ORDER).click()
        # ==》创建页
        from page_objectes.create_order_page import CreateOrderPage
        return CreateOrderPage(self.driver)
    def goto_dispatch(self):
        logger.info("进入调度计划页面")
        self.do_find(self.__BTN_TRANSPORTSYS).click()
        sleep(1)
        self.do_find(self.__BTN_DISPATCH).click()
        from page_objectes.dispatch_list_page import DispatchListPage
        return DispatchListPage(self.driver)
    def goto_order_statement_detail(self):
        logger.info("进入到对账管理-应收明细页面")
        from page_objectes.order_statement_detail_page import OrderStatementDetailPage
        return OrderStatementDetailPage()