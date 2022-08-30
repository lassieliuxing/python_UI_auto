from selenium.webdriver.common.by import By

from page_objectes.base_page import BasePage


class OrderStatementDetailPage(BasePage):

    def order_price_revision(self):
        self.do_find(By.XPATH,"//a[text()='2022082940001112']/../..//span[@data-testid='setting-icon']").click()
        self.do_find(By.XPATH,"//*[text()='费用调整']").click()
        # 点击费用调整
        # 跳转费用调整框
        from page_objectes.price_revision_page import PriceRevisionPage
        return  PriceRevisionPage(self.driver)
    def get_order_price_total(self):
        pass
        # self.do_find(By.XPATH,"//a[text()='2022082940001112']/../..//span[text()='-30']")
        # 判断费用调整总额

    def order_price_total_list(self):
        # 查看调整总额里的明细
        pass

    def order_price_detail(self):

        from page_objectes.transport.ordermanagesys.order_detail_page import OrderDetailPage
        return OrderDetailPage(self.driver)
        pass
    def goto_statement_verify(self):
        # 输入客户企业名
        # 点击查询
        # 勾选受理单
        # 点击对账
        from page_objectes.orderstatementsys.order_statement_verify_page import OrderStatementVerfyPage
        return OrderStatementVerfyPage()