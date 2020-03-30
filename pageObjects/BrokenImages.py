from selenium.webdriver.common.by import By


class BrokenImages:

    ImagesPath = (By.XPATH,"//div[@id='content']//img")

    def __init__(self, driver):
        self.driver = driver

    def returnImages(self):
        return self.driver.find_elements(*BrokenImages.ImagesPath)
