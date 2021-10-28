import pytest

from pageObjects.Documents import Documents
from pageObjects.LoginPage import LoginPage
from pageObjects.Promoters import Promoters
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from utilities import XLUtils
import time


class Test_documents:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    path = ".//TestData/Bank statement.pdf"
    logger = LogGen.loggen()

    @pytest.mark.regression
    @pytest.mark.sanity
    # @pytest.mark.skip
    def test_Doc_upload(self, setup):
        self.logger.info("************* test_Doc_upload **********")
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
        time.sleep(5)
        self.pg = Promoters(self.driver)
        self.pg.clickonanyentity()
        self.driver.refresh()
        time.sleep(5)
        self.dp = Documents(self.driver)
        self.dp.clickdocumentstab()
        time.sleep(5)
        self.dp.clickAddDoc()
        time.sleep(5)
        self.dp.uploadCertificateofIncorporation("D://User/Rajeshwari/EntityOnboarding/TestData/Aadhaar_front-Test.jpg")
        time.sleep(2)
        self.dp.docSave()
        time.sleep(3)
        self.dp.uploadgst1("D://User/Rajeshwari/EntityOnboarding/TestData/Aadhaar_front-Test.jpg")
        time.sleep(2)
        self.dp.docSave()
        time.sleep(3)
        self.dp.uploadCompanyPANCard("D://User/Rajeshwari/EntityOnboarding/TestData/Aadhaar_front-Test.jpg")
        time.sleep(2)
        self.dp.docSave()
        time.sleep(3)
        print(self.dp.MemorandumText())
        act_title = self.dp.MemorandumText()
        exp_title = "Memorandum of Association"
        if act_title == exp_title:
            self.logger.info("**** passed ****")
            self.dp.uploadMemorandum("D://User/Rajeshwari/EntityOnboarding/TestData/Aadhaar_front-Test.jpg")
            time.sleep(2)
            self.dp.docSave()
            time.sleep(3)
        else:
            self.logger.info("**** failed ****")
            self.dp.uploadGSTBill12months("D://User/Rajeshwari/EntityOnboarding/TestData/sample.pdf")
            time.sleep(2)
            self.dp.docSave()
            time.sleep(3)
        print(self.dp.ArticlesText())
        act_title = self.dp.ArticlesText()
        exp_title = "Articles of Association"
        if act_title == exp_title:
            self.logger.info("**** passed ****")
            self.dp.upoadArticles("D://User/Rajeshwari/EntityOnboarding/TestData/Aadhaar_front-Test.jpg")
            time.sleep(2)
            self.dp.docSave()
            time.sleep(3)
        else:
            self.logger.info("**** failed ****")
            self.dp.uploadAuditedFinancials3Years("D://User/Rajeshwari/EntityOnboarding/TestData/sample.pdf")
            time.sleep(2)
            self.dp.docSave()
            time.sleep(3)
        self.dp.uploadLenders("D://User/Rajeshwari/EntityOnboarding/TestData/sample.pdf")
        time.sleep(2)
        self.dp.docSave()
        time.sleep(3)
        self.dp.uploadAgreement("D://User/Rajeshwari/EntityOnboarding/TestData/sample.pdf")
        time.sleep(2)
        self.dp.docSave()
        time.sleep(3)
        self.dp.uploadUdyogAadhaar("D://User/Rajeshwari/EntityOnboarding/TestData/sample.pdf")
        time.sleep(2)
        self.dp.docSave()
        time.sleep(3)
        self.dp.uploadShopActLicense("D://User/Rajeshwari/EntityOnboarding/TestData/sample.pdf")
        time.sleep(2)
        self.dp.docSave()
        time.sleep(3)
        self.dp.uploadChannelLogo("D://User/Rajeshwari/EntityOnboarding/TestData/Aadhaar_front-Test.jpg")
        time.sleep(2)
        self.dp.docSave()
        time.sleep(3)
        self.dp.uploadAuditReport("D://User/Rajeshwari/EntityOnboarding/TestData/sample.pdf")
        time.sleep(2)
        self.dp.docSave()
        time.sleep(3)
        self.dp.uploadITRDocuments("D://User/Rajeshwari/EntityOnboarding/TestData/sample.pdf")
        time.sleep(2)
        self.dp.docSave()
        time.sleep(3)
        self.dp.uploadBoardResolutionDocument("D://User/Rajeshwari/EntityOnboarding/TestData/sample.pdf")
        time.sleep(2)
        self.dp.docSave()
        time.sleep(3)
        self.dp.uploadDealershipCertificate("D://User/Rajeshwari/EntityOnboarding/TestData/sample.pdf")
        time.sleep(2)
        self.dp.docSave()
        time.sleep(3)
        self.driver.refresh()
        time.sleep(5)
        self.driver.close()
