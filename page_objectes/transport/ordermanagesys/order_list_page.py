"""受理单页面"""
import logging

from selenium.webdriver.common.by import By

from page_objectes.base_page import BasePage
from utils.log_utils import logger


class OrdersListPage(BasePage):
    __MSG_ADD_OPERATE = (By.XPATH, "//*[text()='创建开单客户3']")

    def get_add_order_result(self):
        logger.info("获取受理单列表页")
        # 获取新增受理单
        # 返回消息文本
        res = self.wait_element_until_visible(self.__MSG_ADD_OPERATE)
        logging.info(f"断言获取到的实际结果为{res}")
        assert res != []
        return "创建成功"

    def get_order_detail(self):
        pass
        return OrdersListPage()
