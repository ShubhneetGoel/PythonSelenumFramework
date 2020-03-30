import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pageObjects.HomePage import HomePage
from testData.AbTestingData import ABTestingData
from testData.AddRemoveElements import AddRemoveElements
from utilities.BaseClass import BaseClass


class TestAddRemoveElements(BaseClass):

    def test_addRemoveElements(self,getData):
        log = self.get_logger()
        homePage = HomePage(self.driver)
        addRemoveElementsPage = homePage.returnAddRemoveElementsPage()

        for i in range(0,getData["AddElements"]):
            addRemoveElementsPage.returnAddElement()

        for i in range(0, getData["DelElements"]):
            addRemoveElementsPage.returnDeleteElement()

        assert addRemoveElementsPage.returnDeleteElementsSize() == 0

    @pytest.fixture(params=AddRemoveElements.AddRemoveElementsCount)
    def getData(self,request):
        return request.param