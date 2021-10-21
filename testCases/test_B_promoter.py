import random
import string
import time

import pytest

from pageObjects.Documents import Documents
from pageObjects.Entity import Entity
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
    baseURLDev = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_creating_newEntity(self, setup):
        self.logger.info("************* test_creating_newEntity **********")
        self.driver = setup
        self.driver.get(self.baseURLDev)
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
        # self.dp = Documents(self.driver)
        # self.dp.clickdocumentstab()
        # self.dp.clicklink()
        # time.sleep(5)
        self.pg.clickPromoterguarantorstab()
        time.sleep(5)
        self.pg.clickaddnewpromoter()
        time.sleep(5)
        self.pg.setpromotername("R B")
        time.sleep(3)
        self.pg.setpromoterfathername("A B")
        time.sleep(3)
        self.pg.setpromotermothername("K B")
        time.sleep(3)
        self.pg.clickMS()
        time.sleep(3)
        self.pg.selectMS()
        time.sleep(3)
        self.promoterDOB = generate_random_Date()
        self.pg.setDOB(self.promoterDOB)
        # self.pg.setDOB("7")
        time.sleep(3)
        self.pg.clickGender()
        time.sleep(3)
        self.pg.selectGender()
        time.sleep(3)
        self.promoterpan = random_generatorpan() + "P"
        self.pg.setPancard(self.promoterpan)
        # self.pg.setPancard("AACCS2650K")
        time.sleep(3)
        # self.pg.setAadhar("276794591146")
        self.promoteradhar = generate_random_adharnumber()
        self.pg.setAadhar(self.promoteradhar)
        time.sleep(3)
        # self.pg.setEmail("")
        # self.pg.setPhoneNumber("")
        self.promoteremail = random_generator() + "@gmail.com"
        self.pg.setEmail(self.promoteremail)
        time.sleep(3)
        self.promotermobile = generate_random_number()
        self.pg.setPhoneNumber(self.promotermobile)
        time.sleep(3)
        self.pg.clickJKAccess()
        self.pg.selectJKAccess()
        self.pg.clickISPrimaryPromoter()
        time.sleep(3)
        self.pg.selectISPrimaryPromoterNO()
        # time.sleep(3)
        # self.pg.clickPromoterStatus()
        # self.pg.selectPromoterStatus()
        self.pg.ClickSubmitPromoterStatus()
        time.sleep(5)
        self.driver.refresh()
        time.sleep(5)
        self.pg.clickPromoterguarantorstab()
        time.sleep(5)
        # @pytest.mark.regression
        # @pytest.mark.sanity
        # def test_Adding_PromoterAddress(self, setup):
        self.pg.clicklinkEditEntity()
        time.sleep(3)
        self.pg.clickEditAddress()
        time.sleep(3)
        self.pg.setpincode("560037")
        time.sleep(5)
        self.pg.setvillage("Challakere")
        time.sleep(3)
        self.pg.setlandmark("Junction")
        time.sleep(3)
        self.pg.setAdd1("1 block")
        time.sleep(3)
        self.pg.setAdd2("Near Temple")
        time.sleep(3)
        self.pg.clickAddressType()
        time.sleep(3)
        self.pg.selectAddressType()
        time.sleep(3)
        # self.pg.setYICA()
        self.promoterYearincurrentAddress = generate_random_yearnumber()
        self.pg.setYICA(self.promoterYearincurrentAddress)
        time.sleep(3)
        self.pg.clickupdate()
        time.sleep(3)
        self.driver.refresh()
        time.sleep(5)
        self.pg.clickPromoterguarantorstab()
        time.sleep(5)
        self.pg.clicklinkEditEntity()
        time.sleep(5)
        self.pg.clickcurr()
        time.sleep(3)
        self.pg.click()
        time.sleep(3)
        self.pg.update()
        time.sleep(3)
        self.driver.refresh()
        time.sleep(5)
        self.pg.clickPromoterguarantorstab()
        time.sleep(5)
        self.pg.clicklinkEditEntity()
        time.sleep(5)
        self.pg.uploadphoto("D://User/Rajeshwari/EntityOnboarding/TestData/Photoupload.png")
        self.pg.uploadsave()
        time.sleep(3)
        self.pg.uploadaadharfront("D://User/Rajeshwari/EntityOnboarding/TestData/Aadhaar_front-Test.jpg")
        self.pg.uploadsave()
        time.sleep(3)
        self.pg.uploadaadharback("D://User/Rajeshwari/EntityOnboarding/TestData/Aadhaar_back-Test.jpg")
        self.pg.uploadsave()
        time.sleep(3)
        self.pg.uploadaddressproof("D://User/Rajeshwari/EntityOnboarding/TestData/Address.pdf")
        self.pg.uploadsave()
        time.sleep(3)
        self.pg.uploadKYCDoc("D://User/Rajeshwari/EntityOnboarding/TestData/Address.pdf")
        self.pg.uploadsave()
        time.sleep(3)
        self.pg.uploadCACertifiedNetWorth("D://User/Rajeshwari/EntityOnboarding/TestData/Address.pdf")
        self.pg.uploadsave()
        time.sleep(3)
        self.pg.ClickAddBankDetails()
        time.sleep(3)
        self.pg.setAccNumber("1233211233")
        self.pg.setConfirmAccNumber("1233211233")
        time.sleep(3)
        self.pg.setAccHolderName("Testing One")
        self.driver.close()
