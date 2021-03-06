import random
import string
import time

import pytest

from pageObjects.LoginPage import LoginPage
from pageObjects.Promoters import Promoters
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))


def random_generatorpan(size=9, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))


def generate_random_adharnumber(length=11):
    return int(''.join([str(random.randint(6, 9))]) + ''.join([str(random.randint(0, 9)) for _ in range(length)]))


def generate_random_number(length=9):
    return int(''.join([str(random.randint(6, 9))]) + ''.join([str(random.randint(0, 9)) for _ in range(length)]))


def generate_random_yearnumber(length=0):
    return int(''.join([str(random.randint(1, 9))]) + ''.join([str(random.randint(0, 9)) for _ in range(length)]))


def generate_random_Date(length=0):
    return int(''.join([str(random.randint(1, 9))]) + ''.join([str(random.randint(1, 9)) for _ in range(length)]))


class Test_promoter:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_creating_newEntity(self, setup):
        self.logger.info("************* test_Creating_NewPromoter **********")
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
        self.pp = Promoters(self.driver)
        self.pp.clickonanyentity()
        self.driver.refresh()
        time.sleep(5)
        self.pp.clickPromoterguarantorstab()
        self.logger.info("*************Adding New Promoter Information **********")
        time.sleep(5)
        self.pp.clickaddnewpromoter()
        time.sleep(5)
        self.pp.setpromotername("Test B")
        time.sleep(3)
        self.pp.setpromoterfathername("A B")
        time.sleep(3)
        self.pp.setpromotermothername("K B")
        time.sleep(3)
        self.pp.clickMS()
        time.sleep(3)
        self.pp.selectMS()
        time.sleep(3)
        self.promoterDOB = generate_random_Date()
        self.pp.setDOB(self.promoterDOB)
        # self.pp.setDOB("7")
        time.sleep(3)
        self.pp.clickGender()
        time.sleep(3)
        self.pp.selectGender()
        time.sleep(3)
        self.promoterpan = random_generatorpan() + "P"
        self.pp.setPancard(self.promoterpan)
        # self.pp.setPancard("AACCS2650K")
        time.sleep(3)
        # self.pp.setAadhar("276794591146")
        self.promoteradhar = generate_random_adharnumber()
        self.pp.setAadhar(self.promoteradhar)
        time.sleep(3)
        # self.pp.setEmail("")
        # self.pp.setPhoneNumber("")
        self.promoteremail = random_generator() + "@gmail.com"
        self.pp.setEmail(self.promoteremail)
        time.sleep(3)
        self.promotermobile = generate_random_number()
        self.pp.setPhoneNumber(self.promotermobile)
        time.sleep(3)
        self.pp.clickJKAccess()
        self.pp.selectJKAccess()
        self.pp.clickISPrimaryPromoter()
        time.sleep(3)
        self.pp.selectISPrimaryPromoterYES()
        time.sleep(3)
        self.pp.clickPromoterStatus()
        self.pp.selectPromoterStatusActive()
        time.sleep(2)
        self.pp.ClickSubmitPromoterStatus()
        # time.sleep(2)
        # print(self.pp.textISPrimaryPromoter())
        # act_title = self.pp.textISPrimaryPromoter()
        # exp_title = "Only a Single Promoter can be marked as Primary."
        # if act_title == exp_title:
        #     self.logger.info("**** passed ****")
        #     self.pp.clickISPrimaryPromoter()
        #     time.sleep(2)
        #     self.pp.selectISPrimaryPromoterNO()
        #     time.sleep(2)
        # else:
        #     self.logger.info("**** failed ****")
        #     self.pp.clickISPrimaryPromoter()
        #     time.sleep(2)
        #     self.pp.selectISPrimaryPromoterYES()
        #     time.sleep(3)
        # self.pp.ClickSubmitPromoterStatus()
        self.logger.info("************* Promoter Information added successful **********")
        # time.sleep(5)
        # self.driver.refresh()
        # time.sleep(5)
        # self.pp.clickPromoterguarantorstab()
        # time.sleep(5)
        # self.pp.clicklinkEditEntity()
        time.sleep(10)
        self.logger.info("*************Adding New Promoter Permanent Address **********")
        self.pp.clickEditAddress()
        time.sleep(3)
        self.pp.setpincode("560037")
        time.sleep(5)
        self.pp.setvillage("Challakere")
        time.sleep(3)
        self.pp.setlandmark("Junction")
        time.sleep(3)
        self.pp.setAdd1("1 block")
        time.sleep(3)
        self.pp.setAdd2("Near Temple")
        time.sleep(3)
        self.pp.clickAddressType()
        time.sleep(3)
        self.pp.selectAddressType()
        time.sleep(3)
        # self.pp.setYICA()
        self.promoterYearincurrentAddress = generate_random_yearnumber()
        self.pp.setYICA(self.promoterYearincurrentAddress)
        time.sleep(3)
        self.pp.clickupdate()
        time.sleep(3)
        self.logger.info("************* Permanent Address added successful **********")
        # self.driver.refresh()
        # time.sleep(5)
        # self.pp.clickPromoterguarantorstab()
        # time.sleep(5)
        # self.pp.clicklinkEditEntity()
        time.sleep(5)
        self.logger.info("*************Adding New Promoter Current Address **********")
        self.pp.clickcurr()
        time.sleep(3)
        self.pp.click()
        time.sleep(3)
        self.pp.update()
        time.sleep(3)
        self.logger.info("************* Current Address added successful **********")
        # self.driver.refresh()
        # time.sleep(5)
        # self.pp.clickPromoterguarantorstab()
        # time.sleep(5)
        # self.pp.clicklinkEditEntity()
        time.sleep(3)
        self.logger.info("*************Uploading New Promoter Documents **********")
        time.sleep(5)
        self.pp.uploadphoto("D://User/Rajeshwari/EntityOnboarding/TestData/Photoupload.png")
        time.sleep(5)
        self.pp.uploadsave()
        time.sleep(3)
        self.pp.uploadaadharfront("D://User/Rajeshwari/EntityOnboarding/TestData/Aadhaar_front-Test.jpg")
        time.sleep(5)
        self.pp.uploadsave()
        time.sleep(3)
        self.pp.uploadaadharback("D://User/Rajeshwari/EntityOnboarding/TestData/Aadhaar_back-Test.jpg")
        time.sleep(5)
        self.pp.uploadsave()
        time.sleep(3)
        self.pp.uploadaddressproof("D://User/Rajeshwari/EntityOnboarding/TestData/Address.pdf")
        time.sleep(5)
        self.pp.uploadsave()
        time.sleep(3)
        self.pp.uploadKYCDoc("D://User/Rajeshwari/EntityOnboarding/TestData/Address.pdf")
        time.sleep(5)
        self.pp.uploadsave()
        time.sleep(3)
        self.pp.uploadCACertifiedNetWorth("D://User/Rajeshwari/EntityOnboarding/TestData/Address.pdf")
        time.sleep(5)
        self.pp.uploadsave()
        time.sleep(3)
        self.logger.info("************* Documents uploaded successful **********")
        time.sleep(3)
        self.driver.refresh()
        time.sleep(5)
        self.pp.clickPromoterguarantorstab()
        time.sleep(5)
        self.pp.clicklinkEditEntity()
        time.sleep(3)
        self.logger.info("*************Adding New Promoter Bank Details **********")
        self.pp.ClickAddBankDetails()
        time.sleep(3)
        self.pp.setAccNumber("1233211233")
        self.pp.setConfirmAccNumber("1233211233")
        time.sleep(3)
        self.pp.setAccHolderName("Testing One")
        time.sleep(3)
        self.pp.setIFSC("CNRB0004208")
        time.sleep(3)
        self.pp.clickAccType()
        self.pp.selectAccTypeCurr()
        self.promoterBankMobile = generate_random_number()
        self.pp.SetMobileNumber(self.promoterBankMobile)
        time.sleep(3)
        self.pp.clickISPrimayAcc()
        self.pp.selectISPrimaryAccYes()
        time.sleep(3)
        self.pp.clickISPrimaryAccStatus()
        self.pp.selectISPrimaryAccStatusActive()
        self.logger.info("************* Bank Details added successful **********")
        time.sleep(3)
        self.driver.close()
