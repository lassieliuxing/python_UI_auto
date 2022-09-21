from page_objectes.login_page import LoginPage


class Test_carrier:
    def setup_class(self):
        self.home = LoginPage().login("18900000000","1111111l")
    def teardown_class(self):
        self.home.do_quit()
    def test_ceate_carrier(self):
        self.home.goto_carrier_manage()