import pytest
import time
import pytest 
from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# @pytest.fixture()
# def set_up():
#     print("Start test")
#     capabilities = DesiredCapabilities.CHROME.copy()
#     capabilities["pageLoadStrategy"] = "eager"
#     options = webdriver.ChromeOptions()
#     # options.add_argument("--headless")
#     options.add_experimental_option("excludeSwitches", ['enable_logging']) 
#     service = Service()
#     driver = webdriver.Chrome(options=options, service=service)
#     # driver.implicitly_wait(30) 
#     yield driver
#     time.sleep(2)
#     print("Finish test")

@pytest.fixture(scope = "module")
def set_group():
    print("Start test")
    capabilities = DesiredCapabilities.CHROME.copy()
    capabilities["pageLoadStrategy"] = "eager"
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_experimental_option("excludeSwitches", ['enable_logging']) 
    service = Service()
    driver = webdriver.Chrome(options=options, service=service)
    # driver.implicitly_wait(30) 
    yield driver
    time.sleep(2)
    print("Finish test")