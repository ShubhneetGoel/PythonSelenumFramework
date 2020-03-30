from selenium.webdriver.common.by import By


class ChallengingDOM:

    def __init__(self, driver):
        self.driver = driver

    def returnChallengingDOMElements(self,getData):
        strPath = "//td[contains(text(),'"+ getData["var"] +"')]/parent::tr/td"
        ChallengingDOMElementsPath = (By.XPATH, strPath)
        ChallengingDOMElements = self.driver.find_elements(*ChallengingDOMElementsPath)
        return ChallengingDOMElements