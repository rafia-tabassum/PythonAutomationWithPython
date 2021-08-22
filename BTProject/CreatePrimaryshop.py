import random
import string
import time
from telnetlib import EC

import autoit
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

option1 = Options()
option1.add_argument("--disable-notifications")

csv_reader = pd.read_csv(r'primaryshopinfo.csv')
total_row = csv_reader.shape[0]
bin_number = csv_reader['BIN_Number'].tolist()
primaryshopname = csv_reader['PrimaryshopName'].tolist()
primaryshoptradelicense = csv_reader['Primaryshop_Trade_License'].tolist()
primaryshoptradeexpirydate = csv_reader['Primaryshop_Trade_License_ExpiryDate'].tolist()
primaryshopcategory = csv_reader['PrimaryshopCategory'].tolist()
sbuname = csv_reader['SBUName'].tolist()
score = csv_reader['Score'].tolist()
primaryshopsellertype = csv_reader['PrimaryshopSellerType'].tolist()
merchant = csv_reader['Merchant'].tolist()
merchantaddress = csv_reader['Address'].tolist()
keypersonname = csv_reader['KeyPersonName'].tolist()
keypersondesignation = csv_reader['KeyPersonDesignation'].tolist()
keypersonphonenumber = csv_reader['KeyPersonPhoneNumber'].tolist()
keypersonemail = csv_reader['KeypersonEmail'].tolist()
bankname = csv_reader['BankName'].tolist()
branchname = csv_reader['BranchName'].tolist()
accountname = csv_reader['AccountName'].tolist()
accountnumber = csv_reader['AccountNumber'].tolist()
routingnumber = csv_reader['RoutingNumber'].tolist()
categoryheadname = csv_reader['CategoryheadName'].tolist()
categoryheadphnnumber = csv_reader['CategoryHeadPhoneNumber'].tolist()
kamname = csv_reader['KAMName'].tolist()
kamphnnumber = csv_reader['KAMPhoneNumber'].tolist()
bdmname = csv_reader['BDMName'].tolist()
bdmphnnumber = csv_reader['BDMPhonenumber'].tolist()
vmname = csv_reader['VMName'].tolist()
vmphnnumber = csv_reader['VMPhoneNUmber'].tolist()
acquisitionname = csv_reader['AcquisitionByName'].tolist()
acquisitionphnnumber = csv_reader['AcquisitionPhonenumber'].tolist()
acquisitionemail = csv_reader['AcquisitionEmail'].tolist()
acquisitiondate = csv_reader['AcquisitionDate'].tolist()
agreementexpirydate = csv_reader['AgreementExpiryDate'].tolist()
creditlimit = csv_reader['CreditLimit'].tolist()
credittime = csv_reader['CreditTime'].tolist()


driver = webdriver.Chrome(executable_path="E:\Pythonproj\chromedriver.exe", options=option1)
driver.get("https://beta-erp.evaly.com.bd/auth/login")
driver.maximize_window()

Userid = driver.find_element_by_xpath("//input[@placeholder='Username']")
Userid.send_keys("ishak")

Password = driver.find_element_by_xpath("//input[@placeholder='Password']")
Password.send_keys("#121123!")

Loginbtn = driver.find_element_by_xpath("//span[contains(text(), 'Log In')]")
Loginbtn.click()
time.sleep(4)

# sidemenu = driver.find_element_by_xpath("//*[@id='__next']/div[1]/div[1]/button")
# sidemenu.click()
# time.sleep(2)

clickonshop = driver.find_element_by_xpath("//*[@id='__next']/section/section/div/ul/li[3]/a")
clickonshop.click()
time.sleep(2)

clickprimaryshop = driver.find_element_by_xpath("//*[@id='__next']/section/section/div/ul/li[3]/ul/li[1]/a")
clickprimaryshop.click()
time.sleep(2)


