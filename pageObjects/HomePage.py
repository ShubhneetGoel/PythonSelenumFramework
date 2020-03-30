from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pageObjects.ABTesting import ABTesting
from pageObjects.AddRemoveElements import AddRemoveElements
from pageObjects.BasicAuthPage import BasicAuthPage
from pageObjects.BrokenImages import BrokenImages
from pageObjects.ChallengingDOM import ChallengingDOM


class HomePage:

    ABTestingLink = (By.LINK_TEXT, "A/B Testing")
    AddRemoveLink = (By.LINK_TEXT, "Add/Remove Elements")
    BasicAuthLink = (By.LINK_TEXT, "Basic Auth")
    BrokenImagesLink = (By.LINK_TEXT, "Broken Images")
    ChallengingDOMLink = (By.LINK_TEXT, "Challenging DOM")

    def __init__(self, driver):
        self.driver = driver

    def returnABTestingPage(self):
        self.driver.find_element(*HomePage.ABTestingLink).click()
        ABTestingInst = ABTesting(self.driver)
        return ABTestingInst

    def returnAddRemoveElementsPage(self):
        self.driver.find_element(*HomePage.AddRemoveLink).click()
        AddRemoveLinkInst = AddRemoveElements(self.driver)
        return AddRemoveLinkInst

    def returnBasicAuthPage(self,getData):
        link = self.driver.find_element(*HomePage.BasicAuthLink).get_attribute("href")
        index = link.find('//')
        print(index)
        link = link[:index+2] + getData["Username"] + ':' + getData["Password"]+ '@' + link[index+2:]
        self.driver.get(link)
        BasicAuthPageInst = BasicAuthPage(self.driver)
        return BasicAuthPageInst

    def returnBrokenImagesPage(self):
        self.driver.find_element(*HomePage.BrokenImagesLink).click()
        BrokenImagesInst = BrokenImages(self.driver)
        return BrokenImagesInst

    def returnChallengingDOM(self):
        self.driver.find_element(*HomePage.ChallengingDOMLink).click()
        ChallengingDOMInst = ChallengingDOM(self.driver)
        return ChallengingDOMInst
