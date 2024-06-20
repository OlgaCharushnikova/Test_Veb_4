from testpage import OperationsHelper
import logging
import yaml, time
import requests

with open("./testdata.yaml") as f:
    testdata = yaml.safe_load(f)
name = testdata["username"]
password = testdata["password"]


def test_step1(login, title, description, content, find_description):
    logging.info("Test1 Starting")
    try:
        res1 = requests.post(testdata["address2"],
                             params={"title": title, "description": description, "content": content},
                             headers={"X-Auth-Token": login})
        res2 = requests.get(testdata["address2"],
                            params={"description": find_description}, headers={"X-Auth-Token": login})
    except:
        logging.exception(f"Exception of requests")
        return None
    logging.debug(f"Requests post and get")
    assert res1 and res2


def test_step2(browser):
    logging.info("Test2 Starting")
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login("test")
    testpage.enter_pass("test")
    testpage.click_login_button()
    assert testpage.get_error_text() == "401"

def test_step3(browser):
    logging.info("Test3 Starting")
    testpage = OperationsHelper(browser)
    testpage.enter_login(name)
    testpage.enter_pass(password)
    testpage.click_login_button()
    assert testpage.get_user_text() == f"Hello, {name}"

def test_step4(browser):
    logging.info("Test4 Starting")
    testpage = OperationsHelper(browser)
    testpage.click_new_post_btn()
    testpage.enter_title("test title")
    testpage.enter_description("test description")
    testpage.enter_content("test content")
    testpage.click_save_button()
    time.sleep(2)
    assert testpage.get_res_text() == "test title"
def test_step5(browser):
    logging.info("Test5 Starting")
    testpage = OperationsHelper(browser)
    testpage.click_contact_us()
    testpage.enter_name_feedback("test name")
    testpage.enter_email_feedback("test@mail.ru")
    testpage.enter_content_feedback("test content")
    testpage.click_contact_us_button()
    time.sleep(3)
    assert testpage.get_alert() == "Form successfully submitted"
    time.sleep(4)