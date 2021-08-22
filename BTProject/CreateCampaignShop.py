import random
import string
import time
import pandas as pd
from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException, InvalidSelectorException, \
    NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

option1 = Options()
option1.add_argument("--disable-notifications")

csv_reader = pd.read_csv(r'campaign.csv')
total_row = csv_reader.shape[0]
campaign_name = csv_reader['Campaign_Name'].tolist()  # store user id in this variable
print(campaign_name)

minorderquantity = csv_reader['Min_Order_Quantity'].tolist()
minorderamount = csv_reader['Min_Order_Amount'].tolist()
maxorderquantity = csv_reader['Max_Order_Quantity'].tolist()
maxorderamount = csv_reader['Max_Order_Amount'].tolist()


driver = webdriver.Chrome(executable_path="E:\Pythonproj\chromedriver.exe", options=option1)
driver.get("https://beta-erp.evaly.com.bd/auth/login")
driver.maximize_window()

Userid = driver.find_element_by_xpath("//input[@placeholder='Username']")
Userid.send_keys("ishak")

Password = driver.find_element_by_xpath("//input[@placeholder='Password']")
Password.send_keys("#121123!")

Loginbtn = driver.find_element_by_xpath("//span[contains(text(), 'Log In')]")
Loginbtn.click()
time.sleep(3)

clickonshop = driver.find_element_by_xpath("//*[@id='__next']/section/section/div/ul/li[3]/a")
clickonshop.click()
time.sleep(2)

clickprimaryshop = driver.find_element_by_xpath("//*[@id='__next']/section/section/div/ul/li[3]/ul/li[1]/a")
clickprimaryshop.click()
time.sleep(2)

AddtoCampaign = driver.find_element_by_xpath("//*[@id='__next']/section/div/section/div/div/table/tbody/tr[1]/td[9]/button[1]")
AddtoCampaign.click()
time.sleep(3)

# SelectCampaign = driver.find_element_by_xpath("/html/body/reach-portal/div/div/div/section[2]/section/table/tbody/tr[1]")
# SelectCampaign.click()
for i in range(total_row):
    try:
        time.sleep(3)
        driver.find_element_by_xpath("//input[@class='CampaignInlineSearchFilter___StyledInput-sc-3s2soe-0 icKzGq form-input w-full']").send_keys(campaign_name[i], Keys.ENTER)
        time.sleep(7)
        driver.find_element_by_xpath("//tbody/tr/td[@class='p-2']/a").click()
        time.sleep(2)

        MinOrderQuantity = driver.find_element_by_xpath("//input[@name='min_order_quantity']")
        MinOrderQuantity.click()
        MinOrderQuantity.send_keys(Keys.BACKSPACE)
        # time.sleep(2)
        MinOrderQuantity.send_keys(str(minorderquantity[i]))

        MaxOrderQuantity = driver.find_element_by_xpath("//input[@name='max_order_quantity']")
        MaxOrderQuantity.click()
        MaxOrderQuantity.send_keys(Keys.BACKSPACE)
        MaxOrderQuantity.send_keys(str(maxorderquantity[i]))

        MinOrderAmount = driver.find_element_by_xpath("//input[@name='min_order_amount']")
        MinOrderAmount.click()
        MinOrderAmount.send_keys(Keys.BACKSPACE)
        # time.sleep(2)
        MinOrderAmount.send_keys(str(minorderamount[i]))

        MaxOrderAmount = driver.find_element_by_xpath("//input[@name='max_order_amount']")
        MaxOrderAmount.click()
        MaxOrderAmount.send_keys(Keys.BACKSPACE)
        # time.sleep(2)
        MaxOrderAmount.send_keys(str(maxorderamount[i]))

        Submit = driver.find_element_by_xpath("//span[contains(text(), 'Submit')]")
        Submit.click()
    except(
            ElementClickInterceptedException, InvalidSelectorException, NoSuchElementException,
            StaleElementReferenceException):
        print("Exception occur")
    try:
        searchBox = driver.find_element_by_xpath("//input[@class='CampaignInlineSearchFilter___StyledInput-sc-3s2soe-0 icKzGq form-input w-full']")
        for i in range(len(campaign_name[i])):
            searchBox.click()
            searchBox.send_keys(Keys.BACK_SPACE)
            searchBox.send_keys(Keys.ENTER)
            time.sleep(3)
    except(
        ElementClickInterceptedException, InvalidSelectorException, NoSuchElementException,
        StaleElementReferenceException):
        print("Exception occur")