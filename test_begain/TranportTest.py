class Test_Transport:
    def setup_class(self):
        from page_objectes.login_page import LoginPage
        self.home = LoginPage().login("13900000000", "1111111l")

    def teardown_class(self):
        self.home.do_quit()

    def test_transport_from_start_to_sign(self):
        waybillnum = "CW2022081027008001"
        self.home.goto_full_transporting() \
            .confirm_start(waybillnum)    \
            .confirm_arrive(waybillnum) \
            .confirm_sign(waybillnum)


    def test_transport_sign_from_wait_depart(self):
        waybillnum = "CW2022081129000601"
        self.home.goto_full_transporting() \
            .confirm_sign(waybillnum)

    def test_transport_sign_from_wait_arrive(self):
        waybillnum = "CW2022081129000601"
        self.home.goto_full_transporting() \
            .confirm_start(waybillnum) \
            .confirm_sign(waybillnum)
