from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from utilities.BaseClass import BaseClass
from POM.LoginPage import LoginPage
from POM.DashboardPage import DashboardPage
@given('I Launch the browser')
def step_impl(context):
    context.base_class = BaseClass(context.driver)


@when('I open orange HRM LoginPage')
def step_impl(context):
    wait = WebDriverWait(context.driver, timeout=10)
    wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "img[alt='company-branding']")))
    status = context.driver.find_element(By.CSS_SELECTOR, "img[alt='company-branding']").is_displayed()
    assert status is True

@when('Enter username "admin" and password "admin123"')
def step_impl(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.field_usernameMethod().send_keys("admin")
    context.login_page.field_passwordMethod().send_keys("admin123")

@when('Click on login button')
def step_impl(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.button_loginMethod().click()


@then('User must succesfully login to the Dashboard page')
def step_impl(context):
    context.dashboard_page = DashboardPage(context.driver)
    wait = WebDriverWait(context.driver, timeout=10)
    wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//span[@class='oxd-topbar-header-breadcrumb']/h6")))

    text_dashboard = context.dashboard_page.txt_dashboardMethod().text
    if text_dashboard == 'Dashboard':
        assert True, "Test Passed"
    else:
        assert False, "Test Failed"

@when('Enter username "admin" and password "admin"')
def step_impl(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.field_usernameMethod().send_keys("admin")
    context.login_page.field_passwordMethod().send_keys("admin")


@then('Show message the Invalid credentials')
def step_impl(context):
    context.login_page = LoginPage(context.driver)
    text_invalid_credentials = context.login_page.txt_message_invalidMethod().text
    if text_invalid_credentials == 'Invalid credentials':
        assert True, "Test Passed"
    else:
        assert False, "Test Failed"


@when('Enter username "<ExcelIndex>" and password "<ExcelIndex>"')
def step_impl(context):
    pass


@when('Enter username "1" and password "1"')
def step_impl(context):
   pass


@when('Enter username "2" and password "2"')
def step_impl(context):
    pass


@when(u'Enter username "3" and password "3"')
def step_impl(context):
    pass


@when(u'Enter username "4" and password "4"')
def step_impl(context):
    pass


@when(u'Enter username "5" and password "5"')
def step_impl(context):
   pass



