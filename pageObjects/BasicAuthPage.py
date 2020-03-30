from selenium.webdriver.common.by import By

class BasicAuthPage:

    checkTextPath = (By.TAG_NAME,"P")

    def __init__(self, driver):
        self.driver = driver

    def returnPText(self):
        return self.driver.find_element(*BasicAuthPage.checkTextPath).text


