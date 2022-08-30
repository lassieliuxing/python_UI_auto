from page_objectes.login_page import LoginPage


class Test_Dispatch:

        def setup_class(self):
            self.home = LoginPage().login("18900000000", "1111111l")

        def teardown_class(self):
            self.home.do_quit()
        def test_dispatch_only_deliver(self):
            ordernum="2022081930008309"
            self.home.goto_dispatch() \
            .diapstch_order(ordernum) .input_dispatch_with_deliver()
        def test_dispatch_with_all(self):
            ordernum = "2022081930008309"
            self.home.goto_dispatch()\
                .diapstch_order(ordernum)\
                .input_dispatch_with_advance_and_deliver_and_banlance()