"""首页"""
from page_objectes.base_page import BasePage


class HomePage(BasePage):
    def goto_create_order(self):
        # 点击菜单”受理单“
        # 点击菜单”创建受理单“
        # ==》创建页
        from page_objectes.create_order_page import CreateOrderPage
        return CreateOrderPage(self.driver)