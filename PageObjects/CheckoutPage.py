from selenium.webdriver.common.by import By


class Checkoutpage:
    def __init__(self,driver):
        self.driver = driver
        productName=(By.XPATH, "div/h4/a")

    def getproductname(self):
        return self.driver.find_element(*Checkoutpage.getproductname())