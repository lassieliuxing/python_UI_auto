import allure
from selenium.webdriver.common.by import By

from page_objectes.base_page import BasePage


@allure.feature("创建受理单模块")
class CreateVehiclePage(BasePage):
    __INPUT_PLATE=(By.CSS_SELECTOR, "input[aria-required='true']")
    __CHOOSE_COLOR=(By.CSS_SELECTOR,"input[id$='plateColorCode']")
    __CHOOSE_COLOR_ITEM=(By.CSS_SELECTOR,"span[title='蓝色']")
    __CHOOSE_LENTH=(By.CSS_SELECTOR,"input[id$='vehicleLengthCode']")
    __CHOOSE_LENTH_ITEM=(By.CSS_SELECTOR,"span[title='1.80米']")
    __CHOOSE_DATE=(By.CSS_SELECTOR,"div[class$='ant-picker-focused']")
    __CHOOSE_DATE_RETIR=(By.CSS_SELECTOR,"input[id$='mandatoryRetirementTime']")
    __CHOOSE_DATE_TODAY=(By.CSS_SELECTOR,"input[id$='annualInspectionTime']")


        
    
    def createVehicle(self):
       self.do_send_keys("川A81888",self.__INPUT_PLATE)
       self.do_find(self.__CHOOSE_COLOR).click()
       self.do_find(self.__CHOOSE_COLOR_ITEM).click()
       self.do_find(self.__CHOOSE_LENTH).click()
       self.do_find(self.__CHOOSE_LENTH_ITEM).click()
       self.do_find(self.__CHOOSE_DATE).click()
       self.do_find(self.__CHOOSE_DATE_TODAY).click()

       from page_objectes.driverandvehicle.VehicleListPage import VehicleListPage
       return VehicleListPage(self.driver)
