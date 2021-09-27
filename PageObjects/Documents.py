class Documents:
    tab_documents_xpath = "//div[@id='mat-tab-label-0-2']"
    link_gstdocs_xpath = "//mat-tab-body/div[1]/div[1]/anchors-section-renderer[1]/div[1]/anchors-content-decider[1]/anchors-documents[1]/section[1]/div[3]/anchors-document[1]/div[1]/anchors-document-input[1]/div[1]/div[1]/div[1]/span[1]/i[1]"

    def __init__(self, driver):
        self.driver = driver

    def clickdocumentstab(self):
        self.driver.find_element_by_xpath(self.tab_documents_xpath).click()

    def clicklink(self):
        self.driver.find_element_by_xpath(self.link_gstdocs_xpath).click()

