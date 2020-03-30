from selenium.webdriver.common.by import By

class AddRemoveElements:

    addElementPath = (By.XPATH,"//button[contains(text(),'Add Element')]")
    deleteElementPath = (By.XPATH,"//button[@class='added-manually']")

    def __init__(self,driver):
        self.driver = driver

    def returnAddElement(self):
        return self.driver.find_element(*AddRemoveElements.addElementPath).click()

    def returnDeleteElement(self):
        return self.driver.find_element(*AddRemoveElements.deleteElementPath).click()

    def returnDeleteElementsSize(self):
        return len(self.driver.find_elements(*AddRemoveElements.deleteElementPath))