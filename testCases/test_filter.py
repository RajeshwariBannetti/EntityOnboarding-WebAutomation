import time
from pageObjects.LoginPage import LoginPage
from utilities import XLUtils
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig
from pageObjects.Filters import Filter


class Test_003_Filter:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def test_filter_login(self, setup):
        self.logger.info("************* Test_003_Filter **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        time.sleep(5)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        time.sleep(3)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(5)
        self.logger.info("************* Login successful **********")
        self.logger.info("******* Filter with firm type and date range **********")

        self.filter = Filter(self.driver)
        self.filter.clickOnFilterButton()
        self.filter.firm()
        self.filter.listfirm()
        self.filter.DateRangeIp()
        self.filter.DateRangeFrom("7/1/2021")
        self.filter.DateRangeTo("8/1/2021")
        time.sleep(5)
        self.filter.Savebutton()
        print()
        time.sleep(10)
        self.filter.Searchresult()
        row_count = self.filter.getNoOfRows()
        print(row_count)
        self.driver.close()

