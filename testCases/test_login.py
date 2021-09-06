import pytest
from selenium import webdriver
from PageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_001_Login:

    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    def test_homePageTitle(self, setup):
        self.logger.info("******Test_001******")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.logger.info("******Verifying Home Page Title******")
        act_title = self.driver.title
        self.driver.close()
        #For printing title of the page
        if act_title == "Log in to Jai Kisan":
            assert True
            self.logger.info("******HomePage title test is passed******")
        else:
            assert False

    def test_login(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        self.driver.close()

