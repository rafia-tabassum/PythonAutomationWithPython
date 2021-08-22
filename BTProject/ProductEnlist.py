import math
from selenium import webdriver
import random
import time
import pandas as pd
from selenium.common.exceptions import NoSuchFrameException, InvalidSelectorException, WebDriverException, \
    ElementClickInterceptedException, NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.common.keys import Keys

login_admin_id = "ishak"
login_admin_password = "#121123!"

csv_reader = pd.read_csv(r"Products.csv")
total_row = csv_reader.shape[0]  # total row in excel file
product_id = csv_reader['ID'].tolist()
print(product_id)
product_name = csv_reader['Item_Name'].tolist()  # store user id in this variable
print(product_name)
random_number = random.randint(1000, 12000)

manage_stock = csv_reader['In_stock'].tolist()
# print(str(manage_stock))
minimum_wholesale_quantity = csv_reader['Minimum_Wholesale_Quantity'].tolist()
wholesale_price = csv_reader['wholesale_Price'].tolist()
seller_price = csv_reader['Seller_Price'].tolist()
regular_price = csv_reader['Regular_Price'].tolist()
discount_value = csv_reader['Discount_value'].tolist()
discount_type = csv_reader['Discount_Type'].tolist()


driver = webdriver.Chrome(executable_path="E:\Pythonproj\chromedriver.exe") # Driver location
driver.maximize_window()


def admin_login(driver):
    try:
        driver.get("https://beta-erp.evaly.com.bd/")  # access web url
        time.sleep(1)
        driver.find_element_by_xpath("//input[@placeholder='Username']").send_keys(login_admin_id)  # click user name input field
        time.sleep(1)
        driver.find_element_by_xpath("//input[@placeholder='Password']").send_keys(login_admin_password)  # write password
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
time.sleep(3)

for i in range(total_row):
    try:
        time.sleep(3)
        driver.find_element_by_xpath("//input[@placeholder='Search....']").send_keys(product_name[i], Keys.ENTER)
        time.sleep(7)
        driver.find_element_by_xpath("/html/body/div[1]/section/div/section/div/table/tbody/tr/td[10]/button").click()
        time.sleep(2)
        # Enlist Products
        if math.isnan(manage_stock[i]) == False:
            driver.find_element_by_name("manage_stock").click()
            Instock = driver.find_element_by_name("in_stock")
            Instock.click()
            Instock.send_keys(Keys.BACKSPACE)
            Instock.send_keys(str(manage_stock[i]))
            Instock.send_keys(Keys.BACKSPACE)
            Instock.send_keys(Keys.BACKSPACE)
            time.sleep(2)
        driver.find_element_by_name("minimum_wholesale_quantity").send_keys(minimum_wholesale_quantity[i])
        driver.find_element_by_name("wholesale_price").send_keys(wholesale_price[i])
        driver.find_element_by_xpath(
            "/html/body/reach-portal/div/div/div/section[2]/div/form/div/div/div[1]/div[1]/div[4]/label/input").click()  # check box product item
        driver.find_element_by_name("seller_price").send_keys(seller_price[i])
        driver.find_element_by_name("price").send_keys(regular_price[i])
        if math.isnan(discount_value[i]) == False:
            driver.find_element_by_name("is_discount_enabled").click()
            driver.find_element_by_name("discount_value").send_keys(discount_value[i])
            if discount_type[i]=="Percentage":
                driver.find_element_by_xpath("//input[@name='discount_type'][@value='percentage']").click()
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
driver.close()