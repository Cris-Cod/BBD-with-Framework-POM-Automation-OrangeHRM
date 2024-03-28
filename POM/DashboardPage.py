from selenium.webdriver.common.by import By


class DashboardPage:

    def __init__(self, driver):
        self.driver = driver

    txt_dashboard = (By.XPATH, "//span[@class='oxd-topbar-header-breadcrumb']/h6")
    btn_admin = (By.XPATH, "//ul[@class='oxd-main-menu']/li[1]")
    btn_add = (By.XPATH, "//div[@class='orangehrm-header-container']/button")

    def txt_dashboardMethod(self):
        return self.driver.find_element(*DashboardPage.txt_dashboard)

    def btn_adminMethod(self):
        return self.driver.find_element(*DashboardPage.btn_admin)

    def btn_addMethod(self):
        return self.driver.find_element(*DashboardPage.btn_add)