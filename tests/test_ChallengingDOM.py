import pytest

from pageObjects.HomePage import HomePage
from testData.ChallengingDOM import ChallengingDOM
from utilities.BaseClass import BaseClass


class TestChallengingDOM(BaseClass):

    def test_ChallengingDOM(self,getData):
        log = self.get_logger()
        homePage = HomePage(self.driver)
        ChallengingDOMPage = homePage.returnChallengingDOM()
        ChallengingDOMElements = ChallengingDOMPage.returnChallengingDOMElements(getData)
        found = 0
        for element in ChallengingDOMElements:
            if getData["var"] in element.text:
                found = 1
                break
        assert found == 1

    @pytest.fixture(params=ChallengingDOM.ChallengingDOMVars)
    def getData(self,request):
        return request.param