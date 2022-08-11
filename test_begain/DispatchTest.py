from page_objectes.login_page import LoginPage


class Test_Dispatch:

        def setup_class(self):
            self.home = LoginPage().login("13900000000", "1111111l")
        #
        # def teardown_class(self):
        #     self.home.do_quit()
        def test_dispatch(self):
            self.home.goto_dispatch()  \
            .diapstch_order() .input_dispatch_with_deliver()
