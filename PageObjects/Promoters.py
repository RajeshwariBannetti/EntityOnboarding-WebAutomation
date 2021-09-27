class Promoters:
    clickon_entitytoedit_xpath = "//tbody/tr[2]/td[3]"
    tab_PromotersandGuarantors_xpath = "//div[@id='mat-tab-label-0-1']"
    button_NewPromoter_xpath = "//mat-tab-body/div[1]/div[1]/anchors-section-renderer[1]/div[" \
                               "1]/anchors-content-decider[1]/anchors-member-details[1]/div[1]/anchors-table[1]/div[" \
                               "1]/div[2]/div[3]/button[2]/span[2] "
    textbox_promoterinfo_xpath = "//body/div[2]/div[2]/div[1]/mat-dialog-container[1]/anchors-member[1]/section[" \
                                 "1]/anchors-member-section[1]/anchors-forms[1]/anchors-form-builder[1]/div[2]/form[" \
                                 "1]/jkf-element-builder[1]/anchors-wrapper-element[1]/anchors-text-input[1]/div[" \
                                 "1]/mat-form-field[1]/div[1]/div[1]/div[3] "
    textbox_Promoterfathername_xpath = "//body/div[2]/div[2]/div[1]/mat-dialog-container[1]/anchors-member[" \
                                       "1]/section[1]/anchors-member-section[1]/anchors-forms[" \
                                       "1]/anchors-form-builder[1]/div[2]/form[1]/jkf-element-builder[" \
                                       "2]/anchors-wrapper-element[1]/anchors-text-input[1]/div[1]/mat-form-field[" \
                                       "1]/div[1]/div[1]/div[3] "
    button_guarantor_xpath = "//mat-tab-body/div[1]/div[1]/anchors-section-renderer[1]/div[" \
                             "1]/anchors-content-decider[2]/anchors-member-details[1]/div[1]/anchors-table[1]/div[" \
                             "1]/div[2]/div[3]/button[2] "

    def __init__(self, driver):
        self.driver = driver

    def clickonanyentity(self):
        self.driver.find_element_by_xpath(self.clickon_entitytoedit_xpath).click()

    def clickPromoterguarantorstab(self):
        self.driver.find_element_by_xpath(self.tab_PromotersandGuarantors_xpath).click()

    def clickaddnewpromoter(self):
        self.driver.find_element_by_xpath(self.button_NewPromoter_xpath).click()

    def setpromotername(self, promotername):
        self.driver.find_element_by_xpath(self.textbox_promoterinfo_xpath).send_keys(promotername)

    def setpromoterfathername(self, promoterfamathername):
        self.driver.find_element_by_xpath(self.textbox_Promoterfathername_xpath).send_keys(promoterfamathername)

    def clickaddnewguarantor(self):
        self.driver.find_element_by_xpath(self.button_guarantor_xpath).click()
