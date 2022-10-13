from selenium.webdriver.common.by import By

from page_objectes.base_page import BasePage
from utils.log_utils import logger


class ExternalVehicleListPage(BasePage):
    __BTN_EXTERNAL_CREATE_VEHICLE=(By.XPATH,"//span[text()='添 加']")
    __BTN_EXTERNAL_SEARCH_VEHICLE=(By.XPATH,"//span[text()='查询']")
    __BTN_EXTERNAL_RESET_VEHICLE=(By.XPATH,"//span[text()='重置']")
    __INPUT_EXTERNAL_SEARCH_VEHICLE_PLATE=(By.XPATH,"//input[@data-testid='drivers-vehicles-input']")
    __BTN_EXTERNAL_VEHICLE_SWITCH=(By.XPATH,"//button[@data-testid='car-enable-switch']")
    def create_vehicle(self):
        logger.info("进入外协车辆管理页面")
        self.do_find(self.__BTN_EXTERNAL_CREATE_VEHICLE).click()
        from page_objectes.driverandvehicle.external.input_external_vehicle_info_page import \
            InputExternalVehicleInfoPage
        return InputExternalVehicleInfoPage(self.driver)

    def search_vehicle(self):
        pass
    def modify_vehicle(self):
        from page_objectes.driverandvehicle.external.input_external_vehicle_info_page import \
            InputExternalVehicleInfoPage
        return InputExternalVehicleInfoPage(self.driver)