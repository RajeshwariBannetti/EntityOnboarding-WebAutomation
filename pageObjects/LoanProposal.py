def click():
    pass


class LoanProposal:
    tab_LoanProposals_xpath = "//div[contains(text(),'Loan Proposals')]"
    button_addNewProposal_xpath = "//mat-tab-body/div[1]/div[1]/anchors-section-renderer[1]/div[" \
                                  "1]/anchors-content-decider[1]/anchors-member-details[1]/div[1]/anchors-table[" \
                                  "1]/div[1]/div[2]/div[2]/button[2] "
    dropdown_LoanProduct_xpath = "//body/div[2]/div[2]/div[1]/mat-dialog-container[1]/anchors-member[1]/section[" \
                                 "1]/anchors-member-section[1]/anchors-forms[1]/anchors-form-builder[1]/div[1]/form[" \
                                 "1]/jkf-element-builder[1]/anchors-wrapper-element[1]/anchors-select-input[1]/div[" \
                                 "1]/mat-form-field[1]/div[1]/div[1]/div[3]/mat-select[1]/div[1]/div[1]/span[1] "
    list_LoanProduct_xpath = "//span[contains(text(),'Equipment Finance')]"
    dropdown_Lender_xpath = "//body/div[2]/div[2]/div[1]/mat-dialog-container[1]/anchors-member[1]/section[" \
                            "1]/anchors-member-section[1]/anchors-forms[1]/anchors-form-builder[1]/div[1]/form[" \
                            "1]/jkf-element-builder[2]/anchors-wrapper-element[1]/anchors-select-input[1]/div[" \
                            "1]/mat-form-field[1]/div[1]/div[1]/div[3] "
    list_Lender_xpath = "//span[contains(text(),'Care India finvest')]"
    textbox_ROI_xpath = "//input[@id='mat-input-0']"
    textbox_LoanAmount_xpath = "//input[@id='mat-input-1']"
    textbox_LTV_xpath = "//input[@id='mat-input-2']"
    textbox_Tenure_xpath = "//input[@id='mat-input-3']"
    dropdown_TenureUnit_xpath = "//body/div[2]/div[2]/div[1]/mat-dialog-container[1]/anchors-member[1]/section[" \
                                "1]/anchors-member-section[1]/anchors-forms[1]/anchors-form-builder[1]/div[1]/form[" \
                                "1]/jkf-element-builder[7]/anchors-wrapper-element[1]/anchors-select-input[1]/div[" \
                                "1]/mat-form-field[1]/div[1]/div[1]/div[3]/mat-select[1]/div[1]/div[1]/span[1] "
    list_TenureUnit_xpath = "//span[contains(text(),'Months')]"
    textbox_ProposedLoan_Amount = "//input[@id='mat-input-4']"
    textbox_ProposedCommercialOffered_xpath = "//input[@id='mat-input-5']"
    dropdown_RepaymentType_xpath = "//body/div[2]/div[2]/div[1]/mat-dialog-container[1]/anchors-member[1]/section[" \
                                   "1]/anchors-member-section[1]/anchors-forms[1]/anchors-form-builder[1]/div[" \
                                   "1]/form[1]/jkf-element-builder[10]/anchors-wrapper-element[" \
                                   "1]/anchors-select-input[1]/div[1]/mat-form-field[1]/div[1]/div[1]/div[" \
                                   "3]/mat-select[1]/div[1]/div[1]/span[1] "
    list_RepaymentType_xpath = "//span[contains(text(),'STANDARD')]"
    dropdown_Category_xpath = "//body/div[2]/div[2]/div[1]/mat-dialog-container[1]/anchors-member[1]/section[" \
                              "1]/anchors-member-section[1]/anchors-forms[1]/anchors-form-builder[1]/div[1]/form[" \
                              "1]/jkf-element-builder[11]/anchors-wrapper-element[1]/anchors-select-input[1]/div[" \
                              "1]/mat-form-field[1]/div[1]/div[1]/div[3]/mat-select[1]/div[1]/div[1]/span[1] "
    list_Category_xpath = "//span[contains(text(),'Institution')]"
    dropdown_AgreementType_xpath = "//body/div[2]/div[2]/div[1]/mat-dialog-container[1]/anchors-member[1]/section[" \
                                   "1]/anchors-member-section[1]/anchors-forms[1]/anchors-form-builder[1]/div[" \
                                   "1]/form[1]/jkf-element-builder[12]/anchors-wrapper-element[" \
                                   "1]/anchors-select-input[1]/div[1]/mat-form-field[1]/div[1]/div[1]/div[" \
                                   "3]/mat-select[1]/div[1]/div[1]/span[1] "
    list_AgreementType_xpath = "//span[contains(text(),'FLDG')]"
    dropdown_CommissionType_xpath = "//body/div[2]/div[2]/div[1]/mat-dialog-container[1]/anchors-member[1]/section[" \
                                    "1]/anchors-member-section[1]/anchors-forms[1]/anchors-form-builder[1]/div[" \
                                    "1]/form[1]/jkf-element-builder[13]/anchors-wrapper-element[" \
                                    "1]/anchors-select-input[1]/div[1]/mat-form-field[1]/div[1]/div[1]/div[3] "
    list_CommissionType_xpath = "//span[contains(text(),'Percentage')]"
    textbox_GlobalMargin_xpath = "//input[@id='mat-input-6']"
    textbox_PurposeOfLoan = "//textarea[@id='mat-input-7']"
    button_SubmitLoanProposal_xpath = "//body/div[2]/div[2]/div[1]/mat-dialog-container[1]/anchors-member[1]/section[" \
                                      "1]/anchors-member-section[1]/anchors-forms[1]/anchors-form-builder[1]/div[" \
                                      "1]/div[1]/button[1] "
    # Product Subvention list
    link_Edit_LOANProposal_xpath = "//tbody/tr[1]/td[1]/div[1]/div[1]/div[1]"
    button_addNewProductSubvention_xpath = "//span[contains(text(),'New Product Subvention')]"
    dropdown_product_xpath = "//body/div[2]/div[4]/div[1]/mat-dialog-container[1]/anchors-member[1]/section[" \
                             "1]/anchors-member-section[1]/anchors-forms[1]/anchors-form-builder[1]/div[1]/form[" \
                             "1]/jkf-element-builder[2]/anchors-wrapper-element[1]/anchors-select-input[1]/div[" \
                             "1]/mat-form-field[1]/div[1]/div[1]/div[3]/mat-select[1]/div[1]/div[1]/span[1] "
    list_product_xpath = "//span[contains(text(),'Automatic Feeding system')]"
    dropdown_ProductBrand_xpath = "//body/div[2]/div[4]/div[1]/mat-dialog-container[1]/anchors-member[1]/section[" \
                                  "1]/anchors-member-section[1]/anchors-forms[1]/anchors-form-builder[1]/div[1]/form[" \
                                  "1]/jkf-element-builder[3]/anchors-wrapper-element[1]/anchors-select-input[1]/div[" \
                                  "1]/mat-form-field[1]/div[1]/div[1]/div[3] "
    list_ProductBrand_xpath = "//body/div[2]/div[6]/div[1]/div[1]/div[1]/mat-option[2]/span[1]"

    # Tenure Based Margin
    dropdown_Operator_xpath = "//body/div[2]/div[4]/div[1]/mat-dialog-container[1]/anchors-member[1]/section[" \
                              "1]/anchors-member-section[1]/anchors-forms[1]/anchors-form-builder[1]/div[1]/form[" \
                              "1]/jkf-element-builder[4]/jkf-group-element[1]/div[2]/jkf-element-builder[" \
                              "1]/jkf-array-element[1]/div[2]/div[1]/div[1]/jkf-element-builder[" \
                              "1]/anchors-wrapper-element[1]/anchors-select-input[1]/div[1]/mat-form-field[1]/div[" \
                              "1]/div[1]/div[3] "
    list_Operator_xpath = "//body/div[2]/div[6]/div[1]/div[1]/div[1]/mat-option[1]/span[1]"
    textbox_TenureMargin_xpath = "//input[@id='mat-input-0']"
    dropdown_unit_xpath = "//body/div[2]/div[4]/div[1]/mat-dialog-container[1]/anchors-member[1]/section[" \
                          "1]/anchors-member-section[1]/anchors-forms[1]/anchors-form-builder[1]/div[1]/form[" \
                          "1]/jkf-element-builder[4]/jkf-group-element[1]/div[2]/jkf-element-builder[" \
                          "1]/jkf-array-element[1]/div[2]/div[1]/div[1]/jkf-element-builder[" \
                          "3]/anchors-wrapper-element[1]/anchors-select-input[1]/div[1]/mat-form-field[1]/div[1]/div[" \
                          "1]/div[3]/mat-select[1]/div[1]/div[1]/span[1] "
    list_unit_xpath = "//span[contains(text(),'Days')]"

    # Loan Amount Based
    dropdown_operator_xpath = "//body/div[2]/div[4]/div[1]/mat-dialog-container[1]/anchors-member[1]/section[" \
                              "1]/anchors-member-section[1]/anchors-forms[1]/anchors-form-builder[1]/div[1]/form[" \
                              "1]/jkf-element-builder[5]/jkf-group-element[1]/div[2]/jkf-element-builder[" \
                              "1]/jkf-array-element[1]/div[2]/div[1]/div[1]/jkf-element-builder[" \
                              "1]/anchors-wrapper-element[1]/anchors-select-input[1]/div[1]/mat-form-field[1]/div[" \
                              "1]/div[1]/div[3] "
    list_operator_xpath = "//body/div[2]/div[6]/div[1]/div[1]/div[1]/mat-option[1]/span[1]"
    textbox_PriceRs_xpath = "//input[@id='mat-input-1']"
    dropdown_MarginUnit_xpath = "//body/div[2]/div[4]/div[1]/mat-dialog-container[1]/anchors-member[1]/section[" \
                                "1]/anchors-member-section[1]/anchors-forms[1]/anchors-form-builder[1]/div[1]/form[" \
                                "1]/jkf-element-builder[6]/anchors-wrapper-element[1]/anchors-select-input[1]/div[" \
                                "1]/mat-form-field[1]/div[1]/div[1]/div[3]/mat-select[1]/div[1]/div[1]/span[1] "
    list_MarginUnit_xpath = "//body/div[2]/div[6]/div[1]/div[1]/div[1]/mat-option[1]/span[1]"
    textbox_Margin_xpath = "//input[@id='mat-input-2']"
    button_SubmitLoanAmountBased_xpath = "//body/div[2]/div[4]/div[1]/mat-dialog-container[1]/anchors-member[" \
                                         "1]/section[1]/anchors-member-section[1]/anchors-forms[" \
                                         "1]/anchors-form-builder[1]/div[1]/div[1]/button[1] "
    # Proposal Agreement List
    button_NewProposal_agreement_xpath = "//span[contains(text(),'New Proposal Agreement')]"
    textbox_FLDGvalue_xpath = "//input[@id='mat-input-0']"
    textbox_NoOFPDCsCollected_xpath = "//input[@id='mat-input-1']"
    textbox_BuyBackArrangements_xpath = "//input[@id='mat-input-2']"
    textbox_PlatformPeriod_xpath = "//input[@id='mat-input-3']"
    button_SubmitPAL_xpath = "//body/div[2]/div[4]/div[1]/mat-dialog-container[1]/anchors-member[1]/section[" \
                             "1]/anchors-member-section[1]/anchors-forms[1]/anchors-form-builder[1]/div[1]/div[" \
                             "1]/button[1] "

    # Proposal Documents
    doclink_JKDDQuestionnaire_xpath = "//body/div[2]/div[2]/div[1]/mat-dialog-container[1]/anchors-member[1]/section[" \
                                      "1]/anchors-member-section[4]/anchors-documents[1]/section[1]/div[" \
                                      "3]/anchors-document[1]/div[1]/anchors-document-input[1]/div[1]/div[1]/div[2] "

    def __init__(self, driver):
        self.driver = driver

    def clickLoanProposaltab(self):
        self.driver.find_element_by_xpath(self.tab_LoanProposals_xpath).click()

    def clickaddNewProposal(self):
        self.driver.find_element_by_xpath(self.button_addNewProposal_xpath).click()

    def clickLoanProduct(self):
        self.driver.find_element_by_xpath(self.dropdown_LoanProduct_xpath).click()

    def selectLoanProduct(self):
        self.driver.find_element_by_xpath(self.list_LoanProduct_xpath).click()

    def clickLender(self):
        self.driver.find_element_by_xpath(self.dropdown_Lender_xpath).click()

    def selectLender(self):
        self.driver.find_element_by_xpath(self.list_Lender_xpath).click()

    def setROI(self, ROI):
        self.driver.find_element_by_xpath(self.textbox_ROI_xpath).send_keys(ROI)

    def setLoanAmount(self, LoanAmount):
        self.driver.find_element_by_xpath(self.textbox_LoanAmount_xpath).send_keys(LoanAmount)

    def setLTV(self, LTV):
        self.driver.find_element_by_xpath(self.textbox_LTV_xpath).send_keys(LTV)

    def setTenure(self, Tenure):
        self.driver.find_element_by_xpath(self.textbox_Tenure_xpath).send_keys(Tenure)

    def clickTenureUnit(self):
        self.driver.find_element_by_xpath(self.dropdown_TenureUnit_xpath).click()

    def selectTenureUnit(self):
        self.driver.find_element_by_xpath(self.list_TenureUnit_xpath).click()

    def setProposedLoanAmount(self, Amount):
        self.driver.find_element_by_xpath(self.textbox_ProposedLoan_Amount).send_keys(Amount)

    def setProposedCommercialOffered(self, ProposedCommercialOffered):
        self.driver.find_element_by_xpath(self.textbox_ProposedCommercialOffered_xpath).send_keys(
            ProposedCommercialOffered)

    def clickRepaymentType(self):
        self.driver.find_element_by_xpath(self.dropdown_RepaymentType_xpath).click()

    def selectRepaymentType(self):
        self.driver.find_element_by_xpath(self.list_RepaymentType_xpath).click()

    def clickCategory(self):
        self.driver.find_element_by_xpath(self.dropdown_Category_xpath).click()

    def selectCategory(self):
        self.driver.find_element_by_xpath(self.list_Category_xpath).click()

    def clickAgreementType(self):
        self.driver.find_element_by_xpath(self.dropdown_AgreementType_xpath).click()

    def selectAgreementType(self):
        self.driver.find_element_by_xpath(self.list_AgreementType_xpath).click()

    def clickCommission(self):
        self.driver.find_element_by_xpath(self.dropdown_CommissionType_xpath).click()

    def selectCommission(self):
        self.driver.find_element_by_xpath(self.list_CommissionType_xpath).click()

    def setGlobalMargin(self, GlobalMargin):
        self.driver.find_element_by_xpath(self.textbox_GlobalMargin_xpath).send_keys(GlobalMargin)

    def setPurposeOfLoan(self, PurposeOfLoan):
        self.driver.find_element_by_xpath(self.textbox_PurposeOfLoan).send_keys(PurposeOfLoan)

    def clickSubmitLoanProposal(self):
        self.driver.find_element_by_xpath(self.button_SubmitLoanProposal_xpath).click()

    def clicklink(self):
        self.driver.find_element_by_xpath(self.link_Edit_LOANProposal_xpath).click()

    def clickANPS(self):
        self.driver.find_element_by_xpath(self.button_addNewProductSubvention_xpath).click()

    def clickfirstproduct(self):
        self.driver.find_element_by_xpath(self.dropdown_product_xpath).click()

    def selectfirstproduct(self):
        self.driver.find_element_by_xpath(self.list_product_xpath).click()

    def clickProductBrand(self):
        self.driver.find_element_by_xpath(self.dropdown_ProductBrand_xpath).click()

    def selectProductBrand(self):
        self.driver.find_element_by_xpath(self.list_ProductBrand_xpath).click()

    def clickOperator(self):
        self.driver.find_element_by_xpath(self.dropdown_Operator_xpath).click()

    def selectOperator(self):
        self.driver.find_element_by_xpath(self.list_Operator_xpath).click()

    def setTenureMargin(self, TenureMargin):
        self.driver.find_element_by_xpath(self.textbox_TenureMargin_xpath).send_keys(TenureMargin)

    def clickunit(self):
        self.driver.find_element_by_xpath(self.dropdown_unit_xpath).click()

    def selectunit(self):
        self.driver.find_element_by_xpath(self.list_unit_xpath).click()

    def clickoperator(self):
        self.driver.find_element_by_xpath(self.dropdown_operator_xpath).click()

    def selectoperator(self):
        self.driver.find_element_by_xpath(self.list_operator_xpath).click()

    def setPriceRs(self, PriceRs):
        self.driver.find_element_by_xpath(self.textbox_PriceRs_xpath).send_keys(PriceRs)

    def clickMarginUnit(self):
        self.driver.find_element_by_xpath(self.dropdown_MarginUnit_xpath).click()

    def selectMarginUnit(self):
        self.driver.find_element_by_xpath(self.list_MarginUnit_xpath).click()

    def setMargin(self, Margin):
        self.driver.find_element_by_xpath(self.textbox_Margin_xpath).send_keys(Margin)

    def clickSubmit(self):
        self.driver.find_element_by_xpath(self.button_SubmitLoanAmountBased_xpath).click()

    def clickNPA(self):
        self.driver.find_element_by_xpath(self.button_NewProposal_agreement_xpath).click()

    def setFLDGvalue(self, FLDGvalue):
        self.driver.find_element_by_xpath(self.textbox_FLDGvalue_xpath).send_keys(FLDGvalue)

    def setNoOFPDCsCollected(self, NoOFPDCsCollected):
        self.driver.find_element_by_xpath(self.textbox_NoOFPDCsCollected_xpath).send_keys(NoOFPDCsCollected)

    def setBuyBackArrangements(self, BuyBackArrangements):
        self.driver.find_element_by_xpath(self.textbox_BuyBackArrangements_xpath).send_keys(BuyBackArrangements)

    def setPlatformPeriod(self, PlatformPeriod):
        self.driver.find_element_by_xpath(self.textbox_PlatformPeriod_xpath).send_keys(PlatformPeriod)

    def clickSubmitPAL(self):
        self.driver.find_element_by_xpath(self.button_SubmitPAL_xpath).click()

    def clickDocJKDDQuestionnaire(self, DocJKDDQuestionnaire):
        self.driver.find_element_by_xpath(self.doclink_JKDDQuestionnaire_xpath).send_keys(DocJKDDQuestionnaire)
