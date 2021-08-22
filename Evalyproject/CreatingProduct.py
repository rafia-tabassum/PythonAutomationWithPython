import csv
import time
import autoit
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

option1 = Options()
option1.add_argument("--disable-notifications")
with open('info.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    driver = webdriver.Chrome(executable_path="E:\Pythonproj\chromedriver.exe", options=option1)
    driver.get("https://admin-dev.evaly.com.bd/auth/login")
    driver.maximize_window()

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
    for i, line in enumerate(csv_reader):

        createproduct = driver.find_element_by_xpath("//*[@id='root']/div/div[3]/div/div/div[2]/div/button")
        createproduct.click()
        time.sleep(2)

        productname = driver.find_element_by_xpath("//*[@id='root']/div/div[3]/div/div/div[2]/div/form/div/div[1]/div[1]/label[1]/input")
        productname.send_keys(line[0])
        time.sleep(3)

        image = driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div/div/div[2]/div/form/div/div[2]/div/span")
        image.click()
        time.sleep(5)

        if i == 0:
            autoit.run("FileUpload.exe")
        elif i == 1:
            autoit.run("FileUpload1.exe")
        time.sleep(5)
        proddescription = driver.find_element_by_xpath("//*[@id='root']/div/div[3]/div/div/div[2]/div/form/div/div[1]/div[1]/label[2]/textarea")
        proddescription.send_keys(line[1])

        tags = driver.find_element_by_name("tags")
        tags.send_keys(line[2])
        tags.send_keys(Keys.ENTER)
        time.sleep(2)

        score = driver.find_element_by_name("score")
        score.clear()
        score.send_keys(line[3])

        category = driver.find_element_by_xpath("//*[@id='root']/div/div[3]/div/div/div[2]/div/form/div/div[1]/div[2]/div[1]/div/div/label/input")
        category.send_keys(line[4])
        time.sleep(3)
        categoryselectbtn = driver.find_element_by_xpath("//button[contains(text(),'Select')]")
        categoryselectbtn.click()
        time.sleep(3)

        brand = driver.find_element_by_xpath("//*[@id='root']/div/div[3]/div/div/div[2]/div/form/div/div[1]/div[2]/div[2]/div/label/input")
        brand.send_keys(line[5])
        time.sleep(3)
        brandselect = driver.find_element_by_xpath("//*[@id='1608726572']")
        brandselect.click()

        specification_name = driver.find_element_by_xpath("//*[@id='root']/div/div[3]/div/div/div[2]/div/form/div/div[1]/div[3]/div/div/div[1]/label/input")
        specification_name.send_keys(line[6])

        specification_value = driver.find_element_by_xpath("//*[@id='root']/div/div[3]/div/div/div[2]/div/form/div/div[1]/div[3]/div/div/div[2]/label/input")
        specification_value.send_keys(line[7])

        submitform=driver.find_element_by_xpath("//button[@type='submit']")
        submitform.submit()
        time.sleep(3)

        # createvariant = driver.find_element_by_xpath("/html/body/reach-portal[2]/div/div/footer/div/button[1]") // Yes
        if i==0:
            createvariant = driver.find_element_by_xpath("/html/body/reach-portal[2]/div/div/footer/div/button[2]")
            createvariant.click()
            time.sleep(5)

        elif i==1:
            createvariant = driver.find_element_by_xpath("/html/body/reach-portal[2]/div/div/footer/div/button[1]")
            createvariant.click()
            time.sleep(4)

            editioncreate = driver.find_element_by_xpath("//*[@id='root']/div/div[3]/div/div/div[2]/div[1]/div/p")
            editioncreate.click()
            time.sleep(2)

            searchoption = driver.find_element_by_xpath("//input[@placeholder = 'Search Attributes..']")
            searchoption.click()
            # searchoption.send_keys(line[8])
            time.sleep(3)

            selecteditionoption = driver.find_element_by_xpath("//input[@class= 'form-checkbox']")
            selecteditionoption.click()
            time.sleep(2)

            btnnext = driver.find_element_by_xpath("//button[contains(text(),'Next')]")
            btnnext.click()
            time.sleep(4)

    driver.close()