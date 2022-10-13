"""首页"""
from time import sleep

from selenium.webdriver.common.by import By

from page_objectes.base_page import BasePage
from utils.log_utils import logger


class HomePage(BasePage):
    # 一级菜单
    __BTN_ORDER = (By.XPATH, "//*[text()='受理开单']")
    __BTN_TRANSPORTSYS = (By.XPATH, "//*[text()='运输管理']")
    __BTN_FINANCE_SYS = (By.XPATH, "//span[text()='财务管理']")
    __BTN_CUSTOMER_SYS = (By.XPATH, "//span[text()='客户管理']")
    __BTN_TRANSPORT_CAPACITY_SYS = (By.XPATH, "//span[text()='运力管理']")
    __BTN_CARRIER_SYS = (By.XPATH, "//span[text()='承运商管理']")
    __BTN_REPORT_SYS = (By.XPATH, "//span[text()='报表中心']")
    # 二级菜单
    # 受理开单
    __BTN_CREATE_ORDER = (By.XPATH, "//*[text()='创建受理单']")
    __BTN_COMMON_INFORMATION = (By.XPATH, "//*[text()='常用信息']")
    # 运输管理
    __BTN_ORDERMANAGE = (By.XPATH, "//*[text()='受理单管理']")
    __BTN_DISPATCH = (By.XPATH, "//*[text()='调度计划']")
    __BTN_FULL_TRANSPORT = (By.XPATH, "//*[text()='整车运输']")
    __BTN_SELF_TRANSPORT = (By.XPATH, "//*[text()='自有运输']")
    __BTN_CARIIER_TRANSPORT = (By.XPATH, "//*[text()='承运商运输']")
    __BTN_RECEIPT_MANAGE = (By.XPATH, "//*[text()='回单管理']")
    __BTN_ANOMALIES_MANAGE = (By.XPATH, "//*[text()='异常管理']")
    # 财务管理
    __BTN_FINANCE_ORDER = (By.XPATH, "//span[text()='受理单结算']")
    __BTN_FINANCE_CARRIER = (By.XPATH, "//span[text()='承运商结算']")
    __BTN_FINANCE_FULL_TRUCK = (By.XPATH, "//span[text()='整车核销']")
    __BTN_FINANCE_OTHER_FEE = (By.XPATH, "//span[text()='其他费用核销']")
    # 运力管理
    __BTN_EXTRA_CAPACITY = (By.XPATH, "//span[text()='外协运力']")
    __BTN_SELF_CAPACITY = (By.XPATH, "//span[text()='自有运力']")

    # 三级菜单

     # 受理单结算
    __BTN_FINANCE_STATEMENT_MANAGE = (By.XPATH, "//span[text()='对账管理']")
    __BTN_FINANCE_INVOICE_MANAGE = (By.XPATH, "//span[text()='发票管理']")
    __BTN_FINANCE_RECEIVE_MANAGE = (By.XPATH, "//span[text()='收款管理']")
     # 承运商结算
    __BTN_FINANCE_CARRIER_STATEMENT_VERIFY = (By.XPATH, "//span[text()='对账管理']")

    # 标签页
     # 常用信息
    __BTN_COMMON_ROUTE = (By.XPATH, "//*[text()='常用线路']")
    __BTN_COMMON_SHIPPER = (By.XPATH, "//*[text()='常用发货']")
    __BTN_COMMON_RECEIVE = (By.XPATH, "//*[text()='常用收货']")
    __BTN_COMMON_CARGOES = (By.XPATH, "//*[text()='常用货物']")
     # 受理单管理
    __BTN_ORDER_TRANSPORTING = (By.XPATH, "//*[text()='运输中']")
    __BTN_ORDER_ALL = (By.XPATH, "//*[text()='全部']")
     # 整车运输
    __BTN_FULL_TRUCK_ALL = (By.XPATH, "//*[text()='全部']")
     # 自有运输
    __BTN_SELF_ALL = (By.XPATH, "//*[text()='全部']")
     # 承运商运输
    __BTN_CARRIER_ALL = (By.XPATH, "//*[text()='全部']")
     # 回单管理
    __BTN_RECEIPT_VERIFIED = (By.XPATH, "//*[text()='已核销']")
     # 对账管理
    __BTN_FINANCE_FULL_TRUCK_STATEMENT_VERIFY = (By.XPATH, "//span[text()='对账核销']")
    __BTN_FINANCE_STATEMENT_VERIFIED = (By.XPATH, "//span[text()='已核销']")
     # 发票管理
    __BTN_FINANCE_INVOICE_RECORD = (By.XPATH, "//span[text()='开票记录']")
     # 收款管理
    __BTN_FINANCE_RECEIVE_RECORD = (By.XPATH, "//span[text()='收款记录']")
     # 整车核销
    __BTN_FINANCE_FULL_TRUCK_STATEMENT_VERIFIED = (By.XPATH, "//span[text()='已核销']")
     # 其他费用核销
    __BTN_FINANCE_OTHER_FEE_VERIFIED = (By.XPATH, "//span[text()='已核销']")

     # 外协运力
    __BTN_EXTRA_VECHILE = (By.XPATH, "//span[text()='车辆管理']")
     # 自有运力
    __BTN_SELF_VECHILE = (By.XPATH, "//span[text()='车辆管理']")



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


    def goto_order_manage_wait_dispatch(self):
        logger.info("进入受理单管理页面-待调度")
        self.do_find(self.__BTN_TRANSPORTSYS).click()
        sleep(1)
        self.do_find(self.__BTN_ORDERMANAGE).click()
        from page_objectes.transport.ordermanagesys.order_wait_dispatch_page import OrderWaitDispatchPage
        return OrderWaitDispatchPage()
    def goto_order_manage_transporting(self):
        logger.info("进入受理单管理页面-运输中")
        self.do_find(self.__BTN_TRANSPORTSYS).click()
        sleep(1)
        self.do_find(self.__BTN_ORDERMANAGE).click()
        self.do_find(self.__BTN_ORDER_TRANSPORTING).click()


    def goto_order_manage_all(self):
        logger.info("进入受理单管理页面-全部")
        self.do_find(self.__BTN_TRANSPORTSYS).click()
        sleep(1)
        self.do_find(self.__BTN_ORDERMANAGE).click()
        self.do_find(self.__BTN_ORDER_ALL).click()



    def goto_dispatch(self):
        logger.info("进入调度计划页面")
        self.do_find(self.__BTN_TRANSPORTSYS).click()
        sleep(1)
        self.do_find(self.__BTN_DISPATCH).click()
        from page_objectes.transport.diapstchsys.dispatch_list_page import DispatchListPage
        return DispatchListPage(self.driver)



    def goto_full_truck_transporting(self):
        logger.info("进入整车运输页面-运输中")
        self.do_find(self.__BTN_TRANSPORTSYS).click()
        sleep(1)
        self.do_find(self.__BTN_FULL_TRANSPORT).click()
        from page_objectes.transport.fulltransportsys.full_transporting_page import FullTransportIngPage
        return FullTransportIngPage(self.driver)

    def goto_full_truck_all(self):
        logger.info("进入整车运输页面-全部")
        self.do_find(self.__BTN_TRANSPORTSYS).click()
        sleep(1)
        self.do_find(self.__BTN_FULL_TRANSPORT).click()
        self.do_find(self.__BTN_FULL_TRUCK_ALL).click()
        from page_objectes.transport.fulltransportsys.full_transporting_page import FullTransportIngPage
        return FullTransportIngPage(self.driver)
    def goto_self_transporting(self):
        logger.info("进入自有运输页面-运输中")
        self.do_find(self.__BTN_TRANSPORTSYS).click()
        sleep(1)
        self.do_find(self.__BTN_SELF_TRANSPORT).click()

    def goto_self_all(self):
        logger.info("进入自有运输页面-全部")
        self.do_find(self.__BTN_TRANSPORTSYS).click()
        sleep(1)
        self.do_find(self.__BTN_SELF_TRANSPORT).click()
        self.do_find(self.__BTN_SELF_ALL).click()
    def goto_carrier_transporting(self):
        logger.info("进入承运商运输页面-运输中")
        self.do_find(self.__BTN_TRANSPORTSYS).click()
        sleep(1)
        self.do_find(self.__BTN_CARIIER_TRANSPORT).click()

    def goto_carrier_all(self):
        logger.info("进入承运商运输页面-全部")
        self.do_find(self.__BTN_TRANSPORTSYS).click()
        sleep(1)
        self.do_find(self.__BTN_CARIIER_TRANSPORT).click()
        self.do_find(self.__BTN_CARRIER_ALL).click()

    def goto_receipt(self):
        logger.info("进入回单管理页面")
        self.do_find(self.__BTN_TRANSPORTSYS).click()
        sleep(1)
        self.do_find(self.__BTN_RECEIPT_MANAGE).click()
    def goto_receipt_verified(self):
        logger.info("进入回单管理页面-已核销")
        self.do_find(self.__BTN_TRANSPORTSYS).click()
        sleep(1)
        self.do_find(self.__BTN_RECEIPT_MANAGE).click()
        self.do_find(self.__BTN_RECEIPT_VERIFIED).click()

    def goto_anomalies_list(self):
        logger.info("进入异常管理页面")
        self.do_find(self.__BTN_TRANSPORTSYS).click()
        sleep(1)
        self.do_find(self.__BTN_ANOMALIES_MANAGE).click()



    def goto_finance_order_statement(self):
        logger.info("进入到对账管理-应收明细页面")
        self.do_find(self.__BTN_FINANCE_SYS).click()
        sleep(1)
        self.do_find(self.__BTN_FINANCE_ORDER).click()
        self.do_find(self.__BTN_FINANCE_STATEMENT_MANAGE).click()
        sleep(2)
        self.do_find(By.XPATH, "//span[text()='知道了']").click()
        from page_objectes.orderstatementsys.order_statement_detail_page import OrderStatementDetailPage
        return OrderStatementDetailPage(self.driver)

    def goto_finance_order_statement_verify(self):
        logger.info("进入到对账管理-对账核销页面")
        self.do_find(self.__BTN_FINANCE_SYS).click()
        sleep(1)
        self.do_find(self.__BTN_FINANCE_ORDER).click()
        self.do_find(self.__BTN_FINANCE_STATEMENT_MANAGE).click()
        self.do_find(self.__BTN_FINANCE_FULL_TRUCK_STATEMENT_VERIFY)
        from page_objectes.orderstatementsys.order_statement_verify_page import OrderStatementVerfyPage
        return OrderStatementVerfyPage()

    def goto_finance_order_statement_veried(self):
        logger.info("进入到对账管理-对账已核销页面")
        self.do_find(self.__BTN_FINANCE_SYS).click()
        self.do_find(self.__BTN_FINANCE_ORDER).click()
        sleep(1)
        self.do_find(self.__BTN_FINANCE_STATEMENT_MANAGE)
        self.do_find(self.__BTN_FINANCE_STATEMENT_VERIFIED).click()
        from page_objectes.orderstatementsys.order_statement_veried_page import OrderStatementVeriedPage
        return OrderStatementVeriedPage()

    def goto_invoice_waite_invoice(self):
        logger.info("进入待开发票页面")
        self.do_find(self.__BTN_FINANCE_SYS).click()
        self.do_find(self.__BTN_FINANCE_ORDER).click()
        self.do_find(self.__BTN_FINANCE_INVOICE_MANAGE).click()
    def goto_invoice_record(self):
        logger.info("进入开票记录页面")
        self.do_find(self.__BTN_FINANCE_SYS).click()
        self.do_find(self.__BTN_FINANCE_ORDER).click()
        self.do_find(self.__BTN_FINANCE_INVOICE_MANAGE).click()
        self.do_find(self.__BTN_FINANCE_INVOICE_RECORD).click()
    def goto_receive_waite_receive(self):
        logger.info("进入待收款页面")
        self.do_find(self.__BTN_FINANCE_SYS).click()
        self.do_find(self.__BTN_FINANCE_ORDER).click()
        self.do_find(self.__BTN_RECEIPT_MANAGE).click()
    def goto_receive_record(self):
        logger.info("进入收款记录页面")
        self.do_find(self.__BTN_FINANCE_SYS).click()
        self.do_find(self.__BTN_FINANCE_ORDER).click()
        self.do_find(self.__BTN_RECEIPT_MANAGE).click()
        self.do_find(self.__BTN_FINANCE_RECEIVE_RECORD).click()
    def goto_carrier_receive_list(self):
        logger.info("进入承运商应收明细页面")
        self.do_find(self.__BTN_FINANCE_SYS).click()
        self.do_find(self.__BTN_FINANCE_CARRIER).click()
        self.do_find(self.__BTN_FINANCE_CARRIER_STATEMENT_VERIFY).click()

    def goto_full_truck_verify(self):
        logger.info("进入整车核销页面")
        self.do_find(self.__BTN_FINANCE_SYS).click()
        self.do_find(self.__BTN_FINANCE_FULL_TRUCK).click()
    def goto_full_truck_verifed(self):
        logger.info("进入整车核销页面-已核销")
        self.do_find(self.__BTN_FINANCE_SYS).click()
        self.do_find(self.__BTN_FINANCE_FULL_TRUCK).click()
        self.do_find(self.__BTN_FINANCE_FULL_TRUCK_STATEMENT_VERIFIED).click()

    def goto_other_fee_verify(self):
        logger.info("进入其他费用核销页面-未核销")
        self.do_find(self.__BTN_FINANCE_SYS).click()
        self.do_find(self.__BTN_FINANCE_OTHER_FEE).click()
    def goto_other_fee_verifed(self):
        logger.info("进入其他费用核销页面-已核销")
        self.do_find(self.__BTN_FINANCE_SYS).click()
        self.do_find(self.__BTN_FINANCE_OTHER_FEE).click()
        self.do_find(self.__BTN_FINANCE_OTHER_FEE_VERIFIED).click()
    def goto_customer(self):
        logger.info("进入客户管理页面")
        self.do_find(self.__BTN_CUSTOMER_SYS).click()
        from page_objectes.customersys.customer_list_page import CustomerListPage
        return CustomerListPage(self.driver)

    def goto_transport_capacity_extra_driver(self):
        logger.info("进入外协运力-司机管理页面")
        self.do_find(self.__BTN_TRANSPORT_CAPACITY_SYS).click()
        self.do_find(self.__BTN_EXTRA_CAPACITY).click()
    def goto_transport_capacity_extra_vehicle(self):
        logger.info("进入外协运力-车辆管理页面")
        self.do_find(self.__BTN_TRANSPORT_CAPACITY_SYS).click()
        self.do_find(self.__BTN_EXTRA_CAPACITY).click()
        self.do_find(self.__BTN_EXTRA_VECHILE).click()
    def goto_transport_capacity_self_driver(self):
        logger.info("进入自有运力-司机管理页面")
        self.do_find(self.__BTN_TRANSPORT_CAPACITY_SYS).click()
        self.do_find(self.__BTN_SELF_TRANSPORT).click()
    def goto_transport_capacity_self_vehicle(self):
        logger.info("进入自有运力-车辆管理页面")
        self.do_find(self.__BTN_TRANSPORT_CAPACITY_SYS).click()
        self.do_find(self.__BTN_SELF_TRANSPORT).click()
        self.do_find(self.__BTN_SELF_VECHILE).click()
    def goto_carrier_manage(self):
        logger.info("进入承运商管理页面")
        self.do_find(self.__BTN_CARRIER_SYS).click()
        sleep(2)
        from page_objectes.carriersys.carrier_list_page import CarrierManagePage
        return CarrierManagePage(self.driver)

    def goto_report_center(self):

        logger.info("进入报表中心页面")
        self.do_find(self.__BTN_REPORT_SYS).click()

