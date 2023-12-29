from page_objectes.login_page import LoginPage


class Test_vehicle:
    def setup_class(self):
        self.home = LoginPage().login("18900000000","1111111l")

    # def teardown_class(self):
    #     self.home.do_quit()

    def test_create_vehicle(self):
        self.home.goto_create_vehicle().createVehicle()
