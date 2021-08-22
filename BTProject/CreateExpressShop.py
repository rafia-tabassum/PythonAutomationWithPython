import random
import string
import time

import autoit
import pandas as pd
from selenium import webdriver
from selenium.common.exceptions import NoSuchFrameException, InvalidSelectorException
from selenium.webdriver.common.keys import Keys

login_admin_id = "ishak"
login_admin_password = "#121123!"

csv_reader = pd.read_csv(r"Express.csv")
total_row = csv_reader.shape[0]

express_name = csv_reader['Express_Shop_Name'].tolist()
primaryshop_name = csv_reader['Primary_Shop_Name'].tolist()
score = csv_reader['Score'].tolist()
commission_rate = csv_reader['Commisssion_Rate'].tolist()
express_service = csv_reader['Express_Service'].tolist()
express_address = csv_reader['Express_Address'].tolist()

minorderquantity = csv_reader['Min_Order_Quantity'].tolist()
minorderamount = csv_reader['Min_Order_Amount'].tolist()
maxorderquantity = csv_reader['Max_Order_Quantity'].tolist()
maxorderamount = csv_reader['Max_Order_Amount'].tolist()

driver = webdriver.Chrome(executable_path="E:\Pythonproj\chromedriver.exe") # Driver location
driver.maximize_window()


def admin_login(driver):
    try:
        driver.get("https://beta-erp.evaly.com.bd/")  # access web url
        time.sleep(1)
        driver.find_element_by_xpath("//input[@placeholder='Username']").send_keys(
            login_admin_id)  # click user name input field
        time.sleep(1)
        driver.find_element_by_xpath("//input[@placeholder='Password']").send_keys(
            login_admin_password)  # write password
        time.sleep(1)
        driver.find_element_by_xpath(
            "//span[text()='Log In']").click()  # click submit button
        time.sleep(3)
    except(NoSuchFrameException, InvalidSelectorException):
        print("@@@@@ Admin_Login Function Exception occur @@@@@@")

admin_login(driver)

clickonshop = driver.find_element_by_xpath("//*[@id='__next']/section/section/div/ul/li[3]/a")
clickonshop.click()
time.sleep(2)

driver.find_element_by_xpath("//li/a[contains(text(),'Express Shops')]").click()
time.sleep(4)

for i in range(total_row):
    driver.find_element_by_xpath("//button/span[contains(text(),'Create Express Shops')]").click()
    time.sleep(2)

    image = driver.find_element_by_xpath("//span[contains(text(),'Choose file')]")
    image.click()
    time.sleep(3)

    if i == 0:
        autoit.run("E:\Pythonproj\BTProject\primaryshoplogo\FileUpload.exe")
        time.sleep(2)
    elif i == 1:
        autoit.run("E:\Pythonproj\BTProject\primaryshoplogo\FileUpload1.exe")
    time.sleep(2)

    uploadimage = driver.find_element_by_xpath("//button[contains(text(),'Upload Now')]")
    uploadimage.click()
    time.sleep(2)
    applycrop = driver.find_element_by_xpath("//span[contains(text(),'Apply Crop')]")
    applycrop.click()
    time.sleep(3)

    uploadbanner = driver.find_element_by_xpath("//*[@id='drop-area_image']/label")
    uploadbanner.click()
    time.sleep(3)

    if i == 0:
        autoit.run("E:\Pythonproj\BTProject\primaryshoplogo\FileUpload2.exe")
    elif i == 1:
        autoit.run("E:\Pythonproj\BTProject\primaryshoplogo\FileUpload3.exe")

    driver.find_element_by_name('name').send_keys(express_name[i]+''.join(random.choice(string.digits) for _ in range(2)))
    driver.find_element_by_name('mother_shop_slug').send_keys(primaryshop_name[i])
    time.sleep(2)
    SelectPrimaryShop = driver.find_element_by_xpath("//span[contains(text(),'Select')]")
    SelectPrimaryShop.click()

    Score = driver.find_element_by_name('score')
    Score.send_keys(score[i])
    # Score.send_keys(Keys.BACKSPACE)
    # Score.send_keys(Keys.BACKSPACE)
    time.sleep(1)
    Commission = driver.find_element_by_name('commission_rate')
    Commission.send_keys(commission_rate[i])
    # Commission.send_keys(Keys.BACKSPACE)
    # Commission.send_keys(Keys.BACKSPACE)

    driver.find_element_by_name('service').send_keys(express_service[i])

    Address = driver.find_element_by_id('pac-input')
    Address.send_keys(express_address[i])
    time.sleep(3)
    Address.send_keys(Keys.ARROW_DOWN)
    Address.send_keys(Keys.ENTER)
    time.sleep(1)
    driver.find_element_by_xpath("//button[contains(text(),'Next')]").click()

    MinQuantity = driver.find_element_by_name('min_order_quantity')
    MinQuantity.send_keys(str(minorderquantity[i]))

    MaxQuantity = driver.find_element_by_name('max_order_quantity')
    MaxQuantity.send_keys(str(maxorderquantity[i]))

    MinAmount = driver.find_element_by_name('min_order_amount')
    MinAmount.send_keys(str(minorderamount[i]))

    MaxAmount = driver.find_element_by_name('max_order_amount')
    MaxAmount.send_keys(str(maxorderamount[i]))

    driver.find_element_by_xpath("//button[@type='submit']").click()

