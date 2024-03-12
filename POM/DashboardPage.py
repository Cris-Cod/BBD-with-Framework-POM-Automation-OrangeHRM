from selenium.webdriver.common.by import By


class DashboardPage:

    def __init__(self, driver):
        self.driver = driver

    txt_dashboard = (By.XPATH, "//span[@class='oxd-topbar-header-breadcrumb']/h6")

    def txt_dashboardMethod(self):
        return self.driver.find_element(*DashboardPage.txt_dashboard)