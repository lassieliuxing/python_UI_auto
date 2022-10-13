from selenium.webdriver.common.by import By

from page_objectes.base_page import BasePage
from utils.log_utils import logger


class InputExternalVehicleInfoPage(BasePage):
    __INPUT_EXTERNAL_PLATE_PROVINCE=(By.XPATH,"//*[@data-testid='car-province-select']")
    __INPUT_EXTERNAL_PLATE_NUMBER=(By.XPATH,"//*[@data-testid='car-plate-input']")
    __INPUT_EXTERNAL_PLATE_COLOR=(By.XPATH,"//input[@id='plateColorCode']")
    __INPUT_EXTERNAL_VEHICLE_TYPE=(By.XPATH,"//input[@id='vehicleTypeCode']")
    __INPUT_EXTERNAL_VEHICLE_LENGTH=(By.XPATH,"//input[@id='vehicleLengthCode']")
    __INPUT_EXTERNAL_VEHICLE_CONFIRM=(By.XPATH,"//button[@data-testid='confirm-button']")

    def input_require_info(self):
        logger.info("进入外协车辆输入信息页面")

        from page_objectes.driverandvehicle.external.external_vehicle_list_page import ExternalVehicleListPage
        return ExternalVehicleListPage(self.driver)
    def input_all_info(self):
        pass
    def modify_info(self):
        pass