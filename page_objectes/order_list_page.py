"""受理单页面"""
import logging

from selenium.webdriver.common.by import By

from page_objectes.base_page import BasePage
from utils.log_utils import logger


class OrdersListPage(BasePage):

    def get_operate_result(self):
        logger.info("获取受理单列表页")
        # 获取新增受理单
        # 返回消息文本
        res = self.driver.find_elements(By.XPATH, "//*[text()='创建开单客户3']")
        logging.info(f"断言获取到的实际结果为{res}")
        assert res != []
        return "创建成功"