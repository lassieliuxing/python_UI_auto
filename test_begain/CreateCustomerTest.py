from page_objectes.login_page import LoginPage


class Test_customer:
    def setup_class(self):
        self.home = LoginPage().login("18900000000", "1111111l")

    def teardown_class(self):
        self.home.do_quit()
    def test_create_base_customer(self):
        self.home.goto_customer().create_customer().input_require_info()

