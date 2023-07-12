from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from PageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


#@pytest.mark.usefixtures("setup")

class TestOne (BaseClass):

    def test_e2e(self):

        #self.driver.implicitly_wait(10)


        # click on shop
        homePage = HomePage(self.driver)
        checkOutPage= homePage.shopItems()

        # Grab all the products
        products = self.driver.find_elements(By.XPATH, "//div[@class='card h-100']")
        i = -1

        for product in products:
            i = i+1
            productName = product.find_element(By.XPATH, "div/h4/a").text
            if productName == "Blackberry:":
                product.find_element(By.XPATH, "div/button").click()
        print(productName)
        # goto check out page
        self.driver.find_element(By.CSS_SELECTOR, ".nav-link.btn.btn-primary").click()
        # check out from that page
        self.driver.find_element(By.CSS_SELECTOR, ".btn.btn-success").click()
        # select country from auto suggestive drop down
        self.driver.find_element(By.ID, "country").send_keys("Ind")
        self.verifyLinkPresence("India")
        # select country and chick on the purchase
       # self.driver.find_element(By.XPATH, "//a[.='India']").click()
        #self.driver.find_element(By.CSS_SELECTOR, "div[class='checkbox checkbox-primary']").click()
        #self.driver.find_element(By.XPATH, "//input[@value='Purchase']").click()
        # verify the succes message
        #SuccesText = self.driver.find_element(By.CSS_SELECTOR, "div[class*='alert alert-success alert-dismissible']").text

        #assert "Success! Thank you!" in SuccesText

        #print(SuccesText)

