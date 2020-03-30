import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pageObjects.HomePage import HomePage
from testData.AbTestingData import ABTestingData
from testData.AddRemoveElements import AddRemoveElements
from testData.BasicAuth import BasicAuth
from utilities.BaseClass import BaseClass


class TestBasicAuth(BaseClass):

    def test_basicAuth(self,getData):
        log = self.get_logger()
        homePage = HomePage(self.driver)
        basicAuthPage = homePage.returnBasicAuthPage(getData)
        assert "Congratulations!" in basicAuthPage.returnPText()

    @pytest.fixture(params=BasicAuth.BasicAuthCredentials)
    def getData(self,request):
        return request.param