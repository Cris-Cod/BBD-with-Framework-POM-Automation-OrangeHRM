import time

from behave import *
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from POM.DashboardPage import DashboardPage
from POM.LoginPage import LoginPage
from utilities.BaseClass import BaseClass
from POM.AdminOption import AdminOption
stars = 10 * "*"

base_class = BaseClass()
log = base_class.loggen()




@when('Enter username "{user}" and password "{pwd}" and click on login button')
def step_impl(context, user, pwd):
    context.login_page = LoginPage(context.driver)
    log.info(f"{stars} se ingresa a la pagina del login {context.login_page} {stars}")
    wait = WebDriverWait(context.driver, timeout=10)
    wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "input[name='username']")))
    context.login_page.field_usernameMethod().send_keys(user)
    log.info(f"{stars} se ingresa el usuario {user} {stars}")
    context.login_page.field_passwordMethod().send_keys(pwd)
    log.info(f"{stars} se ingresa el password {pwd} {stars}")
    context.login_page.button_loginMethod().click()
    log.info(f"{stars} se realiza click al botón del login {stars}")


@when('User must succesfully login to the Dashboard page')
def step_impl(context):
    context.dashboard_page = DashboardPage(context.driver)
    log.info(f"{stars} se ingresa a la pagina del dashboard {context.dashboard_page} {stars}")
    wait = WebDriverWait(context.driver, timeout=10)
    wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//span[@class='oxd-topbar-header-breadcrumb']/h6")))
    text_dashboard = context.dashboard_page.txt_dashboardMethod().text
    log.info(f"{stars} se toma el texto {text_dashboard} {stars}")
    if text_dashboard == "Dashboard":
        message = "Test Passed"
    else:
        message = "Test Failed"
    print(message)
    assert True, message
    log.info(f"{stars} {message} {stars}")



@when('enter dashborar page click in Admin option')
def step_impl(context):
    context.dashboard_page = DashboardPage(context.driver)
    log.info(f"{stars} se ingresa a la pagina del dashboard {context.dashboard_page} {stars}")
    context.dashboard_page.btn_adminMethod().click()
    log.info(f"{stars} se realiza click sobre el boton admin {stars}")


@when('click in the button add')
def step_impl(context):
    context.dashboard_page = DashboardPage(context.driver)
    wait = WebDriverWait(context.driver, timeout=10)
    wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//div[@class='orangehrm-header-container']/button")))
    context.dashboard_page.btn_addMethod().click()
    log.info(f"{stars} se realiza click sobre el boton add {stars}")


@then('fill all fields in the form and save the user')
def step_impl(context):
    log.info(f"{stars} se ingresa a la pagina add user{stars}")
    text_succesfully = 'Successfully Saved'
    context.admin_option = AdminOption(context.driver)
    wait = WebDriverWait(context.driver, timeout=10)
    wait.until(expected_conditions.presence_of_element_located((By.XPATH, "(//div[@class='oxd-select-wrapper'])[1]")))
    context.admin_option.fieldSelectRoleMethod().click()
    log.info(f"{stars} se realiza click sobre el campo role{stars}")
    wait = WebDriverWait(context.driver, timeout=10)
    wait.until(expected_conditions.presence_of_element_located((By.XPATH, "(//div[@role='option'])[2]")))
    context.admin_option.selectRoleMethod().click()
    log.info(f"{stars} se seleccina una opción{stars}")
    context.admin_option.fieldEmployeeNameMethod().send_keys("Carlos")
    log.info(f"{stars} se ingresa el nombre del usuario{stars}")
    wait = WebDriverWait(context.driver, 10)
    wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//div[@role='option']/span")))
    context.admin_option.autoCompleteEmployeeNameMethod().click()
    log.info(f"{stars} se selecciona el nombre completo del usuario{stars}")
    context.admin_option.fieldStatusMethod().click()
    log.info(f"{stars} se realiza click sobre el campo status{stars}")
    wait = WebDriverWait(context.driver, timeout=10)
    wait.until(expected_conditions.presence_of_element_located((By.XPATH, "(//div[@class='oxd-select-option'])[2]")))
    context.admin_option.selectStatusMethod().click()
    log.info(f"{stars} se seleccina una opción de status{stars}")
    context.admin_option.fieldUsernameMethod().send_keys("CarlosTest")
    log.info(f"{stars} se ingresa un username{stars}")
    context.driver.save_screenshot(".\\ScreenShots\\" + 'Enter user.png')
    context.admin_option.fieldPasswordMethod().send_keys("Bot1234#")
    log.info(f"{stars} se ingresa el password{stars}")
    context.driver.save_screenshot(".\\ScreenShots\\" + 'Enter password.png')
    context.admin_option.fieldConfirmPasswordMethod().send_keys("Bot1234#")
    log.info(f"{stars} se confirma el password{stars}")
    context.driver.save_screenshot(".\\ScreenShots\\" + 'Enter confirm password.png')
    context.admin_option.btnSaveMethod().click()
    log.info(f"{stars} se hace click al botón save {stars}")
    wait = WebDriverWait(context.driver, timeout=10)
    wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//p[@class='oxd-text oxd-text--p oxd-text--toast-message oxd-toast-content-text']")))
    text = context.admin_option.txt_successfullyNameMethod().text
    log.info(f"{stars} se toma el texto {text} {stars}")
    context.driver.save_screenshot(".\\ScreenShots\\" + 'get the text_succesfully.png')
    if text == text_succesfully:
        assert True
        log.info(f"{stars} el test Passed {text} {stars}")
    else:
        assert False
        log.info(f"{stars} el test Failed {text} {stars}")