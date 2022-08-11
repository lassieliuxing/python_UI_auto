class OrderStatementVerfyPage:
    def statementList_total(self):
        pass

    def statementList_total_list(self):
        pass

    def goto_statementList_detail(self):
        from page_objectes.statement_detail_page import StatementDetailPage
        return StatementDetailPage(self.driver)

    def statement_price_revision(self):

        from page_objectes.price_revision_page import PriceRevisionPage
        return PriceRevisionPage(self.driver)
    def goto_statement_veried(self):
        from page_objectes.order_statement_veried_page import OrderStatementVeriedPage
        return OrderStatementVeriedPage(self.driver)
        # 点击操作
        # 点击核销
