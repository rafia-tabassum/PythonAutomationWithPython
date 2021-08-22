from selenium import webdriver
import random
import time
import pandas as pd
from selenium.common.exceptions import NoSuchFrameException, InvalidSelectorException, WebDriverException, \
    ElementClickInterceptedException, NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.common.keys import Keys

login_admin_id = "ishak"
login_admin_password = "#121123!"

df = pd.read_csv(r"E:\Pythonproj\BTProject\EvalyProducts.csv", header=None)
total_row = df.shape[0]  # total row in excel file
product_id = df[0].tolist()
product_name = df[1].tolist()  # store user id in this variable

random_number = random.randint(1000, 12000)

product_price = random_number
wholesale_price = random_number - 50
seller_price = random_number - 20

driver = webdriver.Chrome(executable_path="E:\Pythonproj\chromedriver.exe") # Driver location
driver.maximize_window()


def admin_login(driver):
    try:
        driver.get("https://beta-erp.evaly.com.bd/")  # access web url
        time.sleep(1)
        driver.find_element_by_xpath(
            "/html/body/div/div[1]/div/section/form/div[1]/label[1]/div/input").click()  # click user name input field
        driver.find_element_by_xpath("/html/body/div/div[1]/div/section/form/div[1]/label[1]/div/input").send_keys(
            login_admin_id)  # write user name
        time.sleep(1)
        driver.find_element_by_xpath("/html/body/div/div[1]/div/section/form/div[1]/label[2]/div/input").send_keys(
            login_admin_password)  # write password
        time.sleep(1)
        driver.find_element_by_xpath(
            "//span[text()='Log In']").click()  # click submit button
        time.sleep(3)
    except(NoSuchFrameException, InvalidSelectorException):
        print("@@@@@ Admin_Login Function Exception occur @@@@@@")


admin_login(driver)
driver.refresh()
time.sleep(2)
driver.find_element_by_xpath("//h4[text()='Shops']").click()
time.sleep(2)
driver.find_element_by_xpath("/html/body/div[1]/section/section/div/ul/li[3]/ul/li[1]/a").click()  # Click primary shops
time.sleep(3)
driver.find_element_by_xpath("(//p[@title='Coffeekon'])[1]").click()
time.sleep(3)
driver.find_element_by_xpath("//button[text()='Primaryshop Products  ']").click()
time.sleep(2)
driver.find_element_by_xpath("//span[text()='Enlist Product']").click()

for i in range(total_row):
    try:
        time.sleep(3)
        driver.find_element_by_xpath("//input[@placeholder='Search....']").send_keys(product_name[i], Keys.ENTER)
        time.sleep(7)
        driver.find_element_by_xpath("/html/body/div[1]/section/div/section/div/table/tbody/tr/td[10]/button").click()
        time.sleep(2)
        # Enlist Products
        driver.find_element_by_name("manage_stock").click()
        driver.find_element_by_name("in_stock").send_keys("5000")
        driver.find_element_by_name("minimum_wholesale_quantity").send_keys("20")
        driver.find_element_by_name("wholesale_price").send_keys(wholesale_price)
        driver.find_element_by_xpath(
            "/html/body/reach-portal/div/div/div/section[2]/div/form/div/div/div[1]/div[1]/div[4]/label/input").click()  # check box product item
        driver.find_element_by_name("seller_price").send_keys(seller_price)
        driver.find_element_by_name("price").send_keys(product_price)

        check_product_name = driver.find_element_by_xpath(
            "//div[@class='mb-4']//li[1]").text  # read product name from enlist modal
        print(check_product_name)
        if check_product_name == "Product Name: N/A":
            driver.find_element_by_xpath("//div[contains(@class,'flex justify-end')]//button[1]").click()
            print("Cancel Button Click")
            time.sleep(3)
        else:
            driver.find_element_by_xpath("//span[text()='Submit']").click()
            print(product_name[i] + " Product Enlist Successfully")
            time.sleep(3)

    except(
            ElementClickInterceptedException, InvalidSelectorException, NoSuchElementException,
            StaleElementReferenceException):
        print("Exception occur")
    # delete character form search
    try:
        searchBox = driver.find_element_by_xpath("//input[@placeholder='Search....']")
        for i in range(len(product_name[i])):
            searchBox.click()
            searchBox.send_keys(Keys.BACK_SPACE)
    except(
            ElementClickInterceptedException, InvalidSelectorException, NoSuchElementException,
            StaleElementReferenceException):
        print("Exception occur")
