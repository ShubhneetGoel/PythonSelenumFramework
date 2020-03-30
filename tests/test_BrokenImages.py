import pytest
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pageObjects.BrokenImages import BrokenImages
from pageObjects.HomePage import HomePage
from testData.AbTestingData import ABTestingData
from testData.AddRemoveElements import AddRemoveElements
from testData.BasicAuth import BasicAuth
from utilities.BaseClass import BaseClass


class TestBrokenImages(BaseClass):

    def test_BrokenImages(self):
        log = self.get_logger()
        homePage = HomePage(self.driver)
        brokenImagesPage = homePage.returnBrokenImagesPage()
        brokenImagesList = brokenImagesPage.returnImages()
        brokenImageCount = 0
        for image in brokenImagesList:
            src = image.get_attribute("src")
            req = requests.get(src)
            if req.status_code != 200:
                brokenImageCount = brokenImageCount + 1
                log.error("The image link is not working " + src)
        assert brokenImageCount == 0