"""首页"""
from time import sleep

from selenium.webdriver.common.by import By

from page_objectes.base_page import BasePage
from utils.log_utils import logger


class HomePage(BasePage):
    __BTN_ORDER = (By.XPATH, "//*[text()='受理开单']")
    __BTN_CREATE_ORDER = (By.XPATH, "//*[text()='创建受理单']")
    __BTN_TRANSPORTSYS = (By.XPATH, "//*[text()='运输管理']")
    __BTN_DISPATCH = (By.XPATH, "//*[text()='调度计划']")
    __BTN_FULL_TRANSPORT = (By.XPATH, "//*[text()='整车运输']")
    __BTN_FULL_TRANSPORT_ALL = (By.XPATH, "//div[@id='rc-tabs-6-tab-COMPLETED']")
    __BTN_COMMON_INFORMATION=(By.XPATH,"//*[text()='常用信息']")
    __BTN_COMMON_ROUTE=(By.XPATH,"//*[text()='常用线路']")
    __BTN_COMMON_SHIPPER=(By.XPATH,"//*[text()='常用发货']")
    __BTN_COMMON_RECEIVE=(By.XPATH,"//*[text()='常用收货']")
    __BTN_COMMON_CARGOES=(By.XPATH,"//*[text()='常用货物']")

    def goto_create_order(self):
        logger.info("进入创建受理单页面")
        # 点击菜单”受理单“
        self.do_find(self.__BTN_ORDER).click()
        # 点击菜单”创建受理单“
        self.do_find(self.__BTN_CREATE_ORDER).click()
        # ==》创建页
        from page_objectes.ordersys.create_order_page import CreateOrderPage
        return CreateOrderPage(self.driver)
    def goto_common_information_route(self):
        logger.info("进入常用路线页面")
        self.do_find(self.__BTN_ORDER).click()
        self.do_find(self.__BTN_COMMON_INFORMATION).click()
        self.do_find(self.__BTN_COMMON_ROUTE)

    def goto_common_information_shipper(self):
        logger.info("进入常用发货页面")
        self.do_find(self.__BTN_ORDER).click()
        self.do_find(self.__BTN_COMMON_INFORMATION).click()
        self.do_find(self.__BTN_COMMON_SHIPPER)
    def goto_common_information_receive(self):
        logger.info("进入常用收货页面")
        self.do_find(self.__BTN_ORDER).click()
        self.do_find(self.__BTN_COMMON_INFORMATION).click()
        self.do_find(self.__BTN_COMMON_RECEIVE)
    def goto_common_information_cargoes(self):
        logger.info("进入常用货物页面")
        self.do_find(self.__BTN_ORDER).click()
        self.do_find(self.__BTN_COMMON_INFORMATION).click()
        self.do_find(self.__BTN_COMMON_CARGOES)


    def goto_dispatch(self):
        logger.info("进入调度计划页面")
        self.do_find(self.__BTN_TRANSPORTSYS).click()
        sleep(1)
        self.do_find(self.__BTN_DISPATCH).click()

        from page_objectes.transport.diapstchsys.dispatch_list_page import DispatchListPage
        return DispatchListPage(self.driver)

    def goto_order_statement_detail(self):
        logger.info("进入到对账管理-应收明细页面")
        from page_objectes.orderstatementsys.order_statement_detail_page import OrderStatementDetailPage
        return OrderStatementDetailPage()

    def goto_full_transporting(self):
        logger.info("进入整车运输页面-运输中")
        self.do_find(self.__BTN_TRANSPORTSYS).click()
        self.do_find(self.__BTN_FULL_TRANSPORT).click()

        from page_objectes.transport.fulltransportsys.full_transporting_page import FullTransportIngPage
        return FullTransportIngPage(self.driver)

    def goto_full_transport_all(self):
        logger.info("进入整车运输页面-全部")
        self.do_find(self.__BTN_TRANSPORTSYS).click()
        self.do_find(self.__BTN_FULL_TRANSPORT).click()

        from page_objectes.transport.fulltransportsys.full_transporting_page import FullTransportIngPage
        return FullTransportIngPage(self.driver)
