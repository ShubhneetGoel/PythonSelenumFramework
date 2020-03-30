from selenium.webdriver.common.by import By

class ABTesting:


    h3Heading = (By.TAG_NAME,"h3")


    def __init__(self,driver):
        self.driver = driver

    def returnh3text(self):
        return self.driver.find_element(*ABTesting.h3Heading).text
