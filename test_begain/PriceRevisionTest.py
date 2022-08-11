from page_objectes.login_page import LoginPage


class Test_PriceRevision:
    def setup_class(self):
        self.home = LoginPage().login("13900000000", "1111111l")
    #
    # def teardown_class(self):
    #     self.home.do_quit()
    def test_order_price_revision(self):
        self.home.goto_order_statement_detail().order_price_revision().price_revision()