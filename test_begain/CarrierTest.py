from typing import List

from page_objectes.login_page import LoginPage


class Test_carrier:
    def setup_class(self):
        self.home = LoginPage().login("18900000000","1111111l")
    def teardown_class(self):
        self.home.do_quit()
    # def test_ceate_carrier(self):
    #     self.home.goto_carrier_manage().create_carrier().create_require_input()
    def test_query_carrier(self):
        self.home.goto_carrier_manage().search_carrier()

