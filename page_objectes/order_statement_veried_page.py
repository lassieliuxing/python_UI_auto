class OrderStatementVeriedPage:
    def goto_statement_detail(self):
        from page_objectes.statement_detail_page import StatementDetailPage
        return StatementDetailPage(self.driver)