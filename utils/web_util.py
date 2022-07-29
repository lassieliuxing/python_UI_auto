from utils.log_utils import logger


def click_exception(by,element,max_attempts=5):
    def _inner(driver):
        #多次点击按钮
        actul_attempts = 0 #实际点击次数
        while actul_attempts<max_attempts:
            actul_attempts += 1
            try:
                #如果点击过程报错，执行except，并继续循环
                #没有报错，直接return循环结束
                driver.find_element(by, element).click()
                return True
            except Exception:
                logger.info("在点击时报错")
                # 当大于最大次数，结束循环，抛出异常
        raise Exception("超出最大点击次数")
    return  _inner()