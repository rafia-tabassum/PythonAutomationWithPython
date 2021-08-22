import math

import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

option1 = Options()
option1.add_argument("--disable-notifications")
csv_reader = pd.read_csv(r'enlistproduct.csv')
total_row = csv_reader.shape[0]

instock = csv_reader['In_stock'].tolist()
minimumwholesalequantity = csv_reader['Minimum_Wholesale_Quantity'].tolist()
wholesaleprice = csv_reader['wholesale_Price'].tolist()
sellerprice = csv_reader['Seller_Price'].tolist()
regularprice = csv_reader['Regular_Price'].tolist()
discountvalue = csv_reader['Discount_value'].tolist()
discounttype = csv_reader['Discount_Type'].tolist()


driver = webdriver.Chrome(executable_path="E:\Pythonproj\chromedriver.exe", options=option1)
driver.get("https://beta-erp.evaly.com.bd/auth/login")
driver.maximize_window()
driver.implicitly_wait(10)
Userid = driver.find_element_by_xpath("//input[@placeholder='Username']")
Userid.send_keys("ishak")

Password = driver.find_element_by_xpath("//input[@placeholder='Password']")
Password.send_keys("#121123!")

Loginbtn = driver.find_element_by_xpath("//span[contains(text(), 'Log In')]")
Loginbtn.click()
# time.sleep(3)

clickonshop = driver.find_element_by_xpath("//*[@id='__next']/section/section/div/ul/li[3]/a")
# clickonshop = wait.until(EC.visibility_of_element_located(By.XPATH, "//*[@id='__next']/section/section/div/ul/li[3]/a"))
clickonshop.click()
# time.sleep(2)

clickprimaryshop = driver.find_element_by_xpath("//*[@id='__next']/section/section/div/ul/li[3]/ul/li[1]/a")
clickprimaryshop.click()
# time.sleep(2)

clickprimaryshopname = driver.find_element_by_xpath("//*[@id='__next']/section/div/section/div/div/table/tbody/tr[1]/td[3]")
clickprimaryshopname.click()
# time.sleep(3)

primaryshopproducts = driver.find_element_by_xpath("//button[contains(text(),'Primaryshop Products')]")
primaryshopproducts.click()

EnlistProduct = driver.find_element_by_xpath("//button/span[contains(text(),'Enlist Product')]")
EnlistProduct.click()
# time.sleep(2)
for i in range(total_row):


    # if i == 0:
    enlistbtn = driver.find_element_by_xpath("//tbody/tr[3]/td/button[@data-tip='Enlist']")
    enlistbtn.click()
    # else:
    # # time.sleep(5)
    # # page = driver.find_element_by_xpath("//*[@id='__next']/section/div/section/div/table/tbody")
    # # print(page.text)
    #     enlistbtn = driver.find_element_by_xpath("//tbody/tr[3]/td/button[@data-tip='Enlist']")
    #     enlistbtn.click()
    if math.isnan(instock[i])== False:

        ManageStock = driver.find_element_by_xpath("//input[@name='manage_stock']")
        ManageStock.click()

        InStock = driver.find_element_by_xpath("//input[@name='in_stock']")
        InStock.click()
        # time.sleep(1)
        InStock.send_keys(Keys.BACKSPACE)
        InStock.send_keys(instock[i])

    MinWholeSaleQuantity = driver.find_element_by_xpath("//input[@name='minimum_wholesale_quantity']")
    MinWholeSaleQuantity.send_keys(minimumwholesalequantity[i])

    WholeSalePrice = driver.find_element_by_xpath("//input[@name='wholesale_price']")
    WholeSalePrice.send_keys(wholesaleprice[i])

    SelectVariant = driver.find_element_by_xpath("/html/body/reach-portal/div/div/div/section[2]/div/form/div/div/div[1]/div[1]/div[4]/label/input")
    SelectVariant.click()

    SellerPrice = driver.find_element_by_xpath("//input[@name='seller_price']")
    SellerPrice.send_keys(sellerprice[i])
#
    RegularPrice = driver.find_element_by_xpath("//input[@name='price']")
    RegularPrice.send_keys(regularprice[i])

    if math.isnan(discountvalue[i]) == False:
        EnableDiscount = driver.find_element_by_xpath("//input[@name='is_discount_enabled']")
        EnableDiscount.click()

        DiscountValue = driver.find_element_by_xpath("//input[@name='discount_value']")
        DiscountValue.send_keys(discountvalue[i])

        if discounttype[i] =="Percentage":
            DiscountType = driver.find_element_by_xpath("/html/body/reach-portal/div/div/div/section[2]/div/form/div/div/div[1]/div[2]/div[3]/div[1]/div/label[2]/input")
            DiscountType.click()


    Submit = driver.find_element_by_xpath("//span[contains(text(), 'Submit')]")
    Submit.click()