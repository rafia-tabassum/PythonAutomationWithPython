import random
import string
import time
import pyautogui
import autoit
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

merchant_name = "Dan Company"

def create_merchant(driver):
    time.sleep(4)
    clickonmerchant = driver.find_element_by_xpath("//div/h4[contains(text(),'Merchant')]")
    clickonmerchant.click()

    time.sleep(2)
    createmerchant = driver.find_element_by_xpath("//span[contains(text(),'Create Merchant')]")
    createmerchant.click()
    time.sleep(2)

    image = driver.find_element_by_xpath("//span[contains(text(),'Choose file')]")
    image.click()
    time.sleep(2)
    pyautogui.write(r"C:\Users\ASUS\Downloads\banner.jpg")
    pyautogui.press('enter')
    time.sleep(2)
    uploadimage = driver.find_element_by_xpath("//button[contains(text(),'Upload Now')]")
    uploadimage.click()
    time.sleep(2)
    applycrop = driver.find_element_by_xpath("//span[contains(text(),'Apply Crop')]")
    applycrop.click()
    time.sleep(2)

    merchantname = driver.find_element_by_xpath("//input[@name='merchant_name']")
    merchantname.send_keys(merchant_name+ ''.join(random.choice(string.digits) for _ in range(2)))

    type = driver.find_element_by_xpath("//select[@name='merchant_type']")
    sel = Select(type)
    sel.select_by_index(2)

    cphonenumber = '019' + ''.join(random.choice(string.digits) for _ in range(8))
    companyphonenumber = driver.find_element_by_xpath("//input[@name='merchant_phone_no']")
    companyphonenumber.send_keys(cphonenumber)

    merchantemail = driver.find_element_by_xpath("//input[@name='merchant_email']")
    merchantemail.send_keys('merchant'+ ''.join(random.choice(string.digits) for _ in range(3)) + '@evaly.com.bd')

    merchantaddress = driver.find_element_by_xpath("//input[@name='merchant_address']")
    merchantaddress.send_keys("House-1, Road-13, Dhanmondi")

    ownerfirstname = driver.find_element_by_xpath("//input[@name='owner_first_name']")
    ownerfirstname.send_keys("Asma-ul")

    ownerlastname = driver.find_element_by_xpath("//input[@name='owner_last_name']")
    ownerlastname.send_keys("Husna")

    phonenumber = '019'+''.join(random.choice(string.digits) for _ in range(8))
    owner = driver.find_element_by_xpath("//input[@name='owner']")
    owner.send_keys(phonenumber)

    email = 'owner' + ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(3)) + '@evaly.com.bd'
    owneremail = driver.find_element_by_xpath("//input[@name='owner_email']")
    owneremail.send_keys(email)

    ownernid = driver.find_element_by_xpath("//input[@name='owner_nid_no']")
    ownernid.send_keys("155867333222")

    merchanttradelicense = driver.find_element_by_xpath("//input[@name='merchant_trade_license_no']")
    merchanttradelicense.send_keys("134577754554")

    selectdate = driver.find_element_by_xpath("//input[@type='date']")
    selectdate.send_keys("10/28/2021")
    time.sleep(2)

    time.sleep(1)
    nidfrontimage = driver.find_element_by_xpath("/html/body/div[1]/section[2]/div[2]/div/div[2]/div/div/form/div/div[2]/div/div[8]/label/div/div")
    nidfrontimage.click()
    time.sleep(2)
    pyautogui.write(r"C:\Users\ASUS\Downloads\front.jpg")
    pyautogui.press('enter')
    time.sleep(1)

    nidbackimage = driver.find_element_by_xpath("/html/body/div[1]/section[2]/div[2]/div/div[2]/div/div/form/div/div[2]/div/div[9]/label/div/div")
    nidbackimage.click()
    time.sleep(2)
    pyautogui.write(r"C:\Users\ASUS\Downloads\back.jpg")
    pyautogui.press('enter')
    time.sleep(2)

    submitmerchant = driver.find_element_by_xpath("//button[@type='submit']")
    submitmerchant.click()
    time.sleep(6)

    click_merchant_name = driver.find_element_by_xpath("/html/body/div[1]/section[2]/div[2]/div/section/div/div[1]/div[2]/h3/a")
    print(click_merchant_name.text)
    # click_merchant_name.click()
    # create_primaryshop = driver.find_element_by_xpath("//*[@id='__next']/section[2]/div[1]/div[2]/span[1]/button")
    # create_primaryshop.click()
    # create_primaryshop(driver)


