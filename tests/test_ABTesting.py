import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pageObjects.HomePage import HomePage
from testData.AbTestingData import ABTestingData
from utilities.BaseClass import BaseClass


class TestABTesting(BaseClass):

    def test_abTesting(self,getData):
        log = self.get_logger()
        homePage = HomePage(self.driver)
        abTestingPage = homePage.returnABTestingPage()
        log.info("Given h3 text is " + abTestingPage.returnh3text())
        self.driver.add_cookie(getData)
        self.driver.refresh()
        assert abTestingPage.returnh3text() == "No A/B Test"

    @pytest.fixture(params=ABTestingData.ABTestingData_Cookie)
    def getData(self,request):
        return request.param