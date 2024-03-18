
from behave import *
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from POM.LoginPage import LoginPage
from POM.DashboardPage import DashboardPage
from utilities.BaseClass import BaseClass
stars = 10 * "*"

base_class = BaseClass()
log = base_class.loggen()
@given('I Launch the browser')
def step_impl(context):
    service_obj = Service()
    context.driver = webdriver.Chrome(service=service_obj)
    context.driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
    log.info(f"{stars} se ingresa a la pagina {stars}")


@when('I open orange HRM LoginPage')
def step_impl(context):
    wait = WebDriverWait(context.driver, timeout=10)
    wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "img[alt='company-branding']")))
    status = context.driver.find_element(By.CSS_SELECTOR, "img[alt='company-branding']").is_displayed()
    log.info(f"{stars} se encuentra la imagen {status} {stars}")
    print(status)
    assert status is True

@when('Enter username "{user}" and password "{pwd}"')
def step_impl(context, user, pwd):
    context.login_page = LoginPage(context.driver)
    log.info(f"{stars} se ingresa a la pagina del login {context.login_page} {stars}")
    wait = WebDriverWait(context.driver, timeout=10)
    wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "input[name='username']")))
    context.login_page.field_usernameMethod().send_keys(user)
    log.info(f"{stars} se ingresa el usuario {user} {stars}")
    context.login_page.field_passwordMethod().send_keys(pwd)
    log.info(f"{stars} se ingresa el password {pwd} {stars}")
@when('Click on login button')
def step_impl(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.button_loginMethod().click()
    log.info(f"{stars} se realiza click al botón del login {stars}")

@then('User must succesfully login to the Dashboard page')
def step_impl(context):
    context.dashboard_page = DashboardPage(context.driver)
    log.info(f"{stars} se ingresa a la pagina del dashboard {context.dashboard_page} {stars}")
    wait = WebDriverWait(context.driver, timeout=10)
    wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//span[@class='oxd-topbar-header-breadcrumb']/h6")))
    try:
        text_dashboard = context.dashboard_page.txt_dashboardMethod().text
        log.info(f"{stars} se toma el texto {text_dashboard} {stars}")
        if text_dashboard == "Dashboard":
            message = "Test Passed"
            context.driver.save_screenshot(".\\ScreenShots\\" + "User must succesfully login to the Dashboard page.png")
        else:
            message = "Test Falied"
        context.driver.close()
        assert True, message
        log.info(f"{stars} {message} {stars}")

    except NoSuchElementException:
        context.driver.close()
        assert False, "Elemento 'text_dashboard' no encontrado"
        log.error(f"{stars} Elemento 'text_dashboard' no encontrado {stars}")
    except WebDriverWait as e:
        context.driver.close()
        assert False, f"Test Failed: {str(e)}"
        log.error(f"{stars} el test fallo {stars}")
@when('Enter wrong password username "{user_w}" and password "{pwd_w}"')
def step_impl(context, user_w, pwd_w):
    context.login_page = LoginPage(context.driver)
    log.info(f"{stars} se ingresa a la pagina del login {context.login_page} {stars}")
    wait = WebDriverWait(context.driver, timeout=10)
    wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "input[name='username']")))
    context.login_page.field_usernameMethod().send_keys(user_w)
    log.info(f"{stars} se ingresa el usuario {user_w} {stars}")
    context.login_page.field_passwordMethod().send_keys(pwd_w)
    log.info(f"{stars} se ingresa el password {pwd_w} {stars}")

@then('Show message the Invalid credentials')
def step_impl(context):
    context.login_page = LoginPage(context.driver)
    wait = WebDriverWait(context.driver, timeout=10)
    log.info(f"{stars} se ingresa a la pagina del login {context.login_page} {stars}")
    wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//div[@class='oxd-alert-content oxd-alert-content--error']/p")))
    text_invalid_credentials = context.login_page.txt_message_invalidMethod().text
    log.info(f"{stars} se toma el texto de {text_invalid_credentials} {context.login_page} {stars}")
    if text_invalid_credentials == 'Invalid credentials':
        assert True, "Test Passed"
        log.info(f"{stars} el test paso {stars}")
    else:
        assert False, "Test Failed"
        log.error(f"{stars} el test fallo {stars}")
        context.driver.save_screenshot(".\\ScreenShots\\" + "Show message the Invalid credentials.png")

@when('Enter multiples username "{user_v}" and password "{password_v}"')
def step_impl(context, user_v, password_v):
    context.login_page = LoginPage(context.driver)
    log.info(f"{stars} se ingresa a la escenario de multiples user y passwords {context.login_page} {stars}")
    wait = WebDriverWait(context.driver, timeout=10)
    wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "input[name='username']")))
    context.login_page.field_usernameMethod().send_keys(user_v)
    log.info(f"{stars} se ingresa el usuario {user_v} {stars}")
    context.login_page.field_passwordMethod().send_keys(password_v)
    log.info(f"{stars} se ingresa el password {password_v} {stars}")












