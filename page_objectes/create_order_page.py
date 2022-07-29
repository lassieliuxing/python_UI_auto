"""创建受理单页"""
from page_objectes.base_page import BasePage


class CreateOrderPage(BasePage):
    # 输入”所属信息“-客户企业名/客户单号
    # 输入”发货信息“-发货人/电话/单位/地址
    # 输入”收货信息“-收货人/电话/单位/地址
    # 输入”货物信息“-货物类型/货物名称/货物重量/货物体积/货物件数/货物价值
    # 输入”费用信息“
    # 点击”确认开单“
    # ==>受理单
    def create_order(self):

        from page_objectes.order_list_page import OrdersListPage
        return OrdersListPage(self.driver)