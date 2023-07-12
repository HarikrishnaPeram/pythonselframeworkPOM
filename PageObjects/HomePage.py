from selenium.webdriver.common.by import By


class CheckOutPage:
    pass


class HomePage:
    def __init__(self, driver):
        self.driver = driver



    shop =(By.XPATH,"//a[.='Shop']")

    def shopItems(self):
      self.driver.find_element(*HomePage.shop).click()
      checkOutPage = CheckOutPage(self.driver)
      
      
      return checkOutPage
        #driver.find_element(By.XPATH, "//a[.='Shop']").click()