import csv
import random
import string
import time
import autoit
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select

option1 = Options()
option1.add_argument("--disable-notifications")
with open('merchant.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

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


    for i, line in enumerate(csv_reader):

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
        merchantname.send_keys(line[0]+''.join(random.choice(string.digits) for _ in range(2)))
        time.sleep(2)

        type = driver.find_element_by_xpath("//select[@name='merchant_type']")
        sel = Select(type)
        if i == 0:
            sel.select_by_index(2)
        elif i ==1:
            sel.select_by_index(1)
        time.sleep(2)

        cphonenumber = '019' + ''.join(random.choice(string.digits) for _ in range(8))
        companyphonenumber = driver.find_element_by_xpath("//input[@name='merchant_phone_no']")
        companyphonenumber.send_keys(cphonenumber)

        email = 'merchant' + ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(3)) + '@evaly.com.bd'
        merchantemail= driver.find_element_by_xpath("//input[@name='merchant_email']")
        merchantemail.send_keys(email)

        merchantaddress = driver.find_element_by_xpath("//input[@name='merchant_address']")
        merchantaddress.send_keys(line[1])

        ownerfirstname = driver.find_element_by_xpath("//input[@name='owner_first_name']")
        ownerfirstname.send_keys(line[2])

        ownerlastname = driver.find_element_by_xpath("//input[@name='owner_last_name']")
        ownerlastname.send_keys(line[3])

        phonenumber = '019'+''.join(random.choice(string.digits) for _ in range(8))
        owner = driver.find_element_by_xpath("//input[@name='owner']")
        owner.send_keys(phonenumber)

        email = 'owner' + ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(3)) + '@evaly.com.bd'
        owneremail = driver.find_element_by_xpath("//input[@name='owner_email']")
        owneremail.send_keys(email)

        ownernid = driver.find_element_by_xpath("//input[@name='owner_nid_no']")
        ownernid.send_keys(line[4])

        merchanttradelicense = driver.find_element_by_xpath("//input[@name='merchant_trade_license_no']")
        merchanttradelicense.send_keys(line[5])

        selectdate = driver.find_element_by_xpath("//input[@type='date']")
        selectdate.send_keys(line[6])
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