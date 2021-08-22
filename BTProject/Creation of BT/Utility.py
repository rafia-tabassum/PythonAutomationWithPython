import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchFrameException, InvalidSelectorException

login_bt_id = "ishak"
login_bt_password = "#121123!"
chrome = "E:\Pythonproj\chromedriver.exe"


# Return Chrome driver location

def chrome_driver():
    driver = webdriver.Chrome(executable_path=chrome)
    return driver


# return bt id

def bt_id():
    return login_bt_id


# return bt password
def bt_password():
    return login_bt_password

# user end
def bt_login(driver):
    try:
        driver.get("https://stage-erp.evaly.com.bd/auth/login")  # access web url
        time.sleep(1)
        driver.find_element_by_xpath("//input[@placeholder='Username']").send_keys(
            login_bt_id)  # click user name input field
        time.sleep(1)
        driver.find_element_by_xpath("//input[@placeholder='Password']").send_keys(
            login_bt_password)  # write password
        time.sleep(1)
        driver.find_element_by_xpath(
            "//span[text()='Log In']").click()  # click submit button
        time.sleep(3)
    except(NoSuchFrameException, InvalidSelectorException):
        print("@@@@@ Admin_Login Function Exception occur @@@@@@")