for i in range(total_row):


    createprimaryshop = driver.find_element_by_xpath("//span[contains(text(),'Create Primary Shop')]")
    createprimaryshop.click()
    time.sleep(2)

    image = driver.find_element_by_xpath("//span[contains(text(),'Choose file')]")
    image.click()
    time.sleep(5)

    if i == 0:
        autoit.run("E:\Pythonproj\BTProject\primaryshoplogo\FileUpload.exe")
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
    time.sleep(5)
    BINNumber = driver.find_element_by_xpath("//input[@name='bin_no']")
    BINNumber.send_keys(bin_number[i])

    primaryShopName = driver.find_element_by_name('name')
    primaryShopName.send_keys(primaryshopname[i]+''.join(random.choice(string.digits) for _ in range(2)))
    time.sleep(2)

    PrimaryShopTradeLicense = driver.find_element_by_xpath("//*[@id='__next']/section/div/div[2]/form/div/div[1]/div[1]/div[4]/label/input")
    PrimaryShopTradeLicense.send_keys(primaryshoptradelicense[i])

    PrimaryShopTradeExpiryDate = driver.find_element_by_xpath("//input[@type='date']")
    PrimaryShopTradeExpiryDate.send_keys(primaryshoptradeexpirydate[i])
    time.sleep(3)

    PrimaryShopCategory = driver.find_element_by_xpath("//select[@name='category']")
    PrimaryShopCategory.send_keys(primaryshopcategory[i])

    SbuName = driver.find_element_by_xpath("//select[@name='sbu_unit']")
    SbuName.send_keys(sbuname[i])

    Score = driver.find_element_by_xpath("//input[@name='score']")
    Score.click()
    Score.send_keys(Keys.BACKSPACE)
    time.sleep(2)
    Score.send_keys(score[i])

    PrimaryShopSellerType = driver.find_element_by_xpath("//select[@name='seller_type']")
    PrimaryShopSellerType.send_keys(primaryshopsellertype[i])

    MerchantName = driver.find_element_by_xpath("//input[@name='merchant_code']")
    MerchantName.send_keys(merchant[i])
    time.sleep(4)
    # MerchantSelect = driver.find_element_by_xpath("//*[@id='662628982']")
    MerchantSelect = driver.find_element_by_xpath("//*[@id='listbox--1']/div[1]")
    MerchantSelect.click()
    time.sleep(1)

    Address = driver.find_element_by_id('pac-input')
    Address.send_keys(merchantaddress[i])
    time.sleep(3)
    Address.send_keys(Keys.ARROW_DOWN)
    Address.send_keys(Keys.ENTER)

    # KeyPersonName = driver.find_element_by_name('key_personnel.0.name')
    # KeyPersonName.send_keys(keypersonname[i]+''.join(random.choice(string.digits) for _ in range(2)))
    #
    # KeyPersonDesignation = driver.find_element_by_name('key_personnel.0.designation')
    # KeyPersonDesignation.send_keys(keypersondesignation[i])
    #
    # KeyPersonPhoneNumber = driver.find_element_by_name('key_personnel.0.phone_no')
    # KeyPersonPhoneNumber.send_keys(str(keypersonphonenumber[i]).zfill(11))
    #
    # KeyPersonEmail = driver.find_element_by_name('key_personnel.0.email')
    # KeyPersonEmail.send_keys(keypersonemail[i])
    # time.sleep(4)

    # addnewkam = driver.find_element_by_xpath("//button[contains(text(),'Add Another')]")
    # addnewkam.click()
    # time.sleep(3)
    #
    # KeyPersonName1 = driver.find_element_by_name('key_personnel.1.name')
    # KeyPersonName1.send_keys(keypersonname[i]+''.join(random.choice(string.digits) for _ in range(2)))
    #
    # KeyPersonDesignation1 = driver.find_element_by_name('key_personnel.1.designation')
    # KeyPersonDesignation1.send_keys(keypersondesignation[i])
    #
    # KeyPersonPhoneNumber1 = driver.find_element_by_name('key_personnel.1.phone_no')
    # KeyPersonPhoneNumber1.send_keys(str(keypersonphonenumber[i]).zfill(11))
    #
    # KeyPersonEmail1 = driver.find_element_by_name('key_personnel.1.email')
    # KeyPersonEmail1.send_keys(keypersonemail[i])
    # time.sleep(4)

    NextButton = driver.find_element_by_xpath("//button[@type='submit']")
    NextButton.click()
    time.sleep(2)

    # BankName = driver.find_element_by_name('bank_info.0.bank_name')
    # BankName.send_keys(bankname[i])
    #
    # BranchName = driver.find_element_by_name('bank_info.0.bank_branch_name')
    # BranchName.send_keys(branchname[i])
    #
    # AccountName = driver.find_element_by_name('bank_info.0.bank_account_name')
    # AccountName.send_keys(accountname[i])
    #
    # AccountNumber = driver.find_element_by_name('bank_info.0.bank_account_no')
    # AccountNumber.send_keys(accountnumber[i])
    #
    # RoutingNumber = driver.find_element_by_name('bank_info.0.bank_branch_routing_no')
    # RoutingNumber.send_keys(routingnumber[i])

    # KamName = driver.find_element_by_xpath('//*[@id="__next"]/section/div/div[2]/form/div/div[2]/div[1]/div/div[1]/label/div/label/input')
    # KamName.send_keys(kamname[i])
    # time.sleep(3)
    # KamName.send_keys(Keys.ARROW_DOWN)
    # time.sleep(2)
    # KamName.click()
    #
    # # KamName.send_keys(Keys.ENTER)
    # # time.sleep(3)
    # KamNameSelect = driver.find_element_by_xpath("//div/div[1]/div/div[1]/label/div/div/ul")
    # KamNameSelect.click()
    # time.sleep(2)
    #
    # KamPhoneNumber = driver.find_element_by_name('kam.0.phone')
    # KamPhoneNumber.send_keys(str(kamphnnumber[i]).zfill(11))
    #
    #
    # BDMName = driver.find_element_by_xpath('//*[@id="__next"]/section/div/div[2]/form/div/div[2]/div[2]/div/div[1]/label/div/label/input')
    # BDMName.send_keys(bdmname[i])
    # time.sleep(3)
    # BDMName.send_keys(Keys.ARROW_DOWN)
    # time.sleep(2)
    # BDMName.send_keys(Keys.ENTER)
    # # time.sleep(3)
    # # BDMNameSelect = driver.find_element_by_xpath("//*[@id='listbox--250']/div/div")
    # # BDMNameSelect.click()
    # time.sleep(2)
    #
    # BDMPhoneNumber = driver.find_element_by_name('bdm.0.phone')
    # BDMPhoneNumber.send_keys(str(bdmphnnumber[i]).zfill(11))
    #
    # CategoryHeadName = driver.find_element_by_xpath("//*[@id='__next']/section/div/div[2]/form/div/div[2]/div[3]/div/div[1]/label/div/label/input")
    # CategoryHeadName.send_keys(categoryheadname[i])
    # time.sleep(3)
    # # CategoryHeadNameSelect = driver.find_element_by_xpath("//*[@id='listbox--689']/div/div[1]")
    # # CategoryHeadNameSelect.click()
    # # time.sleep(2)
    # CategoryHeadName.send_keys(Keys.ARROW_DOWN)
    # time.sleep(2)
    # CategoryHeadName.click()
    # time.sleep(2)
    #
    # CategoryHeadPhnNumber = driver.find_element_by_name('category_head.0.phone')
    # CategoryHeadPhnNumber.send_keys(str(categoryheadphnnumber[i]).zfill(11))
    # # addnew = driver.find_element_by_xpath("//*[@id='__next']/section/div/div[2]/form/div/div[2]/div[3]/button")
    # # addnew.click()
    # # time.sleep(3)
    #
    # VMName = driver.find_element_by_xpath("//*[@id='__next']/section/div/div[2]/form/div/div[2]/div[4]/div/div[1]/label/div/label/input")
    # VMName.send_keys(vmname[i])
    # time.sleep(3)
    # VMName.send_keys(Keys.ARROW_DOWN)
    # time.sleep(2)
    # VMName.send_keys(Keys.ENTER)
    # # time.sleep(3)
    # # VMNameSelect = driver.find_element_by_xpath("//*[@id='listbox--415']/div/div")
    # # VMNameSelect.click()
    # # time.sleep(2)
    #
    # VMPhoneNumber = driver.find_element_by_name('vm.0.phone')
    # VMPhoneNumber.send_keys(str(vmphnnumber[i]).zfill(11))

    NextBtn = driver.find_element_by_xpath("//button[contains(text(),'Next')]")
    NextBtn.click()
    time.sleep(2)

    AcquisitionName = driver.find_element_by_name('acquisition.0.acquisition_by_name')
    AcquisitionName.send_keys(acquisitionname[i])

    AcquisitionPhoneNumber = driver.find_element_by_name('acquisition.0.acquisition_by')
    AcquisitionPhoneNumber.send_keys(acquisitionphnnumber[i])

    AcquisitionEmail = driver.find_element_by_name('acquisition.0.acquisition_by_email')
    AcquisitionEmail.send_keys(acquisitionemail[i])

    AcquisitionDate = driver.find_element_by_name('acquisition.0.acquisition_date')
    AcquisitionDate.send_keys(acquisitiondate[i])

    AgreementExpiryDate = driver.find_element_by_name('agreement_info.0.agreement_expiry_date')
    AgreementExpiryDate.send_keys(agreementexpirydate[i])

    AgreementScanCopy = driver.find_element_by_id("fileName")
    AgreementScanCopy.click()
    time.sleep(2)
    autoit.run("E:\Pythonproj\BTProject\primaryshoplogo\FileUpload4.exe")
    time.sleep(2)

    CreditLimit = driver.find_element_by_name('agreement_info.0.credit_limit')
    CreditLimit.send_keys(creditlimit[i])

    CreditTime = driver.find_element_by_name('agreement_info.0.credit_time')
    CreditTime.send_keys(credittime[i])

    submit = driver.find_element_by_xpath("//button[contains(text(),'Preview & Sumbit')]")
    submit.click()
    time.sleep(4)

    CreateShop = driver.find_element_by_xpath("//button[contains(text(),'Create Shop')]")
    CreateShop.click()
    time.sleep(2)

    # primaryshopclick = driver.find_element_by_xpath("//*[@id='__next']/section/div/div[1]/div/nav/ul/li[7]/a")
    # primaryshopclick.click()
    time.sleep(4)
driver.close()