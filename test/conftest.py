import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.chrome.service import Service

driver = None

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="firefox"
    )

@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name =request.config.getoption("browser_name")
    if browser_name == "firefox":
        service_obj = Service()
        driver = webdriver.Firefox(service=service_obj)
    elif browser_name == "chrome":
        service_obj = Service("chromedriver.exe")
        driver = webdriver.Chrome(service=service_obj)
    elif browser_name == "IE":
        service_obj = Service("msedgedriver.exe")
        driver = webdriver.Edge(service=service_obj)
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()