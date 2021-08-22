import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

option1 = Options()
option1.add_argument("--disable-notifications")

# 1. Creating Driver object
driver = webdriver.Chrome(executable_path="E:\Pythonproj\chromedriver.exe", chrome_options=option1)
# driver = webdriver.Firefox(executable_path="E:\Pythonproj\geckodriver.exe")
# driver = webdriver.Ie(executable_path="E:\Pythonproj\IEDriverServer.exe")
driver.maximize_window()
# 2. Opening url on the browser
driver.get("https://admin-dev.evaly.com.bd/auth/login")

print(driver.title)  # Will get Title of the page
print(driver.current_url) # Capturing current url of the page

Userid = driver.find_element_by_xpath("//*[@id='root']/div/section/form/label[1]/input")
Userid.send_keys("rafia")

Password = driver.find_element_by_xpath("//*[@id='root']/div/section/form/label[2]/input")
Password.send_keys("#121123!")

Loginbtn = driver.find_element_by_xpath("//*[@id='root']/div/section/form/div/button")
Loginbtn.click()
time.sleep(5)

Product = driver.find_element_by_xpath("//*[@id='sidebar-nav']/div/div[1]/ul/li[8]/div/p")
Product.click()
time.sleep(1)

subProducts = driver.find_element_by_xpath("//*[@id='sidebar-nav']/div/div[1]/ul/ul[5]/li[1]/a/div/p")
subProducts.click()
time.sleep(2)

createproduct = driver.find_element_by_xpath("//*[@id='root']/div/div[3]/div/div/div[2]/div/button")
createproduct.click()

file_path = '/data/product1.jpg'


img = driver.find_element_by_xpath("//*[@id='root']/div/div[3]/div/div/div[2]/div/form/div/div[2]/div/span/svg")
img.click()

# print(driver.page_source) # Current Page source
# driver.close()