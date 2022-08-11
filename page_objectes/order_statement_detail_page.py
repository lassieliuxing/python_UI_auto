import logging


class OrderStatementDetailPage:

    def order_price_revision(self):

        # 点击费用调整
        # 跳转费用调整框
        from page_objectes.price_revision_page import PriceRevisionPage
        return  PriceRevisionPage()
    def order_price_total(self):
        pass
        # 判断费用调整总额

    def order_price_total_list(self):
        # 查看调整总额里的明细
        pass

    def order_price_detail(self):

        from page_objectes.order_detail_page import OrderDetailPage
        return OrderDetailPage(self.driver)
        pass
    def goto_statement_verify(self):
        # 输入客户企业名
        # 点击查询
        # 勾选受理单
        # 点击对账
        from page_objectes.order_statement_verify_page import OrderStatementVerfyPage
        return OrderStatementVerfyPage()