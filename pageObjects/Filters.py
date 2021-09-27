import time

import self as self
from selenium.webdriver.support.ui import Select


class Filter:
    ButtonFilter_xpath = "//body/anchors-root[1]/anchors-anchors-container[1]/anchors-applications[1]/div[1]/div[" \
                         "2]/anchors-table[1]/div[1]/div[2]/div[3]/button[1]/span[1]"
    placeholder_FirmType_xpath = "//body/anchors-root[1]/anchors-anchors-container[1]/anchors-applications[1]/div[" \
                                 "1]/div[" \
                                 "2]/anchors-table[1]/div[1]/anchors-table-filters[1]/div[1]/div[2]/form[1]/div[" \
                                 "1]/div[1]/div[" \
                                 "1]/div[1]/mat-form-field[1]/div[1]/div[1]/div[3]/mat-select[1]/div[1]/div[1]/span[1] "
    lstFirmType_PublicLimitedCompany_xpath = "//span[contains(text(),'Public Limited Company')]"
    lstFirmType_PrivateLimitedCompany_xpath = "//span[contains(text(),'Private Limited Company')]"
    lstFirmType_Partnership_xpath = "//body/div[2]/div[2]/div[1]/div[1]/div[1]/mat-option[3]/span[1]"
    lstFirmType_LimitedLiabilityPartnership_xpath = "//span[contains(text(),'Limited Liability Partnership')]"
    lstFirmType_Proprietorship_xpath = "//span[contains(text(),'Proprietorship')]"
    lstFirmType_OnePersonCompany_xpath = "//span[contains(text(),'One Person Company')]"
    lstFirmType_Section8Company_xpath = "//span[contains(text(),'Section 8 Company')]"
    lstFirmType_LimitedLiabilityCompany_xpath = "//span[contains(text(),'Limited Liability Company')]"
    lstFirmType_Trust_xpath = "//span[contains(text(),'Trust')]"
    lstFirmType_CoOperativeSociety_xpath = "//span[contains(text(),'Co-Operative Society')]"
    Date_Table_xpath = "//body/anchors-root[1]/anchors-anchors-container[1]/anchors-applications[1]/div[1]/div[" \
                       "2]/anchors-table[1]/div[1]/anchors-table-filters[1]/div[1]/div[2]/form[1]/div[2]/div[1]/div[" \
                       "1]/div[1]/mat-form-field[1]/div[1]/div[1]/div[3]/mat-date-range-input[1] "
    DateRangeFrom_xpath = "//input[@id='mat-date-range-input-0']"
    DateRangeTo_xpath = "//body/anchors-root[1]/anchors-anchors-container[1]/anchors-applications[1]/div[1]/div[" \
                        "2]/anchors-table[1]/div[1]/anchors-table-filters[1]/div[1]/div[2]/form[1]/div[2]/div[1]/div[" \
                        "1]/div[1]/mat-form-field[1]/div[1]/div[1]/div[3]/mat-date-range-input[1]/div[1]/div[" \
                        "2]/input[1] "
    btnSave_xpath = "//span[contains(text(),'Save')]"
    tableSearchResult = "//body/anchors-root[1]/anchors-anchors-container[1]/anchors-applications[1]/div[1]/div[" \
                        "2]/anchors-table[1]/div[1]/div[3]/anchors-table-card[1]/mat-card[1] "
    tableRows_xpath = "//table[@id = 'cdk-drop-list-0']//tbody/tr"
    tableColumn_xpath = "//table[@id = 'cdk-drop-list-0']//tbody/tr/td"

    def __init__(self, driver):
        self.driver = driver

    def clickOnFilterButton(self):
        self.driver.find_element_by_xpath(self.ButtonFilter_xpath).click()

    def firm(self):
        self.driver.find_element_by_xpath(self.placeholder_FirmType_xpath).click()

    def listfirm(self):
        self.driver.find_element_by_xpath(self.lstFirmType_PublicLimitedCompany_xpath).click()

    # def listfirm(self):
    #     self.driver.find_element_by_xpath(self.lstFirmType_LimitedLiabilityCompany_xpath).click()

    # def setFirmType(self):
    #     self.driver.find_element_by_xpath(self.placeholder_FirmType_xpath).click()
    #     time.sleep(3)

    # def firmType(self):
    #     self.driver.find_element_by_xpath(self.lstFirmType_PublicLimitedCompany_xpath).click()
    #     time.sleep(3)
    # if firmtype == 'Public Limited Company':
    #     self.listFirmType = self.driver.find_element_by_xpath(self.lstFirmType_PublicLimitedCompany_xpath)

    # elif firmtype == 'Private Limited Company':
    #     self.listFirmType = self.driver.find_element_by_xpath(self.lstFirmType_PrivateLimitedCompany_xpath)
    #
    # elif firmtype == 'Partnership':
    #     self.listFirmType = self.driver.find_element_by_xpath(self.lstFirmType_Partnership_xpath)
    #
    # elif firmtype == 'Limited Liability Partnership':
    #     self.listFirmType = self.driver.find_element_by_xpath(self.lstFirmType_LimitedLiabilityPartnership_xpath)
    #
    # elif firmtype == 'Proprietorship':
    #     self.listFirmType = self.driver.find_element_by_xpath(self.lstFirmType_Proprietorship_xpath)
    #
    # elif firmtype == 'One Person Company':
    #     self.listFirmType = self.driver.find_element_by_xpath(self.lstFirmType_OnePersonCompany_xpath)
    #
    # elif firmtype == 'Section 8 Company':
    #     self.listFirmType = self.driver.find_element_by_xpath(self.lstFirmType_Section8Company_xpath)
    #
    # elif firmtype == 'Limited Liability Company':
    #     self.listFirmType = self.driver.find_element_by_xpath(self.lstFirmType_LimitedLiabilityCompany_xpath)
    #
    # elif firmtype == 'Trust':
    #     self.listFirmType = self.driver.find_element_by_xpath(self.lstFirmType_Trust_xpath)
    #
    # elif firmtype == 'Co-Operative Society':
    #     self.listFirmType = self.driver.find_element_by_xpath(self.lstFirmType_CoOperativeSociety_xpath)
    #
    # else:
    #     self.listFirmType = self.driver.find_element_by_xpath(self.lstFirmType_PublicLimitedCompany_xpath)
    #     time.sleep(3)
    #
    #     # self.listFirmType.click()
    #
    #     self.driver.execute_script("arguments[0].click();", self.firmtype)

    def DateRangeIp(self):
        self.driver.find_element_by_xpath(self.Date_Table_xpath).click()

    def DateRangeFrom(self, fromDate):
        self.driver.find_element_by_xpath(self.DateRangeFrom_xpath).send_keys(fromDate)

    def DateRangeTo(self, toDate):
        self.driver.find_element_by_xpath(self.DateRangeTo_xpath).send_keys(toDate)

    def Savebutton(self):
        self.driver.find_element_by_xpath(self.btnSave_xpath).click()

    def Searchresult(self):
        self.driver.find_element_by_xpath(self.tableSearchResult).click()

    def getNoOfRows(self):
        row_count = len(self.driver.find_element_by_xpath(self.tableRows_xpath))

    def getNoOfCloumns(self):
        return len(self.driver.find_element_by_xpath(self.tableColumn_xpath))
