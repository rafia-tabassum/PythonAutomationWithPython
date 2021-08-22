import csv
import os
import random
import string
import time
import autoit
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pandas as pd


option1 = Options()
option1.add_argument("--disable-notifications")

csv_reader = pd.read_csv(r'merchant.csv')
total_row = csv_reader.shape[0]
merchant_name = csv_reader['MerchantName'].tolist()
type1 = csv_reader['Type'].tolist()
merchant_email = csv_reader['MerchantEmail'].tolist()
merchant_address = csv_reader['Address'].tolist()
owner_first_name = csv_reader['FirstName'].tolist()
owner_last_name = csv_reader['LastName'].tolist()
owner_email = csv_reader['OwnerEmail'].tolist()
owner_nid = csv_reader['OwnerNID'].tolist()
merchant_trade_license = csv_reader['MerchantTradeLicense'].tolist()
merchant_expirydate = csv_reader['ExpiryDate'].tolist()

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


for i in range(total_row):

    createmerchant = driver.find_element_by_xpath("//span[contains(text(),'Create Merchant')]")
    createmerchant.click()
    time.sleep(2)

    image = driver.find_element_by_xpath("//span[contains(text(),'Choose file')]")
    image.click()
    time.sleep(5)

    if i == 0:
        autoit.run("FileUpload2.exe")
    elif i == 1:
        autoit.run("FileUpload3.exe")
    time.sleep(2)
    uploadimage = driver.find_element_by_xpath("//button[contains(text(),'Upload Now')]")
    uploadimage.click()
    time.sleep(2)
    applycrop = driver.find_element_by_xpath("//span[contains(text(),'Apply Crop')]")
    applycrop.click()
    time.sleep(2)

    merchantname = driver.find_element_by_xpath("//input[@name='merchant_name']")
    merchantname.send_keys(merchant_name[i]+''.join(random.choice(string.digits) for _ in range(2)))
    time.sleep(2)

    type = driver.find_element_by_xpath("//select[@name='merchant_type']")
    # sel = Select(type)
    # if type == i:
    type.send_keys(type1[i])
    # elif i ==1:
    #     sel.select_by_index(1)
    time.sleep(2)

    cphonenumber = '019' + ''.join(random.choice(string.digits) for _ in range(8))
    companyphonenumber = driver.find_element_by_xpath("//input[@name='merchant_phone_no']")
    companyphonenumber.send_keys(cphonenumber)

    # email = ''.join(random.choice(string.digits) for _ in range(2))
    merchantemail= driver.find_element_by_xpath("//input[@name='merchant_email']")
    merchantemail.send_keys(merchant_email[i]+''.join(random.choice(string.digits) for _ in range(2))+ '@evaly.com.bd')

    merchantaddress = driver.find_element_by_xpath("//input[@name='merchant_address']")
    merchantaddress.send_keys(merchant_address[i])

    ownerfirstname = driver.find_element_by_xpath("//input[@name='owner_first_name']")
    ownerfirstname.send_keys(owner_first_name[i])

    ownerlastname = driver.find_element_by_xpath("//input[@name='owner_last_name']")
    ownerlastname.send_keys(owner_last_name[i])

    phonenumber = '019'+''.join(random.choice(string.digits) for _ in range(8))
    owner = driver.find_element_by_xpath("//input[@name='owner']")
    owner.send_keys(phonenumber)

    # email = 'owner' + ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(3)) + '@evaly.com.bd'
    owneremail = driver.find_element_by_xpath("//input[@name='owner_email']")
    owneremail.send_keys(owner_email[i])

    ownernid = driver.find_element_by_xpath("//input[@name='owner_nid_no']")
    ownernid.send_keys(owner_nid[i])

    merchanttradelicense = driver.find_element_by_xpath("//input[@name='merchant_trade_license_no']")
    merchanttradelicense.send_keys(merchant_trade_license[i])

    selectdate = driver.find_element_by_xpath("//input[@type='date']")
    selectdate.send_keys(merchant_expirydate[i])
    time.sleep(2)

    nidfrontimage = driver.find_element_by_xpath("//*[@id='__next']/section/div/div[2]/div/div/form/div/div[2]/div/div[8]/label/div/div")
    nidfrontimage.click()
    time.sleep(2)
    autoit.run("FileUpload4.exe")
    time.sleep(2)

    nidbackimage = driver.find_element_by_xpath("//*[@id='__next']/section/div/div[2]/div/div/form/div/div[2]/div/div[9]/label/div/div")
    nidbackimage.click()
    time.sleep(2)
    autoit.run("FileUpload5.exe")
    time.sleep(5)

    submitmerchant = driver.find_element_by_xpath("//button[@type='submit']")
    submitmerchant.click()
    time.sleep(5)

driver.close()