import random
import string
import time
import pyautogui
from selenium.webdriver.common.keys import Keys
from ExpressShopConfig import express_shop_config

primaryshop_name = "Dan Pound Cake"
merchant_name = "Pastry Merchant"
bin_number = 1287485678768
primaryshop_trade_license = 12345676543
category = "Fresh"
sbu_unit = "Evaly"
type = "medium"
primaryshop_address = "70 Shaheed Tajuddin Ahmed Ave, Dhaka 1212, Bangladesh"
keypersonname = "Rasiul"
bank_username = 'Hasan Akbar'

def create_primaryshop(driver):
    time.sleep(4)
    clickonshop = driver.find_element_by_xpath("/html/body/div[1]/section[1]/div/ul/li[3]/a/div")
    clickonshop.click()
    time.sleep(2)

    clickprimaryshop = driver.find_element_by_xpath("/html/body/div[1]/section[1]/div/ul/li[3]/ul/li[1]/a")
    clickprimaryshop.click()
    time.sleep(2)

    createprimaryshop = driver.find_element_by_xpath("//span[contains(text(),'Create Primary Shop')]")
    createprimaryshop.click()
    time.sleep(2)

    image = driver.find_element_by_xpath("//span[contains(text(),'Choose file')]")
    image.click()
    time.sleep(2)
    pyautogui.write(r"C:\Users\ASUS\Downloads\1.jpg")
    pyautogui.press('enter')
    time.sleep(2)
    uploadimage = driver.find_element_by_xpath("//button[contains(text(),'Upload Now')]")
    uploadimage.click()
    time.sleep(2)
    applycrop = driver.find_element_by_xpath("//span[contains(text(),'Apply Crop')]")
    applycrop.click()
    time.sleep(2)

    uploadbanner = driver.find_element_by_xpath("//*[@id='drop-area_image']/label")
    uploadbanner.click()
    time.sleep(3)
    pyautogui.write(r"C:\Users\ASUS\Downloads\bannerimage.jpg")
    pyautogui.press('enter')
    time.sleep(2)

    driver.find_element_by_name('name').send_keys(primaryshop_name+ ''.join(random.choice(string.digits) for _ in range(2)))
    driver.find_element_by_name('bin_no').send_keys(bin_number)
    # driver.find_element_by_name('trade_license_no').send_keys(primaryshop_trade_license)
    driver.find_element_by_name('category').send_keys(category)
    driver.find_element_by_name('sbu_unit').send_keys(sbu_unit)

    Score = driver.find_element_by_name('score')
    Score.click()
    Score.send_keys(Keys.ARROW_RIGHT)
    Score.send_keys(Keys.BACKSPACE)
    time.sleep(1)
    Score.send_keys(''.join(random.choice(string.digits) for _ in range(4)))

    driver.find_element_by_name('seller_type').send_keys(type)
    driver.find_element_by_name('merchant_name').send_keys(merchant_name)
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[1]/section[2]/div[2]/div/div[2]/form/div/div[1]/div[1]/div[11]/label/div/div/ul/div').click()


    Address = driver.find_element_by_id('pac-input')
    Address.send_keys(primaryshop_address)
    time.sleep(3)
    Address.send_keys(Keys.ARROW_DOWN)
    Address.send_keys(Keys.ENTER)
    time.sleep(1)

    KeyPersonName = driver.find_element_by_name('key_personnel.0.username')
    KeyPersonName.send_keys(keypersonname+''.join(random.choice(string.digits) for _ in range(2)))

    KeyPersonDesignation = driver.find_element_by_name('key_personnel.0.designation')
    KeyPersonDesignation.send_keys("Seller")

    KeyPersonPhoneNumber = driver.find_element_by_name('key_personnel.0.phone_no')
    KeyPersonPhoneNumber.send_keys('019'+''.join(random.choice(string.digits) for _ in range(8)))

    KeyPersonEmail = driver.find_element_by_name('key_personnel.0.email')
    KeyPersonEmail.send_keys('keyperson'+ ''.join(random.choice(string.digits) for _ in range(2)) + '@evaly.com.bd')

    driver.find_element_by_xpath("//button[contains(text(),'Next')]").click()
    time.sleep(3)

    driver.find_element_by_name('bank_info.0.bank_name').send_keys("City Bank Limited")
    driver.find_element_by_name('bank_info.0.bank_branch_name').send_keys("Dhanmondi- 32")
    driver.find_element_by_name('bank_info.0.bank_account_name').send_keys(bank_username)
    driver.find_element_by_name('bank_info.0.bank_account_no').send_keys(''.join(random.choice(string.digits) for _ in range(9)))
    driver.find_element_by_name('bank_info.0.bank_branch_routing_no').send_keys(''.join(random.choice(string.digits) for _ in range(6)))

    kam_name = driver.find_element_by_xpath("/html/body/div[1]/section[2]/div[2]/div/div[2]/form/div/div[2]/div[1]/div[1]/div[1]/label/div/label/input")
    kam_name.send_keys("wase")
    time.sleep(2)
    kam_list= driver.find_element_by_xpath("//li[@class='cursor-pointer border-b p-2 px-4']")
    kam_list.click()
    time.sleep(1)
    driver.find_element_by_name('kam.0.phone_no').send_keys('019'+''.join(random.choice(string.digits) for _ in range(8)))

    bdm_name = driver.find_element_by_xpath('/html/body/div[1]/section[2]/div[2]/div/div[2]/form/div/div[2]/div[2]/div[1]/div[1]/label/div/label/input')
    bdm_name.send_keys("tami")
    time.sleep(2)
    bdm_list = driver.find_element_by_id("110126276")
    bdm_list.click()
    time.sleep(1)
    driver.find_element_by_name('bdm.0.phone_no').send_keys(
        '019' + ''.join(random.choice(string.digits) for _ in range(8)))

    cat_head = driver.find_element_by_xpath(
        '/html/body/div[1]/section[2]/div[2]/div/div[2]/form/div/div[2]/div[3]/div[1]/div[1]/label/div/label/input')
    cat_head.send_keys('nabil')
    time.sleep(2)
    cat_head_list = driver.find_element_by_id('-1053155281')
    cat_head_list.click()
    time.sleep(1)
    driver.find_element_by_name('category_head.0.phone_no').send_keys(
        '019' + ''.join(random.choice(string.digits) for _ in range(8)))

    vm_name = driver.find_element_by_xpath('/html/body/div[1]/section[2]/div[2]/div/div[2]/form/div/div[2]/div[4]/div[1]/div[1]/label/div/label/input')
    vm_name.send_keys("ikra")
    time.sleep(2)
    vm_list = driver.find_element_by_id('100270012')
    vm_list.click()
    driver.find_element_by_name('vm.0.phone_no').send_keys(
        '019' + ''.join(random.choice(string.digits) for _ in range(8)))
    driver.find_element_by_xpath("//button[contains(text(),'Next')]").click()



    driver.find_element_by_name('acquisition.0.acquisition_by').send_keys(bank_username)
    driver.find_element_by_name('acquisition.0.acquisition_phone_no').send_keys('019'+''.join(random.choice(string.digits) for _ in range(8)))
    driver.find_element_by_name('acquisition.0.acquisition_email').send_keys('acquis'+ ''.join(random.choice(string.digits) for _ in range(2)) + '@evaly.com.bd')
    driver.find_element_by_name('acquisition.0.acquisition_date').send_keys("09/30/2021")

    driver.find_element_by_name('agreement_info.0.agreement_expiry_date').send_keys("09/30/2021")

    driver.find_element_by_id("fileName").click()
    time.sleep(2)
    pyautogui.write(r"C:\Users\ASUS\Downloads\bannerimage.jpg")
    pyautogui.press('enter')
    time.sleep(2)

    driver.find_element_by_name('agreement_info.0.credit_limit').send_keys("1000000")
    driver.find_element_by_name('agreement_info.0.credit_time').send_keys("30")

    driver.find_element_by_xpath("//button[contains(text(),'Set Config')]").click()
    express_shop_config(driver)
    driver.find_element_by_xpath("//button[contains(text(),'Preview')]").click()
    driver.find_element_by_xpath("//button//span[contains(text(),'Create Shop')]").click()




