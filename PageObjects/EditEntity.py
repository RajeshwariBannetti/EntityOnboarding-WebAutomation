import time

import self as self
from selenium.webdriver.support.ui import Select


class EditEntity:
    Toggle_xpath = "//body/div[2]/div[2]/div[1]/mat-dialog-container[1]/anchors-new-application[1]/section[1]/div[" \
                   "1]/mat-slide-toggle[1]/label[1]/div[1] "
    lnkNewEntity_xpath = "//span[contains(text(),'New Entity Onboarding')]"
    Promoter_name_id = "mat-input-4"
    Promoter_Father_name_id = "mat-input-5"
    Promoter_Mother_name_id = "mat-input-6"
    lstPromoter_Marital_Status_id = "mat-select-8"
    Promoter_DOB_xpath = "//input[@id='mat-input-20']"
    lstPromoter_Gender_xpath = "//body/div[2]/div[2]/div[1]/mat-dialog-container[1]/anchors-new-application[1]/section[" \
                               "1]/div[2]/div[1]/anchors-forms[1]/anchors-form-builder[1]/div[1]/form[" \
                               "1]/jkf-element-builder[7]/anchors-wrapper-element[1]/anchors-select-input[1]/div[" \
                               "1]/mat-form-field[1]/div[1]/div[1]/div[3]/mat-select[1]/div[1]/div[1]/span[1] "
    Promoter_PAN_DL_VoterID_id = "mat-input-21"
    Promoter_AadharNumber_id = "mat-input-22"
    Promoter_Email_id = "mat-input-23"
    Promoter_MobileNumber_id = "mat-input-24"
    lstIs_Primary_Promoter_xpath = "//body/div[2]/div[2]/div[1]/mat-dialog-container[1]/anchors-new-application[" \
                                   "1]/section[" \
                                   "1]/div[2]/div[1]/anchors-forms[1]/anchors-form-builder[1]/div[1]/form[" \
                                   "1]/jkf-element-builder[12]/anchors-wrapper-element[1]/anchors-select-input[1]/div[" \
                                   "1]/mat-form-field[1]/div[1]/div[1]/div[3]/mat-select[1]/div[1]/div[1]/span[1] "
    Submit_button_xpath = "//body/div[2]/div[2]/div[1]/mat-dialog-container[1]/anchors-new-application[1]/section[" \
                          "1]/div[2]/div[1]/anchors-forms[1]/anchors-form-builder[1]/div[1]/div[1]/button[1] "

    def __init__(self, driver):
        self.driver = driver

    def setUserName(self, username):
        self.driver.find_element_by_id(self.textbox_username_id).clear()
        self.driver.find_element_by_id(self.textbox_username_id).send_keys(username)

