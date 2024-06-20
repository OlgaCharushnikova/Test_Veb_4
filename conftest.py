import pytest, yaml
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import requests

with open("./testdata.yaml") as f:
    testdata = yaml.safe_load(f)
    browser = testdata["browser"]
@pytest.fixture(scope="session")
def browser():
    if browser == "firefox":
        service = Service(executable_path=GeckoDriverManager().install())
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(service=service, options=options)
    else:
        service = Service(executable_path=ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()

@pytest.fixture()
def login():
    res1 = requests.post(testdata["address1"], data={"username": testdata["username"], "password": testdata["password"]})
    return res1.json()["token"]

@pytest.fixture()
def title():
    return "Title"

@pytest.fixture()
def description():
    return "Description"

@pytest.fixture()
def content():
    return "Content"

@pytest.fixture()
def find_description():
    return "Content"