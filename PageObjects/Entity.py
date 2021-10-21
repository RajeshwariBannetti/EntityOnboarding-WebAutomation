import select

from selenium import webdriver


class Entity:
    lnkNewEntity_xpath = "//span[contains(text(),'New Entity Onboarding')]"
    textbox_spocname_xpath = "//input[@id='mat-input-1']"
    textbox_spocemail_xpath = "//input[@id='mat-input-2']"
    textbox_spocemobile_xpath = "//input[@id='mat-input-3']"
    dropdownlist_department_xpath = "//body/div[2]/div[2]/div[1]/mat-dialog-container[1]/anchors-new-application[" \
                                    "1]/section[1]/div[2]/div[1]/anchors-forms[1]/anchors-form-builder[1]/div[" \
                                    "1]/form[1]/jkf-element-builder[4]/anchors-wrapper-element[" \
                                    "1]/anchors-select-input[1]/div[1]/mat-form-field[1]/div[1]/div[1]/div[" \
                                    "3]/mat-select[1]/div[1]/div[1]/span[1] "
    list_department_xpath = "//*[contains(text(),' Sales - South ')]"
    dropdownlist_IsPrimaryspoc_xpath = "//body/div[2]/div[2]/div[1]/mat-dialog-container[1]/anchors-new-application[" \
                                       "1]/section[1]/div[2]/div[1]/anchors-forms[1]/anchors-form-builder[1]/div[" \
                                       "1]/form[1]/jkf-element-builder[5]/anchors-wrapper-element[" \
                                       "1]/anchors-select-input[1]/div[1]/mat-form-field[1]/div[1]/div[1]/div[" \
                                       "3]/mat-select[1]/div[1]/div[1]/span[1] "
    list_IsPrimaryspoc_xpath = "//*[contains(text(),' Yes')]"
    button_submit_xpath = "//*[contains(text(),'Submit')]"
    button_businessdetailsedit_xpath = "//*[contains(text(),'Edit')]"
    dropdownlist_firmtype_xpath = "//mat-tab-body/div[1]/div[1]/anchors-section-renderer[1]/div[" \
                                  "1]/anchors-content-decider[" \
                                  "1]/anchors-forms[1]/anchors-form-builder[1]/div[1]/form[1]/jkf-element-builder[" \
                                  "1]/anchors-wrapper-element[1]/anchors-select-input[1]/div[1]/mat-form-field[" \
                                  "1]/div[1]/div[" \
                                  "1]/div[3] "
    list_firmtype_xpath = "/html[1]/body[1]/div[2]/div[2]/div[1]/div[1]/div[1]/mat-option[1]/span[1]"
    dropdownlist_Entitytype_xpath = "//mat-tab-body/div[1]/div[1]/anchors-section-renderer[1]/div[" \
                                    "1]/anchors-content-decider[1]/anchors-forms[1]/anchors-form-builder[1]/div[" \
                                    "1]/form[1]/jkf-element-builder[2]/anchors-wrapper-element[" \
                                    "1]/anchors-select-input[1]/div[1]/mat-form-field[1]/div[1]/div[1]/div[3] "
    list_Entitytype_xpath = "//*[contains(text(),'Agri Value Chain Supplier')]"
    textbox_gst_id = "mat-input-4"
    button_gstok_xapth = "//span[contains(text(),'OK')]"
    textbox_pan_id = "mat-input-5"
    textbox_CIN_id = "mat-input-6"
    textbox_EntityLegalName_id = "mat-input-7"
    button_submitbasicinfo_xpath = "//span[contains(text(),'Submit')]"

    # Additional details =ad
    button_additionaldetails_xpath = "/html[1]/body[1]/anchors-root[1]/anchors-anchors-container[" \
                                     "1]/anchors-application-details[1]/div[1]/div[3]/div[1]/mat-tab-group[1]/div[" \
                                     "1]/mat-tab-body[1]/div[1]/div[1]/anchors-section-renderer[1]/div[" \
                                     "1]/anchors-content-decider[2]/anchors-forms[1]/anchors-form-builder[1]/div[" \
                                     "1]/div[1]/button[1] "
    dropdownlist_Operatingmode_xpath = "//mat-tab-body/div[1]/div[1]/anchors-section-renderer[1]/div[" \
                                       "1]/anchors-content-decider[2]/anchors-forms[1]/anchors-form-builder[1]/div[" \
                                       "1]/form[1]/jkf-element-builder[1]/anchors-wrapper-element[" \
                                       "1]/anchors-select-input[1]/div[1]/mat-form-field[1]/div[1]/div[1]/div[3] "
    list_operatingmode_xpath = "/html[1]/body[1]/div[2]/div[2]/div[1]/div[1]/div[1]/mat-option[2]/span[1]"
    textbox_averagebankbalance_xpath = "/html[1]/body[1]/anchors-root[1]/anchors-anchors-container[" \
                                       "1]/anchors-application-details[1]/div[1]/div[3]/div[1]/mat-tab-group[1]/div[" \
                                       "1]/mat-tab-body[1]/div[1]/div[1]/anchors-section-renderer[1]/div[" \
                                       "1]/anchors-content-decider[2]/anchors-forms[1]/anchors-form-builder[1]/div[" \
                                       "1]/form[1]/jkf-element-builder[2]/anchors-wrapper-element[" \
                                       "1]/anchors-number-input[1]/div[1]/mat-form-field[1]/div[1]/div[1]/div[" \
                                       "3]/input[1] "
    textbox_montlyincome_xpath = "/html[1]/body[1]/anchors-root[1]/anchors-anchors-container[" \
                                 "1]/anchors-application-details[1]/div[1]/div[3]/div[1]/mat-tab-group[1]/div[" \
                                 "1]/mat-tab-body[1]/div[1]/div[1]/anchors-section-renderer[1]/div[" \
                                 "1]/anchors-content-decider[2]/anchors-forms[1]/anchors-form-builder[1]/div[1]/form[" \
                                 "1]/jkf-element-builder[3]/anchors-wrapper-element[1]/anchors-number-input[1]/div[" \
                                 "1]/mat-form-field[1]/div[1]/div[1]/div[3]/input[1] "
    textbox_annualincome_xpath = "/html[1]/body[1]/anchors-root[1]/anchors-anchors-container[" \
                                 "1]/anchors-application-details[1]/div[1]/div[3]/div[1]/mat-tab-group[1]/div[" \
                                 "1]/mat-tab-body[1]/div[1]/div[1]/anchors-section-renderer[1]/div[" \
                                 "1]/anchors-content-decider[2]/anchors-forms[1]/anchors-form-builder[1]/div[1]/form[" \
                                 "1]/jkf-element-builder[4]/anchors-wrapper-element[1]/anchors-number-input[1]/div[" \
                                 "1]/mat-form-field[1]/div[1]/div[1]/div[3]/input[1] "
    button_submitadditianlinfo_xpath = "/html[1]/body[1]/anchors-root[1]/anchors-anchors-container[" \
                                       "1]/anchors-application-details[1]/div[1]/div[3]/div[1]/mat-tab-group[1]/div[" \
                                       "1]/mat-tab-body[1]/div[1]/div[1]/anchors-section-renderer[1]/div[" \
                                       "1]/anchors-content-decider[2]/anchors-forms[1]/anchors-form-builder[1]/div[" \
                                       "1]/div[1]/button[1]/span[1] "

    # Registered Address
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
    # textbox_ra_EnterState_xpath = "//input[@id='mat-input-15']"
    # textbox_ra_EnterDistrict_xpath = "//input[@id='mat-input-16']"
    # textbox_ra_EnterTaluka_xpath = "//input[@id='mat-input-17']"
    textbox_village_id = "mat-input-5"
    textbox_Landmark_id = "mat-input-6"
    textbox_streetaddress1_id = "mat-input-7"
    textbox_streetaddress2_id = "mat-input-8"
    dropdownlist_Addresstype_xpath = "//div[@id='mat-select-value-5']"
    list_addresstype_owned_xpath = "//span[contains(text(),'Owned')]"
    list_addresstype_rented_xpath = "//span[contains(text(),'Rented')]"
    # textbox_latitude_xpath = "//input[@id='mat-input-22']"
    # textbox_longitude_xpath = "//input[@id='mat-input-23']"
    button_submitregisteredadd_xpath = "//mat-tab-body/div[1]/div[1]/anchors-section-renderer[1]/div[" \
                                       "1]/anchors-content-decider[3]/anchors-forms[1]/anchors-form-builder[1]/div[" \
                                       "1]/div[1]/button[1] "

    #  Add Bank Account
    button_AddBankAccount_xpath = "/html[1]/body[1]/anchors-root[1]/anchors-anchors-container[" \
                                  "1]/anchors-application-details[1]/div[1]/div[3]/div[1]/mat-tab-group[1]/div[" \
                                  "1]/mat-tab-body[1]/div[1]/div[1]/anchors-section-renderer[1]/div[" \
                                  "1]/anchors-content-decider[4]/anchors-member-details[1]/div[1]/anchors-table[" \
                                  "1]/div[1]/div[2]/div[2]/button[2]/span[1] "

    # Account information = ai
    textbox_ai_accountnumber_xpath = "/html[1]/body[1]/div[2]/div[2]/div[1]/mat-dialog-container[1]/anchors-member[" \
                                     "1]/section[1]/anchors-member-section[1]/anchors-forms[1]/anchors-form-builder[" \
                                     "1]/div[1]/form[1]/jkf-element-builder[1]/anchors-wrapper-element[" \
                                     "1]/anchors-text-input[1]/div[1]/mat-form-field[1]/div[1]/div[1]/div[3]/input[1] "
    textbox_ai_confirmaccountnumber_xpath = "/html[1]/body[1]/div[2]/div[2]/div[1]/mat-dialog-container[" \
                                            "1]/anchors-member[1]/section[1]/anchors-member-section[1]/anchors-forms[" \
                                            "1]/anchors-form-builder[1]/div[1]/form[1]/jkf-element-builder[" \
                                            "2]/anchors-wrapper-element[1]/anchors-text-input[1]/div[" \
                                            "1]/mat-form-field[1]/div[1]/div[1]/div[3]/input[1] "
    textbox_ai_accountholdername_xpath = "/html[1]/body[1]/div[2]/div[2]/div[1]/mat-dialog-container[" \
                                         "1]/anchors-member[1]/section[1]/anchors-member-section[1]/anchors-forms[" \
                                         "1]/anchors-form-builder[1]/div[1]/form[1]/jkf-element-builder[" \
                                         "3]/anchors-wrapper-element[1]/anchors-text-input[1]/div[1]/mat-form-field[" \
                                         "1]/div[1]/div[1]/div[3]/input[1] "
    textbox_ai_IFSCcode_xpath = "/html[1]/body[1]/div[2]/div[2]/div[1]/mat-dialog-container[1]/anchors-member[" \
                                "1]/section[1]/anchors-member-section[1]/anchors-forms[1]/anchors-form-builder[" \
                                "1]/div[1]/form[1]/jkf-element-builder[4]/anchors-wrapper-element[" \
                                "1]/anchors-text-input[1]/div[1]/mat-form-field[1]/div[1]/div[1]/div[3]/input[1] "
    textbox_ai_EnterMICRCODE_xpath = "//input[@id='mat-input-28']"
    textbox_ai_bankname_xpath = "//input[@id='mat-input-29']"
    textbox_ai_bankaddress_xpath = "//input[@id='mat-input-30']"
    dropdownlist_accounttype_xpath = "/html[1]/body[1]/div[2]/div[2]/div[1]/mat-dialog-container[1]/anchors-member[" \
                                     "1]/section[1]/anchors-member-section[1]/anchors-forms[1]/anchors-form-builder[" \
                                     "1]/div[1]/form[1]/jkf-element-builder[8]/anchors-wrapper-element[" \
                                     "1]/anchors-select-input[1]/div[1]/mat-form-field[1]/div[1]/div[1]/div[3] "
    list_ai_accounttype_Current_xpath = "/html[1]/body[1]/div[2]/div[4]/div[1]/div[1]/div[1]/mat-option[1]/span[1]"
    list_ra_accounttype_Saving_xpath = "//span[contains(text(),'Saving')]"
    textbox_ai_mobilenumber_xpath = "/html[1]/body[1]/div[2]/div[2]/div[1]/mat-dialog-container[1]/anchors-member[" \
                                    "1]/section[1]/anchors-member-section[1]/anchors-forms[1]/anchors-form-builder[" \
                                    "1]/div[1]/form[1]/jkf-element-builder[9]/anchors-wrapper-element[" \
                                    "1]/anchors-number-input[1]/div[1]/mat-form-field[1]/div[1]/div[1]/div[3]/input[1] "
    dropdownlist_ai_Is_Primary_Promoter_xpath = "/html[1]/body[1]/div[2]/div[2]/div[1]/mat-dialog-container[" \
                                                "1]/anchors-member[1]/section[1]/anchors-member-section[" \
                                                "1]/anchors-forms[1]/anchors-form-builder[1]/div[1]/form[" \
                                                "1]/jkf-element-builder[10]/anchors-wrapper-element[" \
                                                "1]/anchors-select-input[1]/div[1]/mat-form-field[1]/div[1]/div[" \
                                                "1]/div[3]/mat-select[1]/div[1]/div[1]/span[1] "
    list_ai_Is_Primary_Promoter_Yes_xpath = "/html[1]/body[1]/div[2]/div[4]/div[1]/div[1]/div[1]/mat-option[1]/span[1]"
    list_ra_Is_Primary_Promoter_No_xpath = "//span[contains(text(),'Yes')]"

    dropdownlist_ai_status_xpath = "/html[1]/body[1]/div[2]/div[2]/div[1]/mat-dialog-container[1]/anchors-member[" \
                                   "1]/section[1]/anchors-member-section[1]/anchors-forms[1]/anchors-form-builder[" \
                                   "1]/div[1]/form[1]/jkf-element-builder[11]/anchors-wrapper-element[" \
                                   "1]/anchors-select-input[1]/div[1]/mat-form-field[1]/div[1]/div[1]/div[3] "
    list_ai_status_Active_xpath = "//span[contains(text(),'Active')]"
    list_ai_status_Inactive_xpath = "//span[contains(text(),'Inactive')]"
    button_submitBankdetails_xpath = "/html[1]/body[1]/div[2]/div[2]/div[1]/mat-dialog-container[1]/anchors-member[" \
                                     "1]/section[1]/anchors-member-section[1]/anchors-forms[1]/anchors-form-builder[" \
                                     "1]/div[1]/div[1]/button[1]/span[1] "

    # Bank statements = bs:
    button_UploadStatement_Bankstatemet_xpath = "//span[contains(text(),'Upload Statement')]"
    dropdownlist_bs_Bankname_xpath = "//input[@id='mat-input-40']"
    list_bs_Bankname_ICICI_xpath = "//span[contains(text(),'ICICI')]"
    list_bs_Bankname_SBI_xpath = "//span[contains(text(),'SBI')]"
    list_bs_Bankname_SanmathiSahakariBank_xpath = "//span[contains(text(),'Sanmathi Sahakari Bank')]"
    list_bs_Bankname_YES_xpath = "//body/div[2]/div[5]/div[1]/div[1]/mat-option[4]/span[1]"
    list_bs_Bankname_YESCORP_xpath = "//span[contains(text(),'YES CORP')]"
    dropdownlist_bs_Accounttype_xpath = "//body/div[2]/div[4]/div[1]/mat-dialog-container[" \
                                        "1]/anchors-bank-statement-upload[1]/jkf-element-builder[" \
                                        "2]/anchors-wrapper-element[1]/anchors-select-input[1]/div[1]/mat-form-field[" \
                                        "1]/div[1]/div[1]/div[3] "
    list_bs_accounttype_Current_xpath = "//span[contains(text(),'Current')]"
    list_bs_accounttype_Saving_xpath = "//body/div[2]/div[6]/div[1]/div[1]/div[1]/mat-option[1]/span[1]"
    dropdownlist_bs_documenttypr_xpath = "//body/div[2]/div[4]/div[1]/mat-dialog-container[" \
                                         "1]/anchors-bank-statement-upload[1]/jkf-element-builder[" \
                                         "3]/anchors-wrapper-element[1]/anchors-select-input[1]/div[1]/mat-form-field[" \
                                         "1]/div[1]/div[1]/div[3]/mat-select[1]/div[1]/div[1]/span[1] "
    option_bs_documenttype_Scanned_xpath = "//span[contains(text(),'Scanned')]"
    option_bs_documenttype_Other_xpath = "//span[contains(text(),'Other')]"
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
        self.driver.find_element_by_xpath(self.list_department_xpath).click()

    def clickIsPrimaryspoc(self):
        self.driver.find_element_by_xpath(self.dropdownlist_IsPrimaryspoc_xpath).click()

    def selectIsPrimaryspoc(self):
        self.driver.find_element_by_xpath(self.list_IsPrimaryspoc_xpath).click()

    def submitspoc(self):
        self.driver.find_element_by_xpath(self.button_submit_xpath).click()

    def clickeditbusinessbutton(self):
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
        self.driver.find_element_by_id(self.textbox_gst_id).send_keys(gst)

    def clickokgst(self):
        self.driver.find_element_by_xpath(self.button_gstok_xapth).click()

    def setpan(self, pan):
        self.driver.find_element_by_id(self.textbox_pan_id).send_keys(pan)

    def setcin(self, cin):
        self.driver.find_element_by_id(self.textbox_CIN_id).send_keys(cin)

    def setLegalname(self, Legalname):
        self.driver.find_element_by_id(self.textbox_EntityLegalName_id).send_keys(Legalname)

    def submitbasicinfo(self):
        self.driver.find_element_by_xpath(self.button_submitbasicinfo_xpath).click()

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
        self.driver.find_element_by_id(self.textbox_village_id).send_keys(village)

    def setlandmark(self, landmark):
        self.driver.find_element_by_id(self.textbox_Landmark_id).send_keys(landmark)

    def setstreetaddress1(self, streetaddress1):
        self.driver.find_element_by_id(self.textbox_streetaddress1_id).send_keys(streetaddress1)

    def setstreetaddress2(self, streetaddress2):
        self.driver.find_element_by_id(self.textbox_streetaddress2_id).send_keys(streetaddress2)

    def clickaddresstype(self):
        self.driver.find_element_by_xpath(self.dropdownlist_Addresstype_xpath).click()

    def selectaddresstype(self):
        self.driver.find_element_by_xpath(self.list_addresstype_rented_xpath).click()

    def submitregisteredadd(self):
        self.driver.find_element_by_xpath(self.button_submitregisteredadd_xpath).click()

    def clickaddbankaccount(self):
        self.driver.find_element_by_xpath(self.button_AddBankAccount_xpath).click()

    def setaccountnumber(self, accountnumber):
        self.driver.find_element_by_xpath(self.textbox_ai_accountnumber_xpath).send_keys(accountnumber)

    def setconfirmaccountnumber(self, confirmaccountnumber):
        self.driver.find_element_by_xpath(self.textbox_ai_confirmaccountnumber_xpath).send_keys(confirmaccountnumber)

    def setaccountholdername(self, accountholdername):
        self.driver.find_element_by_xpath(self.textbox_ai_accountholdername_xpath).send_keys(accountholdername)

    def setifsccode(self, ifsc):
        self.driver.find_element_by_xpath(self.textbox_ai_IFSCcode_xpath).send_keys(ifsc)

    def clickaccounttype(self):
        self.driver.find_element_by_xpath(self.dropdownlist_accounttype_xpath).click()

    def selectaccounttype(self):
        self.driver.find_element_by_xpath(self.list_ai_accounttype_Current_xpath).click()

    def setmobilenumber(self, mobilenumber):
        self.driver.find_element_by_xpath(self.textbox_ai_mobilenumber_xpath).send_keys(mobilenumber)

    def clickISPrimaryPromotor(self):
        self.driver.find_element_by_xpath(self.dropdownlist_ai_Is_Primary_Promoter_xpath).click()

    def selectISParimaryPromotor(self):
        self.driver.find_element_by_xpath(self.list_ra_Is_Primary_Promoter_No_xpath).click()

    def clickStatus(self):
        self.driver.find_element_by_xpath(self.dropdownlist_ai_status_xpath).click()

    def selectStatus(self):
        self.driver.find_element_by_xpath(self.list_ai_status_Active_xpath).click()

    def clicksubmit(self):
        self.driver.find_element_by_xpath(self.button_submitBankdetails_xpath).click()

    # def clcikuploadbankstatement(self):
    #     self.driver.find_element_by_xpath(self.button_UploadStatement_Bankstatemet_xpath).click()
