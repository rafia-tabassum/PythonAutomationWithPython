import math
import time

import pandas as pd
from selenium import webdriver
from selenium.common.exceptions import NoSuchFrameException, InvalidSelectorException
from selenium.webdriver.common.keys import Keys


login_admin_id = "ishak"
login_admin_password = "#121123!"

csv_reader = pd.read_csv(r"Bucketproducts.csv")
total_row = csv_reader.shape[0]  # total row in excel file

# product_name = csv_reader['Product_Name'].tolist()
manage_stock = csv_reader['In_stock'].tolist()
seller_price = csv_reader['Seller_Price'].tolist()
regular_price = csv_reader['Regular_Price'].tolist()
bucket_stock = csv_reader['Bucket_stock'].tolist()
bucket_seller_price = csv_reader['Bucket_Seller_Price'].tolist()
bucket_regular_price = csv_reader['Bucket_Regular_Price'].tolist()
discount_value = csv_reader['Discount_Value'].tolist()
discount_type = csv_reader['Discount_Type'].tolist()

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
driver.refresh()
time.sleep(2)
driver.find_element_by_xpath("//h4[text()='Shops']").click()
time.sleep(2)
driver.find_element_by_xpath("//li/a[contains(text(),'Campaign Shops')]").click()
time.sleep(3)
driver.find_element_by_xpath("//a[contains(text(),'Coffeekon for Automation ...')]").click()
time.sleep(3)
driver.find_element_by_id('primary-shop-product').click()
time.sleep(3)

for i in range(total_row):
    # productname = driver.find_element_by_xpath(
    #     "//div[@class='grid grid-cols-4 gap-4']").text
    # print(productname)
    # if productname == product_name[i]:
    #     driver.find_element_by_xpath("//button[@data-tip='Enlist to Bucket']").click()
    if i == 0:
        driver.find_element_by_xpath("//*[@id='__next']/section/div/div[2]/section/div/div/div[1]/div[3]/button[2]").click()
    elif i == 1:
        driver.find_element_by_xpath("//*[@id='__next']/section/div/div[2]/section/div/div/div[2]/div[3]/button[2]").click()
    if math.isnan(manage_stock[i]) == False:
        driver.find_element_by_name("manage_stock").click()
        Instock = driver.find_element_by_name("in_stock")
        Instock.click()
        Instock.send_keys(Keys.BACKSPACE)
        Instock.send_keys(str(manage_stock[i]))
        Instock.send_keys(Keys.BACKSPACE)
        Instock.send_keys(Keys.BACKSPACE)
        time.sleep(2)
    SellerPrice = driver.find_element_by_name("seller_price")
    SellerPrice.click()
    SellerPrice.send_keys(Keys.CONTROL, "a")
    SellerPrice.send_keys(seller_price[i])
    RegularPrice = driver.find_element_by_name("price")
    RegularPrice.click()
    RegularPrice.send_keys(Keys.CONTROL, "a")
    RegularPrice.send_keys(regular_price[i])
    driver.find_element_by_xpath("//button[@type='submit']").click()
    time.sleep(2)


for i in range(total_row):
    # if total_row == total_row:
    driver.find_element_by_id('bucket').click()
    time.sleep(2)
    # if i == 0:
    driver.find_element_by_xpath('//tr[1]/td[10]/div[1]/button').click()
    # elif i == 1:
    #     driver.find_element_by_xpath('//tr[2]/td[10]/div[1]/button').click()
    time.sleep(2)

    if math.isnan(manage_stock[i]) == False:
        driver.find_element_by_name("manage_stock").click()
        Instock = driver.find_element_by_name("in_stock")
        Instock.click()
        Instock.send_keys(Keys.BACKSPACE)
        Instock.send_keys(str(bucket_stock[i]))
        Instock.send_keys(Keys.BACKSPACE)
        Instock.send_keys(Keys.BACKSPACE)
        time.sleep(2)
    BucketSellerPrice = driver.find_element_by_name("seller_price")
    BucketSellerPrice.click()
    BucketSellerPrice.send_keys(Keys.CONTROL, "a")
    BucketSellerPrice.send_keys(bucket_seller_price[i])

    BucketRegularPrice = driver.find_element_by_name("price")
    BucketRegularPrice.click()
    BucketRegularPrice.send_keys(Keys.CONTROL, "a")
    BucketRegularPrice.send_keys(bucket_regular_price[i])

    if discount_type[i] == "Flat":
        driver.find_element_by_xpath("//input[@name='discount_type'][@value='flat']").click()
    DiscountValue = driver.find_element_by_name("discount_value")
    DiscountValue.click()
    DiscountValue.send_keys(Keys.CONTROL, "a")
    DiscountValue.send_keys(discount_value[i])
    time.sleep(2)

    driver.find_element_by_xpath("//button[@type='submit']").click()
    time.sleep(2)
    driver.find_element_by_id('primary-shop-product').click()
driver.close()