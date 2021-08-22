import random
import string
import time
import pyautogui
from selenium.webdriver.common.keys import Keys
from ExpressShopConfig import express_shop_config

express_name = "Dan Pound Cake31 Express"
primaryshop_name = "Dan Pound Cake31"
score = 100
commission = 50
express_service = "CashValy"
express_address = "68 Shaheed Tajuddin Ahmed Ave, Dhaka 1212, Bangladesh"

def create_express_shop(driver):
    time.sleep(4)
    clickonshop = driver.find_element_by_xpath("/html/body/div[1]/section[1]/div/ul/li[3]/a/div")
    clickonshop.click()
    time.sleep(2)



    driver.find_element_by_xpath("//li/a[contains(text(),'Express Shops')]").click()
    time.sleep(2)

    driver.find_element_by_xpath("//button/span[contains(text(),'Create Express Shops')]").click()
    time.sleep(2)

    image = driver.find_element_by_xpath("//span[contains(text(),'Choose file')]")
    image.click()
    time.sleep(2)
    pyautogui.write(r"C:\Users\ASUS\Downloads\express.jpg")
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
    pyautogui.write(r"C:\Users\ASUS\Downloads\express.jpg")
    pyautogui.press('enter')
    time.sleep(2)

    expressname = driver.find_element_by_name('name')
    expressname.send_keys(express_name+ ''.join(random.choice(string.digits) for _ in range(2)))

    driver.find_element_by_name('mother_shop_slug').send_keys(primaryshop_name)
    time.sleep(2)
    SelectPrimaryShop = driver.find_element_by_xpath("//span[contains(text(),'Select')]")
    SelectPrimaryShop.click()

    driver.find_element_by_name('score').send_keys(score)
    time.sleep(1)
    driver.find_element_by_name('commission_rate').send_keys(commission)

    driver.find_element_by_name('service').send_keys(express_service)

    Address = driver.find_element_by_id('pac-input')
    Address.send_keys(express_address)
    time.sleep(3)
    Address.send_keys(Keys.ARROW_DOWN)
    Address.send_keys(Keys.ENTER)
    time.sleep(1)
    driver.find_element_by_xpath("//button[contains(text(),'Next')]").click()

    express_shop_config(driver)

    driver.find_element_by_xpath("//button[@type='submit']").click()


