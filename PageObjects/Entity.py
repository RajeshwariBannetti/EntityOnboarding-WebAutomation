import select

from selenium import webdriver


class Entity:
    lnkNewEntity_xpath = "//span[contains(text(),'New Entity Onboarding')]"
    textbox_spocname_xpath = "//input[@id='en-sec-new-spoc-fullName']"
    textbox_spocemail_xpath = "//input[@id='en-sec-new-spoc-email']"
    textbox_spocemobile_xpath = "//input[@id='en-sec-new-spoc-mobileNumber']"
    dropdownlist_department_xpath = "/html[1]/body[1]/div[2]/div[2]/div[1]/mat-dialog-container[" \
                                    "1]/anchors-new-application[1]/section[1]/div[2]/div[1]/anchors-forms[" \
                                    "1]/anchors-form-builder[1]/div[1]/form[1]/jkf-element-builder[" \
                                    "4]/anchors-wrapper-element[1]/anchors-select-input[1]/div[1]/mat-form-field[" \
                                    "1]/div[1]/div[1]/div[3]/mat-select[1]/div[1]/div[1]/span[1] "
    list_depStrategicSales_xpath = "/html[1]/body[1]/div[2]/div[4]/div[1]/div[1]/div[1]/mat-option[1]/span[1]"
    list_depSalesWest_xpath = "/html[1]/body[1]/div[2]/div[4]/div[1]/div[1]/div[1]/mat-option[2]/span[1]"
    list_depSalesSouth_xpath = "/html[1]/body[1]/div[2]/div[4]/div[1]/div[1]/div[1]/mat-option[3]/span[1]"
    list_depSalesCentral_xpath = "/html[1]/body[1]/div[2]/div[4]/div[1]/div[1]/div[1]/mat-option[4]/span[1]"
    list_depCOPS_xpath = "/html[1]/body[1]/div[2]/div[4]/div[1]/div[1]/div[1]/mat-option[5]/span[1]"
    dropdownlist_IsPrimaryspoc_xpath = "/html[1]/body[1]/div[2]/div[2]/div[1]/mat-dialog-container[" \
                                       "1]/anchors-new-application[1]/section[1]/div[2]/div[1]/anchors-forms[" \
                                       "1]/anchors-form-builder[1]/div[1]/form[1]/jkf-element-builder[" \
                                       "5]/anchors-wrapper-element[1]/anchors-select-input[1]/div[1]/mat-form-field[" \
                                       "1]/div[1]/div[1]/div[3]/mat-select[1]/div[1]/div[1]/span[1] "
    list_IsPrimaryspocYes_xpath = "/html[1]/body[1]/div[2]/div[4]/div[1]/div[1]/div[1]/mat-option[1]/span[1]"
    list_IsPrimaryspocNo_xpath = "/html[1]/body[1]/div[2]/div[4]/div[1]/div[1]/div[1]/mat-option[2]/span[1]"
    button_submit_xpath = "/html[1]/body[1]/div[2]/div[2]/div[1]/mat-dialog-container[1]/anchors-new-application[" \
                          "1]/section[1]/div[2]/div[1]/anchors-forms[1]/anchors-form-builder[1]/div[1]/div[1]/button[" \
                          "1]/span[1] "
    button_businessdetailsedit_xpath = "/html[1]/body[1]/anchors-root[1]/anchors-anchors-container[" \
                                       "1]/anchors-application-details[1]/div[1]/div[3]/div[1]/mat-tab-group[1]/div[" \
                                       "1]/mat-tab-body[1]/div[1]/div[1]/anchors-section-renderer[1]/div[" \
                                       "1]/anchors-content-decider[1]/anchors-forms[1]/anchors-form-builder[1]/div[" \
                                       "1]/div[1]/button[1] "
    dropdownlist_firmtype_xpath = "//mat-tab-body/div[1]/div[1]/anchors-section-renderer[1]/div[" \
                                  "1]/anchors-content-decider[" \
                                  "1]/anchors-forms[1]/anchors-form-builder[1]/div[1]/form[1]/jkf-element-builder[" \
                                  "1]/anchors-wrapper-element[1]/anchors-select-input[1]/div[1]/mat-form-field[" \
                                  "1]/div[1]/div[" \
                                  "1]/div[3] "
    list_firmtype_xpath = "/html[1]/body[1]/div[2]/div[2]/div[1]/div[1]/div[1]/mat-option[1]/span[1]"
    dropdownlist_Entitytype_xpath = "/html[1]/body[1]/anchors-root[1]/anchors-anchors-container[" \
                                    "1]/anchors-application-details[1]/div[1]/div[3]/div[1]/mat-tab-group[1]/div[" \
                                    "1]/mat-tab-body[1]/div[1]/div[1]/anchors-section-renderer[1]/div[" \
                                    "1]/anchors-content-decider[1]/anchors-forms[1]/anchors-form-builder[1]/div[" \
                                    "1]/form[1]/jkf-element-builder[2]/anchors-wrapper-element[" \
                                    "1]/anchors-select-input[1]/div[1]/mat-form-field[1]/div[1]/div[1]/div[" \
                                    "3]/mat-select[1]/div[1]/div[1]/span[1] "
    list_Entitytype_xpath = "/html[1]/body[1]/div[2]/div[2]/div[1]/div[1]/div[1]/mat-option[8]/span[1]"
    textbox_gst_xpath = "//input[@id='en-sec-firm-isGst-gstNumber']"
    button_gstok_xapth = "//span[contains(text(),'OK')]"
    textbox_pan_xpath = "//input[@id='en-sec-firm-isGst-pan']"
    textbox_CIN_xpath = "//input[@id='en-sec-firm-isGst-cin']"
    textbox_EntityLegalName_xpath = "//input[@id='en-sec-firm-isGst-channelLegalName']"
    textbox_udyogadhar_xpath = "//input[@id='en-sec-firm-isGst-udyogAadhaar']"
    textbox_seActRegistration_xpath = "//input[@id='en-sec-firm-isGst-seActRegistration']"
    textbox_fssaiLicense_xpath = "//input[@id='en-sec-firm-isGst-fssaiLicense']"
    textbox_setLegalBrandName_xpath = "//input[@id='en-sec-firm-isGst-channelBrandName']"
    button_submitbasicinfo_xpath = "//span[contains(text(),'Submit')]"
    button_editAgain_xpath = "/html[1]/body[1]/anchors-root[1]/anchors-anchors-container[" \
                             "1]/anchors-application-details[1]/div[1]/div[3]/div[1]/mat-tab-group[1]/div[" \
                             "1]/mat-tab-body[1]/div[1]/div[1]/anchors-section-renderer[1]/div[" \
                             "1]/anchors-content-decider[1]/anchors-forms[1]/anchors-form-builder[1]/div[1]/div[" \
                             "1]/button[1]/span[1] "
    textbox_dateOfRegistartion_xpath = "//input[@id='en-sec-firm-isGst-dateOfRegistartion']"
    textbox_mobileNumber_xpath = "//input[@id='en-sec-firm-isGst-mobileNumber']"
    textbox_email_xpath = "//input[@id='en-sec-firm-isGst-email']"
    textbox_website_xpath = "//input[@id='en-sec-firm-isGst-website']"
    textbox_deedDate_xpath = "//input[@id='en-sec-firm-isGst-deedDate']"
    dropdownlist_CompanyAct_xpath = "/html[1]/body[1]/anchors-root[1]/anchors-anchors-container[" \
                                    "1]/anchors-application-details[1]/div[1]/div[3]/div[1]/mat-tab-group[1]/div[" \
                                    "1]/mat-tab-body[1]/div[1]/div[1]/anchors-section-renderer[1]/div[" \
                                    "1]/anchors-content-decider[1]/anchors-forms[1]/anchors-form-builder[1]/div[" \
                                    "1]/form[1]/jkf-element-builder[16]/anchors-wrapper-element[" \
                                    "1]/anchors-select-input[1]/div[1]/mat-form-field[1]/div[1]/div[1]/div[" \
                                    "3]/mat-select[1]/div[1]/div[1]/span[1] "
    list_CompanyAct_xpath = "/html[1]/body[1]/div[2]/div[2]/div[1]/div[1]/div[1]/mat-option[1]/span[1]"
    textbox_description_xpath = "//textarea[@id='en-sec-firm-isGst-description']"
    button_submitagain_xpath = "/html[1]/body[1]/anchors-root[1]/anchors-anchors-container[" \
                               "1]/anchors-application-details[1]/div[1]/div[3]/div[1]/mat-tab-group[1]/div[" \
                               "1]/mat-tab-body[1]/div[1]/div[1]/anchors-section-renderer[1]/div[" \
                               "1]/anchors-content-decider[1]/anchors-forms[1]/anchors-form-builder[1]/div[1]/div[" \
                               "1]/button[1]/span[1] "
    # Additional details =ad
    button_additionaldetails_xpath = "//html[1]/body[1]/anchors-root[1]/anchors-anchors-container[" \
                                     "1]/anchors-application-details[1]/div[1]/div[3]/div[1]/mat-tab-group[1]/div[" \
                                     "1]/mat-tab-body[1]/div[1]/div[1]/anchors-section-renderer[1]/div[" \
                                     "1]/anchors-content-decider[2]/anchors-forms[1]/anchors-form-builder[1]/div[" \
                                     "1]/div[1]/button[1]/span[1] "
    dropdownlist_Operatingmode_xpath = "/html[1]/body[1]/anchors-root[1]/anchors-anchors-container[" \
                                       "1]/anchors-application-details[1]/div[1]/div[3]/div[1]/mat-tab-group[1]/div[" \
                                       "1]/mat-tab-body[1]/div[1]/div[1]/anchors-section-renderer[1]/div[" \
                                       "1]/anchors-content-decider[2]/anchors-forms[1]/anchors-form-builder[1]/div[" \
                                       "1]/form[1]/jkf-element-builder[1]/anchors-wrapper-element[" \
                                       "1]/anchors-select-input[1]/div[1]/mat-form-field[1]/div[1]/div[1]/div[" \
                                       "3]/mat-select[1]/div[1]/div[1]/span[1] "
    list_operatingmode_xpath = "/html[1]/body[1]/div[2]/div[2]/div[1]/div[1]/div[1]/mat-option[2]/span[1]"
    textbox_averagebankbalance_xpath = "//input[@id='en-sec-company-addtional-details-averageBankBalance']"
    textbox_montlyincome_xpath = "//input[@id='en-sec-company-addtional-details-monthlyIncome']"
    textbox_annualincome_xpath = "//input[@id='en-sec-company-addtional-details-annualIncome']"
    button_submitadditianlinfo_xpath = "/html[1]/body[1]/anchors-root[1]/anchors-anchors-container[" \
                                       "1]/anchors-application-details[1]/div[1]/div[3]/div[1]/mat-tab-group[1]/div[" \
                                       "1]/mat-tab-body[1]/div[1]/div[1]/anchors-section-renderer[1]/div[" \
                                       "1]/anchors-content-decider[2]/anchors-forms[1]/anchors-form-builder[1]/div[" \
                                       "1]/div[1]/button[1] "

    # Registered Address(Skip Address data fetches from gst number)
    button_edit_registeredaddress_xpath = "//mat-tab-body/div[1]/div[1]/anchors-section-renderer[1]/div[" \
                                          "1]/anchors-content-decider[3]/anchors-forms[1]/anchors-form-builder[" \
                                          "1]/div[1]/div[1]/button[1]/span[1] "
    textbox_pincode_xpath = "/html[1]/body[1]/anchors-root[1]/anchors-anchors-container[" \
                            "1]/anchors-application-details[1]/div[1]/div[3]/div[1]/mat-tab-group[1]/div[" \
                            "1]/mat-tab-body[1]/div[1]/div[1]/anchors-section-renderer[1]/div[" \
                            "1]/anchors-content-decider[3]/anchors-forms[1]/anchors-form-builder[1]/div[1]/form[" \
                            "1]/jkf-element-builder[1]/anchors-wrapper-element[1]/anchors-number-input[1]/div[" \
                            "1]/mat-form-field[1]/div[1]/div[1]/div[4]/input[1] "
    button_pincode_xpath = "//span[contains(text(),'OK')]"
    textbox_EnterState_xpath = "//input[@id='mat-input-15']"
    textbox_EnterDistrict_xpath = "//input[@id='en-sec-company-address-district']"
    textbox_EnterTaluk_xpath = "//input[@id='en-sec-company-address-taluka']"
    textbox_village_xpath = "//input[@id='en-sec-company-address-village']"
    textbox_Landmark_xpath = "//input[@id='en-sec-company-address-landmark']"
    textbox_streetaddress1_id = "mat-input-7"
    textbox_streetaddress2_id = "mat-input-8"
    dropdownlist_Addresstype_xpath = "/html[1]/body[1]/anchors-root[1]/anchors-anchors-container[" \
                                     "1]/anchors-application-details[1]/div[1]/div[3]/div[1]/mat-tab-group[1]/div[" \
                                     "1]/mat-tab-body[1]/div[1]/div[1]/anchors-section-renderer[1]/div[" \
                                     "1]/anchors-content-decider[3]/anchors-forms[1]/anchors-form-builder[1]/div[" \
                                     "1]/form[1]/jkf-element-builder[9]/anchors-wrapper-element[" \
                                     "1]/anchors-select-input[1]/div[1]/mat-form-field[1]/div[1]/div[1]/div[" \
                                     "3]/mat-select[1]/div[1]/div[1]/span[1] "
    list_addresstype_owned_xpath = "/html[1]/body[1]/div[2]/div[2]/div[1]/div[1]/div[1]/mat-option[1]/span[1]"
    list_addresstype_rented_xpath = "//span[contains(text(),'Rented')]"
    # textbox_latitude_xpath = "//input[@id='mat-input-22']"
    # textbox_longitude_xpath = "//input[@id='mat-input-23']"
    button_submitregisteredadd_xpath = "/html[1]/body[1]/anchors-root[1]/anchors-anchors-container[" \
                                       "1]/anchors-application-details[1]/div[1]/div[3]/div[1]/mat-tab-group[1]/div[" \
                                       "1]/mat-tab-body[1]/div[1]/div[1]/anchors-section-renderer[1]/div[" \
                                       "1]/anchors-content-decider[3]/anchors-forms[1]/anchors-form-builder[1]/div[" \
                                       "1]/div[1]/button[1] "

    #  Add Bank Account
    button_AddBankAccount_xpath = "/html[1]/body[1]/anchors-root[1]/anchors-anchors-container[" \
                                  "1]/anchors-application-details[1]/div[1]/div[3]/div[1]/mat-tab-group[1]/div[" \
                                  "1]/mat-tab-body[1]/div[1]/div[1]/anchors-section-renderer[1]/div[" \
                                  "1]/anchors-content-decider[4]/anchors-member-details[1]/div[1]/anchors-table[" \
                                  "1]/div[1]/div[2]/div[2]/button[2]/span[1] "
    # Account information
    textbox_accountnumber_xpath = "//input[@id='en-sec-account-information-accNumber']"
    textbox_confirmaccountnumber_xpath = "//input[@id='en-sec-account-information-accNumberC']"
    textbox_accountholdername_xpath = "//input[@id='en-sec-account-information-accountHolderName']"
    textbox_IFSCcode_xpath = "//input[@id='en-sec-account-information-ifsc']"
    # textbox_EnterMICRCODE_xpath = "//input[@id='mat-input-28']"
    # textbox_bankname_xpath = "//input[@id='mat-input-29']"
    # textbox_bankaddress_xpath = "//input[@id='mat-input-30']"
    dropdownlist_accounttype_xpath = "/html[1]/body[1]/div[2]/div[2]/div[1]/mat-dialog-container[1]/anchors-member[" \
                                     "1]/section[1]/anchors-member-section[1]/anchors-forms[1]/anchors-form-builder[" \
                                     "1]/div[1]/form[1]/jkf-element-builder[8]/anchors-wrapper-element[" \
                                     "1]/anchors-select-input[1]/div[1]/mat-form-field[1]/div[1]/div[1]/div[" \
                                     "3]/mat-select[1]/div[1]/div[1]/span[1] "
    list_accounttype_Current_xpath = "/html[1]/body[1]/div[2]/div[4]/div[1]/div[1]/div[1]/mat-option[1]/span[1]"
    list_accounttype_Saving_xpath = "/html[1]/body[1]/div[2]/div[4]/div[1]/div[1]/div[1]/mat-option[2]/span[1]   "
    textbox_mobilenumber_xpath = "//input[@id='en-sec-account-information-mobileNumber']"
    dropdownlist_IsPrimary_Promoter_xpath = "/html[1]/body[1]/div[2]/div[2]/div[1]/mat-dialog-container[" \
                                            "1]/anchors-member[1]/section[1]/anchors-member-section[1]/anchors-forms[" \
                                            "1]/anchors-form-builder[1]/div[1]/form[1]/jkf-element-builder[" \
                                            "10]/anchors-wrapper-element[1]/anchors-select-input[1]/div[" \
                                            "1]/mat-form-field[1]/div[1]/div[1]/div[3]/mat-select[1]/div[1]/div[" \
                                            "1]/span[1] "
    list_IsPrimary_PromoterYes_xpath = "/html[1]/body[1]/div[2]/div[4]/div[1]/div[1]/div[1]/mat-option[1]/span[1]"
    list_IsPrimary_PromoterNo_xpath = "/html[1]/body[1]/div[2]/div[4]/div[1]/div[1]/div[1]/mat-option[2]/span[1]"
    dropdownlist_status_xpath = "/html[1]/body[1]/div[2]/div[2]/div[1]/mat-dialog-container[1]/anchors-member[" \
                                "1]/section[1]/anchors-member-section[1]/anchors-forms[1]/anchors-form-builder[" \
                                "1]/div[1]/form[1]/jkf-element-builder[11]/anchors-wrapper-element[" \
                                "1]/anchors-select-input[1]/div[1]/mat-form-field[1]/div[1]/div[1]/div[3] "
    list_statusActive_xpath = "/html[1]/body[1]/div[2]/div[4]/div[1]/div[1]/div[1]/mat-option[1]/span[1]"
    list_statusInactive_xpath = "/html[1]/body[1]/div[2]/div[4]/div[1]/div[1]/div[1]/mat-option[2]/span[1]"
    button_submitBankdetails_xpath = "/html[1]/body[1]/div[2]/div[2]/div[1]/mat-dialog-container[1]/anchors-member[" \
                                     "1]/section[1]/anchors-member-section[1]/anchors-forms[1]/anchors-form-builder[" \
                                     "1]/div[1]/div[1]/button[1]/span[1] "
    link_BankAcc_xpath = "/html[1]/body[1]/anchors-root[1]/anchors-anchors-container[1]/anchors-application-details[" \
                         "1]/div[1]/div[3]/div[1]/mat-tab-group[1]/div[1]/mat-tab-body[1]/div[1]/div[" \
                         "1]/anchors-section-renderer[1]/div[1]/anchors-content-decider[4]/anchors-member-details[" \
                         "1]/div[1]/anchors-table[1]/div[1]/div[3]/anchors-table-card[1]/mat-card[" \
                         "1]/mat-card-content[1]/div[1]/anchors-table-base[1]/div[1]/table[1]/tbody[1]/tr[1]/td[2] "
    # Bank statements = bs:
    button_UploadStatement_Bankstatemet_xpath = "//span[contains(text(),'Upload Statement')]"
    dropdownlist_Bankname_xpath = "//input[@id='en-sec-upload-bank-statement-bankName']"
    list_Bankname_ICICI_xpath = "//span[contains(text(),'ICICI')]"
    list_Bankname_SBI_xpath = "//span[contains(text(),'SBI')]"
    list_Bankname_SanmathiSahakariBank_xpath = "//span[contains(text(),'Sanmathi Sahakari Bank')]"
    list_Bankname_YES_xpath = "//body/div[2]/div[5]/div[1]/div[1]/mat-option[4]/span[1]"
    list_Bankname_YESCORP_xpath = "//span[contains(text(),'YES CORP')]"
    dropdownlist_Accounttype_xpath = "/html[1]/body[1]/div[2]/div[4]/div[1]/mat-dialog-container[" \
                                     "1]/anchors-bank-statement-upload[1]/jkf-element-builder[" \
                                     "2]/anchors-wrapper-element[1]/anchors-select-input[1]/div[1]/mat-form-field[" \
                                     "1]/div[1]/div[1]/div[3]/mat-select[1]/div[1]/div[1]/span[1] "
    list_Accounttype_Current_xpath = "/html[1]/body[1]/div[2]/div[6]/div[1]/div[1]/div[1]/mat-option[2]/span[1]"
    list_Accounttype_Saving_xpath = "/html[1]/body[1]/div[2]/div[6]/div[1]/div[1]/div[1]/mat-option[1]/span[1]"
    textbox_password_xpath = "//input[@id='en-sec-upload-bank-statement-password']"
    upload_bankstmt_id = "Upload Bank Statement"
    dropdownlist_documenttype_xpath = "/html[1]/body[1]/div[2]/div[4]/div[1]/mat-dialog-container[" \
                                      "1]/anchors-bank-statement-upload[1]/jkf-element-builder[" \
                                      "3]/anchors-wrapper-element[1]/anchors-select-input[1]/div[1]/mat-form-field[" \
                                      "1]/div[1]/div[1]/div[3]/mat-select[1]/div[1]/div[1]/span[1] "
    list_documenttypeScanned_xpath = "//span[contains(text(),'Scanned')]"
    list_documenttypeOther_xpath = "//span[contains(text(),'Other')]"
    textbox_bs_password_xpath = "//input[@id='mat-input-41']"
    link_bs_uploadbankstatemet_xpath = "//body/div[2]/div[4]/div[1]/mat-dialog-container[" \
                                       "1]/anchors-bank-statement-upload[1]/jkf-element-builder[" \
                                       "5]/anchors-wrapper-element[1]/anchors-document-wrapper[1]/div[" \
                                       "1]/anchors-document-form[1]/div[1]/div[1]/div[2] "

    def __init__(self, driver):
        self.driver = driver

    def clickentity(self):
        self.driver.find_element_by_xpath(self.lnkNewEntity_xpath).click()

    def setspocname(self, spocname):
        self.driver.find_element_by_xpath(self.textbox_spocname_xpath).send_keys(spocname)

    def setspocemail(self, spocemail):
        self.driver.find_element_by_xpath(self.textbox_spocemail_xpath).send_keys(spocemail)

    def setspocmobilenumber(self, spocmobile):
        self.driver.find_element_by_xpath(self.textbox_spocemobile_xpath).send_keys(spocmobile)

    def clickspocdepartment(self):
        self.driver.find_element_by_xpath(self.dropdownlist_department_xpath).click()

    def selectspocdepartment(self):
        self.driver.find_element_by_xpath(self.list_depSalesSouth_xpath).click()

    def clickIsPrimaryspoc(self):
        self.driver.find_element_by_xpath(self.dropdownlist_IsPrimaryspoc_xpath).click()

    def selectIsPrimaryspoc(self):
        self.driver.find_element_by_xpath(self.list_IsPrimaryspocYes_xpath).click()

    def submitspoc(self):
        self.driver.find_element_by_xpath(self.button_submit_xpath).click()

    def clickeditbusinessbutton(self):
        self.driver.find_element_by_xpath(self.button_submit_xpath).click()

    def clickbusinessdetails(self):
        self.driver.find_element_by_xpath(self.button_businessdetailsedit_xpath).click()

    def clickfirmtype(self):
        self.driver.find_element_by_xpath(self.dropdownlist_firmtype_xpath).click()

    def selectfirmtype(self):
        self.driver.find_element_by_xpath(self.list_firmtype_xpath).click()

    def clickEntitytype(self):
        self.driver.find_element_by_xpath(self.dropdownlist_Entitytype_xpath).click()

    def selectentitytype(self):
        self.driver.find_element_by_xpath(self.list_Entitytype_xpath).click()

    def setgst(self, gst):
        self.driver.find_element_by_xpath(self.textbox_gst_xpath).send_keys(gst)

    def clickokgst(self):
        self.driver.find_element_by_xpath(self.button_gstok_xapth).click()

    def setpan(self, pan):
        self.driver.find_element_by_xpath(self.textbox_pan_xpath).send_keys(pan)

    def setcin(self, cin):
        self.driver.find_element_by_xpath(self.textbox_CIN_xpath).send_keys(cin)

    def setLegalname(self, Legalname):
        self.driver.find_element_by_xpath(self.textbox_EntityLegalName_xpath).send_keys(Legalname)

    def setudyogadhar(self, udyogadhar):
        self.driver.find_element_by_xpath(self.textbox_udyogadhar_xpath).send_keys(udyogadhar)

    def setActRegistration(self, seActRegistration):
        self.driver.find_element_by_xpath(self.textbox_seActRegistration_xpath).send_keys(seActRegistration)

    def setfssaiLicense(self, fssaiLicense):
        self.driver.find_element_by_xpath(self.textbox_fssaiLicense_xpath).send_keys(fssaiLicense)

    def setLegalBrandName(self, setLegalBrandName):
        self.driver.find_element_by_xpath(self.textbox_setLegalBrandName_xpath).send_keys(setLegalBrandName)

    def submitbasicinfo(self):
        self.driver.find_element_by_xpath(self.button_submitbasicinfo_xpath).click()

    def clickeditAgain(self):
        self.driver.find_element_by_xpath(self.button_editAgain_xpath).click()

    def setdateOfRegistartion(self, dateOfRegistartion):
        self.driver.find_element_by_xpath(self.textbox_dateOfRegistartion_xpath).send_keys(dateOfRegistartion)

    def setmobileNumber(self, mobileNumber):
        self.driver.find_element_by_xpath(self.textbox_mobileNumber_xpath).send_keys(mobileNumber)

    def setemail(self, email):
        self.driver.find_element_by_xpath(self.textbox_email_xpath).send_keys(email)

    def setwebsite(self, website):
        self.driver.find_element_by_xpath(self.textbox_website_xpath).send_keys(website)

    def setdeedDate(self, deedDate):
        self.driver.find_element_by_xpath(self.textbox_deedDate_xpath).send_keys(deedDate)

    def clickCompanyAct(self):
        self.driver.find_element_by_xpath(self.dropdownlist_CompanyAct_xpath).click()

    def selectCompanyAct(self):
        self.driver.find_element_by_xpath(self.list_CompanyAct_xpath).click()

    def setdescription(self, description):
        self.driver.find_element_by_xpath(self.textbox_description_xpath).send_keys(description)

    def clicksubmitagain(self):
        self.driver.find_element_by_xpath(self.button_submitagain_xpath).click()

    def clickeditbuttonadditionaldetails(self):
        self.driver.find_element_by_xpath(self.button_additionaldetails_xpath).click()

    def clickoperatingmode(self):
        self.driver.find_element_by_xpath(self.dropdownlist_Operatingmode_xpath).click()

    def selectoperatingmode(self):
        self.driver.find_element_by_xpath(self.list_operatingmode_xpath).click()

    def setavgbalance(self, avgbalance):
        self.driver.find_element_by_xpath(self.textbox_averagebankbalance_xpath).send_keys(avgbalance)

    def setmontlyincome(self, montlyincome):
        self.driver.find_element_by_xpath(self.textbox_montlyincome_xpath).send_keys(montlyincome)

    def setannualincome(self, annualincome):
        self.driver.find_element_by_xpath(self.textbox_annualincome_xpath).send_keys(annualincome)

    def submitadditionalinfo(self):
        self.driver.find_element_by_xpath(self.button_submitadditianlinfo_xpath).click()

    def clickeditregadd(self):
        self.driver.find_element_by_xpath(self.button_edit_registeredaddress_xpath).click()

    def setpincode(self, pincode):
        self.driver.find_element_by_xpath(self.textbox_pincode_xpath).send_keys(pincode)

    def clickpincodeok(self):
        self.driver.find_element_by_xpath(self.button_pincode_xpath).click()

    def setvillage(self, village):
        self.driver.find_element_by_xpath(self.textbox_village_xpath).send_keys(village)

    def setlandmark(self, landmark):
        self.driver.find_element_by_xpath(self.textbox_Landmark_xpath).send_keys(landmark)

    def setDistrict(self, District):
        self.driver.find_element_by_xpath(self.textbox_EnterDistrict_xpath).send_keys(District)

    def setTaluk(self, Taluk):
        self.driver.find_element_by_xpath(self.textbox_EnterTaluk_xpath).send_keys(Taluk)

    def clickaddresstype(self):
        self.driver.find_element_by_xpath(self.dropdownlist_Addresstype_xpath).click()

    def selectaddresstype(self):
        self.driver.find_element_by_xpath(self.list_addresstype_rented_xpath).click()

    def submitregisteredadd(self):
        self.driver.find_element_by_xpath(self.button_submitregisteredadd_xpath).click()

    def clickaddbankaccount(self):
        self.driver.find_element_by_xpath(self.button_AddBankAccount_xpath).click()

    def setaccountnumber(self, accountnumber):
        self.driver.find_element_by_xpath(self.textbox_accountnumber_xpath).send_keys(accountnumber)

    def setconfirmaccountnumber(self, confirmaccountnumber):
        self.driver.find_element_by_xpath(self.textbox_confirmaccountnumber_xpath).send_keys(confirmaccountnumber)

    def setaccountholdername(self, accountholdername):
        self.driver.find_element_by_xpath(self.textbox_accountholdername_xpath).send_keys(accountholdername)

    def setifsccode(self, ifsc):
        self.driver.find_element_by_xpath(self.textbox_IFSCcode_xpath).send_keys(ifsc)

    def clickaccounttype(self):
        self.driver.find_element_by_xpath(self.dropdownlist_accounttype_xpath).click()

    def selectaccounttypecurr(self):
        self.driver.find_element_by_xpath(self.list_accounttype_Current_xpath).click()

    def selectaccounttypesaving(self):
        self.driver.find_element_by_xpath(self.list_accounttype_Saving_xpath).click()

    def setmobilenumber(self, mobilenumber):
        self.driver.find_element_by_xpath(self.textbox_mobilenumber_xpath).send_keys(mobilenumber)

    def clickISPrimaryPromotor(self):
        self.driver.find_element_by_xpath(self.dropdownlist_IsPrimary_Promoter_xpath).click()

    def selectISParimaryPromotor(self):
        self.driver.find_element_by_xpath(self.list_IsPrimary_PromoterYes_xpath).click()

    def clickStatus(self):
        self.driver.find_element_by_xpath(self.dropdownlist_status_xpath).click()

    def selectStatus(self):
        self.driver.find_element_by_xpath(self.list_statusActive_xpath).click()

    def clicksubmit(self):
        self.driver.find_element_by_xpath(self.button_submitBankdetails_xpath).click()

    def clickBankEntry(self):
        self.driver.find_element_by_xpath(self.link_BankAcc_xpath).click()

    def clickuploadSatatement(self):
        self.driver.find_element_by_xpath(self.button_UploadStatement_Bankstatemet_xpath).click()

    def clickBankName(self):
        self.driver.find_element_by_xpath(self.dropdownlist_Bankname_xpath).click()

    def selectBankName(self):
        self.driver.find_element_by_xpath(self.list_Bankname_SanmathiSahakariBank_xpath).click()

    def clickAccType(self):
        self.driver.find_element_by_xpath(self.dropdownlist_Accounttype_xpath).click()

    def selectAccTypeCurr(self):
        self.driver.find_element_by_xpath(self.list_Accounttype_Current_xpath).click()

    def selectAccTypeSaving(self):
        self.driver.find_element_by_xpath(self.list_Accounttype_Saving_xpath).click()

    def clickDocType(self):
        self.driver.find_element_by_xpath(self.dropdownlist_documenttype_xpath).click()

    def selectDocType(self):
        self.driver.find_element_by_xpath(self.list_documenttypeScanned_xpath).click()

    def setPassword(self, password):
        self.driver.find_element_by_xpath(self.textbox_password_xpath).send_keys(password)

    def uploadbankstmt(self, bankstmt):
        self.driver.find_element_by_id(self.upload_bankstmt_id).send_keys(bankstmt)
