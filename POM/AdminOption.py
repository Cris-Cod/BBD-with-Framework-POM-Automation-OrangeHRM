from selenium.webdriver.common.by import By
class AdminOption:

    def __init__(self, driver):
        self.driver = driver

    selectRole = (By.XPATH, "(//div[@role='option'])[2]")
    fieldSelectRole = (By.XPATH, "(//div[@class='oxd-select-wrapper'])[1]")

    fieldEmployeeName = (By.XPATH, "//div[@class='oxd-autocomplete-text-input oxd-autocomplete-text-input--active']/input")
    fieldStatus = (By.XPATH, "(//div[@class='oxd-select-wrapper'])[2]")
    selectStatus = (By.XPATH, "(//div[@class='oxd-select-option'])[2]")
    fieldUsername = (By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[2]")
    fieldPassword = (By.XPATH, "(//input[@type='password'])[1]")
    fieldConfirmPassword = (By.XPATH, "(//input[@type='password'])[2]")
    btnSave = (By.XPATH, "//div[@class='oxd-form-actions']/button[2]")
    autoCompleteEmployeeName = (By.XPATH, "//div[@role='option']/span")
    txt_successfully = (By.XPATH, "//p[@class='oxd-text oxd-text--p oxd-text--toast-message oxd-toast-content-text']")
    #Successfully Saved
    def selectRoleMethod(self):
        return self.driver.find_element(*AdminOption.selectRole)

    def fieldSelectRoleMethod(self):
        return self.driver.find_element(*AdminOption.fieldSelectRole)
    def fieldEmployeeNameMethod(self):
        return self.driver.find_element(*AdminOption.fieldEmployeeName)

    def fieldStatusMethod(self):
        return self.driver.find_element(*AdminOption.fieldStatus)

    def selectStatusMethod(self):
        return self.driver.find_element(*AdminOption.selectStatus)

    def fieldUsernameMethod(self):
        return self.driver.find_element(*AdminOption.fieldUsername)

    def fieldPasswordMethod(self):
        return self.driver.find_element(*AdminOption.fieldPassword)

    def fieldConfirmPasswordMethod(self):
        return self.driver.find_element(*AdminOption.fieldConfirmPassword)

    def btnSaveMethod(self):
        return self.driver.find_element(*AdminOption.btnSave)

    def autoCompleteEmployeeNameMethod(self):
        return self.driver.find_element(*AdminOption.autoCompleteEmployeeName)

    def txt_successfullyNameMethod(self):
        return self.driver.find_element(*AdminOption.txt_successfully)