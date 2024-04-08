from testpage import OperationHelper
import pytest
import logging
import yaml
import time
from testpage import TestSearchLocators



with open("testdata.yaml", encoding='utf-8') as f:
    testdata = yaml.safe_load(f)



def test_step1(browsser):
    logging.info("Test 1 Starting")
    testpage = OperationHelper(browsser)
    testpage.go_to_site()
    testpage.enter_login("test")
    testpage.enter_pass("test")
    testpage.click_login_button()
    assert testpage.get_error_text() == "401"


def test_step2(browsser):
    logging.info("Test 2 Starting")
    testpage = OperationHelper(browsser)
    testpage.go_to_site()
    testpage.enter_login(testdata.get("login"))
    testpage.enter_pass(testdata.get("password"))
    testpage.click_login_button()
    assert testpage.get_user_text() == f"Hello, {testdata.get('login')}"


def test_step3(browsser):
    logging.info("Test3 Stsrting")
    testpage = OperationHelper(browsser)
    testpage.click_new_post_btn()
    testpage.enter_title(testdata.get("title"))
    testpage.enter_description(testdata.get("description"))
    testpage.enter_content(testdata.get("content"))
    testpage.click_save_btn()
    time.sleep(3)
    assert testpage.get_res_text() == testdata.get("title"), "Test FAILED!"


def test_step4(browsser):
    # test contact us
    logging.info("Test Contact_us Starting")
    testpage = OperationHelper(browsser)
    testpage.click_contact_link()
    testpage.enter_contact_name(testdata.get("username"))
    testpage.enter_contact_email(testdata.get("user_email"))
    testpage.enter_contact_content(testdata.get("content_contact"))
    testpage.click_contact_send_btn()
    assert testpage.get_allert_message() == "Form successfully submitted", "Test FAILED!"




#Добавьте новый тестовый сценарий для проверки действий на странице "About":

def test_about_page(browsser):
    logging.info("Test About Page Starting")
    testpage = OperationHelper(browsser)
    testpage.go_to_site()
    testpage.click_element(TestSearchLocators.ids["LOCATOR_ABOUT_LINK"])
    assert testpage.get_element_text(TestSearchLocators.ids["LOCATOR_ABOUT_PAGE_HEADER"]) == "About Page"
    assert testpage.get_element_font_size(TestSearchLocators.ids["LOCATOR_ABOUT_PAGE_HEADER"]) == "32px"




if __name__ == "__main__":
    pytest.main(["-vv"])