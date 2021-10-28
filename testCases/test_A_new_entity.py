import random
import string
import time

import pytest

from pageObjects.Entity import Entity
from pageObjects.LoginPage import LoginPage
from pageObjects.Promoters import Promoters
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))


def id_generator(size=15, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def generate_random_adharnumber(length=11):
    return int(''.join([str(random.randint(6, 9))]) + ''.join([str(random.randint(0, 9)) for _ in range(length)]))


def generate_random_yearnumber(length=0):
    return int(''.join([str(random.randint(1, 9))]) + ''.join([str(random.randint(0, 9)) for _ in range(length)]))


def random_generatorseActRegistration(size=9, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))


def generate_random_Date(length=0):
    return int(''.join([str(random.randint(1, 9))]) + ''.join([str(random.randint(1, 9)) for _ in range(length)]))


def generate_random_RegDate(length=0):
    return int(''.join([str(random.randint(1, 9))]) + ''.join([str(random.randint(6, 9)) for _ in range(length)]))


def generate_random_number(length=9):
    return int(''.join([str(random.randint(6, 9))]) + ''.join([str(random.randint(0, 9)) for _ in range(length)]))


class Test_Entity_creation:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_new_entity_login(self, setup):
        self.logger.info("************* Test_Entity_creation **********")
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
        self.logger.info("************ Create entity **************")
        self.ep = Entity(self.driver)
        self.ep.clickentity()
        time.sleep(5)
        self.ep.setspocname("rajeshwari BB")
        time.sleep(5)
        self.spocemail = random_generator() + "@gmail.com"
        self.ep.setspocemail(self.spocemail)
        self.spocmobile = generate_random_number()
        self.ep.setspocmobilenumber(self.spocmobile)
        # self.ep.setspocmobilenumber("9090909089")
        self.ep.clickspocdepartment()
        self.ep.selectspocdepartment()
        self.ep.clickIsPrimaryspoc()
        time.sleep(3)
        self.ep.selectIsPrimaryspoc()
        self.ep.submitspoc()
        time.sleep(5)
        # self.msg = self.driver.find_element_by_tag_name("body").text
        self.logger.info("************Created New Entity **************")
        time.sleep(10)
        self.logger.info("************Add Business details **************")
        self.ep.clickbusinessdetails()
        time.sleep(5)
        self.ep.clickfirmtype()
        self.ep.selectfirmtype()
        time.sleep(2)
        self.ep.clickEntitytype()
        time.sleep(2)
        self.ep.selectentitytype()
        time.sleep(5)
        self.ep.setgst("29AAACQ3943P1ZT")
        # self.gst = id_generator()
        # self.ep.setgst(self.gst)
        time.sleep(2)
        self.ep.clickokgst()
        time.sleep(5)
        self.ep.setpan("TVRPT2971P")
        time.sleep(2)
        self.ep.setcin("U32109KA2008PTC047065")
        time.sleep(2)
        self.udyogaadhar = generate_random_adharnumber()
        self.ep.setudyogadhar(self.udyogaadhar)
        time.sleep(2)
        self.ActRegistration = random_generatorseActRegistration()
        self.ep.setActRegistration(self.ActRegistration)
        time.sleep(2)
        self.ep.setfssaiLicense("1232343")
        time.sleep(2)
        self.ep.setLegalname("Automation")
        time.sleep(2)
        self.ep.submitbasicinfo()
        time.sleep(15)
        self.driver.refresh()
        time.sleep(5)
        self.ep.clickeditregadd()
        time.sleep(5)
        # self.ep.setpincode("560001")
        # time.sleep(2)
        # self.dateOfRegistartion = random_generatorseActRegistration()
        # self.ep.setdateOfRegistartion(self.dateOfRegistartion)
        # self.ep.setDistrict("Village")
        self.ep.setTaluk("Taluk")
        time.sleep(3)
        self.ep.setvillage("Chndigarh")
        time.sleep(3)
        self.ep.setlandmark("LAndmark")
        time.sleep(3)
        self.ep.clickaddresstype()
        self.ep.selectaddresstype()
        time.sleep(3)
        self.ep.submitregisteredadd()
        self.driver.refresh()
        time.sleep(5)
        self.ep.clickeditAgain()
        time.sleep(3)
        self.ep.setLegalBrandName("Rajeshwari")
        time.sleep(2)
        # self.mobileNumber = generate_random_number()
        # self.ep.setmobileNumber(self.mobileNumber)
        # time.sleep(5)
        # self.email = random_generator() + "@gmail.com"
        # self.ep.setemail(self.email)
        time.sleep(2)
        self.ep.setwebsite("www.jaikisan.com")
        time.sleep(2)
        self.deedDate = generate_random_RegDate()
        self.ep.setdeedDate(self.deedDate)
        time.sleep(2)
        self.ep.clickCompanyAct()
        time.sleep(2)
        self.ep.selectCompanyAct()
        time.sleep(2)
        self.ep.setdescription("GST number should be verified via available APIs and information received should be "
                               "pulled")
        time.sleep(5)
        self.ep.clicksubmitagain()
        self.driver.refresh()
        time.sleep(5)
        self.ep.clickeditbuttonadditionaldetails()
        time.sleep(5)
        self.ep.clickoperatingmode()
        time.sleep(2)
        self.ep.selectoperatingmode()
        time.sleep(2)
        self.ep.setavgbalance("90000")
        time.sleep(2)
        self.ep.setmontlyincome("900")
        time.sleep(2)
        self.ep.setannualincome("2000")
        time.sleep(2)
        self.ep.submitadditionalinfo()
        self.driver.refresh()
        time.sleep(10)
        # self.ep.submitregisteredadd()
        # self.ep.clickeditregadd()
        # time.sleep(10)
        # self.ep.setpincode("560037")
        # self.ep.clickpincodeok()
        # self.ep.setvillage("kodihalli")
        # self.ep.setlandmark("Junction")
        # self.ep.setstreetaddress1("Home")
        # self.ep.setstreetaddress2("next to home")
        # time.sleep(3)
        # self.ep.clickaddresstype()
        # time.sleep(3)
        # self.ep.selectaddresstype()
        # time.sleep(3)
        # self.ep.submitregisteredadd()
        # time.sleep(3)
        self.driver.refresh()
        time.sleep(3)
        self.ep.clickaddbankaccount()
        time.sleep(3)
        self.ep.setaccountnumber("123456789")
        time.sleep(3)
        self.ep.setconfirmaccountnumber("123456789")
        time.sleep(3)
        self.ep.setaccountholdername("Rajeshwari b")
        time.sleep(3)
        self.ep.setifsccode("CNRB0000504")
        time.sleep(10)
        self.ep.clickaccounttype()
        self.ep.selectaccounttypecurr()
        time.sleep(3)
        self.mobile = generate_random_number()
        self.ep.setmobilenumber(self.mobile)
        # self.ep.setmobilenumber("9080908080")
        time.sleep(3)
        self.ep.clickISPrimaryPromotor()
        self.ep.selectISParimaryPromotor()
        time.sleep(3)
        self.ep.clickStatus()
        self.ep.selectStatus()
        time.sleep(3)
        self.ep.clicksubmit()
        time.sleep(5)
        self.ep.clickuploadSatatement()
        self.ep.clickBankName()
        time.sleep(3)
        self.ep.selectBankName()
        time.sleep(3)
        self.ep.clickAccType()
        time.sleep(3)
        self.ep.selectAccTypeCurr()
        self.ep.clickDocType()
        time.sleep(3)
        self.ep.selectDocType()
        time.sleep(5)
        self.ep.uploadbankstmt("D://User/Rajeshwari/EntityOnboarding/TestData/Bank statement.pdf")
        time.sleep(100)
        self.driver.refresh()
        time.sleep(5)
        self.driver.close()

        # self.pp = Promoters(self.driver)
        # self.pp.clickPromoterguarantorstab()
        # self.pp.clickaddnewpromoter()
        # time.sleep(5)
        # self.pp.setpromotername("rajeshwari B")
        # self.pp.setpromoterfathername("A B")
        # self.driver.close()
