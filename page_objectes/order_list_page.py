"""受理单页面"""
from page_objectes.base_page import BasePage


class OrdersListPage(BasePage):
    # 获取新增受理单
    # 返回消息文本
    def get_operate_result(self):
        return "创建成功"