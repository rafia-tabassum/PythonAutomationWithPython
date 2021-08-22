import csv
import random
import string
import time

import autoit
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

option1 = Options()
option1.add_argument("--disable-notifications")

csv_reader = pd.read_csv(r'campaign.csv')
total_row = csv_reader.shape[0]

description = csv_reader['Description'].tolist()
campaignname = csv_reader['Campaign_Name'].tolist()
score = csv_reader['Score'].tolist()
category = csv_reader['Category'].tolist()
cashbackpercentage = csv_reader['Cashback_Percentage'].tolist()
campaignstart = csv_reader['Campaign_Start_Date'].tolist()
campaignend = csv_reader['Campaign_End_Date'].tolist()
promotionstart = csv_reader['Promotion_Start_Date'].tolist()
prmotionend = csv_reader['Promotion_End_Date'].tolist()
cashbackdestination = csv_reader['Cashback_Destination'].tolist()
amountperbdt = csv_reader['Amount_Per_BDT'].tolist()
userscore = csv_reader['User_Score'].tolist()
minorderquantity = csv_reader['Min_Order_Quantity'].tolist()
minorderamount = csv_reader['Min_Order_Amount'].tolist()
maxorderquantity = csv_reader['Max_Order_Quantity'].tolist()
maxorderamount = csv_reader['Max_Order_Amount'].tolist()
editbefore = csv_reader['Edit_Before'].tolist()


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

# sidemenu = driver.find_element_by_xpath("//*[@id='__next']/div[1]/div[1]/button")
# sidemenu.click()
# time.sleep(2)

clickoncampaign = driver.find_element_by_xpath("//*[@id='__next']/section/section/div/ul/li[4]/a")
clickoncampaign.click()
# time.sleep(2)

clickallcampaign = driver.find_element_by_xpath("//*[@id='__next']/section/section/div/ul/li[4]/ul/li[1]")
clickallcampaign.click()
time.sleep(2)

for i in range(total_row):

        createcampaign = driver.find_element_by_xpath("//span[contains(text(),'Create Campaign')]")
        createcampaign.click()
        time.sleep(2)

        image = driver.find_element_by_xpath("//span[contains(text(),'Choose file')]")
        image.click()
        time.sleep(3)

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

        uploadbanner = driver.find_element_by_xpath("//*[@id='drop-area_image']/label")
        uploadbanner.click()
        time.sleep(3)

        if i == 0:
            autoit.run("E:\Pythonproj\BTProject\campaignbanner\FileUpload.exe")
        elif i == 1:
            autoit.run("E:\Pythonproj\BTProject\campaignbanner\FileUpload1.exe")
        time.sleep(2)

        Description = driver.find_element_by_xpath("//textarea[@name='description']")
        Description.send_keys(description[i])

        CampaignName = driver.find_element_by_xpath("//input[@name='name']")
        CampaignName.send_keys(campaignname[i] + ''.join(random.choice(string.digits) for _ in range(2)))
        # time.sleep(2)

        # scorerandom = ''.join(random.choice(string.digits) for _ in range(2))
        Score = driver.find_element_by_xpath("//input[@name='score']")
        Score.click()
        Score.send_keys(Keys.BACKSPACE)
        # time.sleep(2)
        Score.send_keys(str(score[i]))
        Score.send_keys(Keys.BACKSPACE)
        Score.send_keys(Keys.BACKSPACE)

        Category = driver.find_element_by_xpath("//select[@name='category']")
        Category.send_keys(category[i])
        # sel = Select(category)
        # if i == 0:
        #     sel.select_by_index(1)
        # elif i ==1:
        #     sel.select_by_index(2)
        # time.sleep(2)

        CashbackPercentage = driver.find_element_by_xpath("//input[@name='cashbackPercentage']")
        CashbackPercentage.send_keys(str(cashbackpercentage[i]))
        CashbackPercentage.send_keys(Keys.BACKSPACE)
        CashbackPercentage.send_keys(Keys.BACKSPACE)

        allowedpayment = driver.find_element_by_xpath("//*[@id='__next']/section/div/div[2]/form/div/div[2]/div/div[1]/label/label[1]/input")
        allowedpayment.click()

        cashbackfor = driver.find_element_by_xpath("//*[@id='__next']/section/div/div[2]/form/div/div[2]/div/div[2]/label/label[1]/input")
        cashbackfor.click()

        CampaignStart = driver.find_element_by_xpath("//*[@id='__next']/section/div/div[2]/form/div/div[2]/div/div[3]/label/div/input")
        CampaignStart.send_keys(campaignstart[i])

        CampaignEnd = driver.find_element_by_xpath("//*[@id='__next']/section/div/div[2]/form/div/div[2]/div/div[4]/label/div/input")
        CampaignEnd.send_keys(campaignend[i])

        PromotionStart = driver.find_element_by_xpath("//*[@id='__next']/section/div/div[2]/form/div/div[2]/div/div[5]/label/div/input")
        PromotionStart.send_keys(promotionstart[i])

        PromotionEnd = driver.find_element_by_xpath("//*[@id='__next']/section/div/div[2]/form/div/div[2]/div/div[6]/label/div/input")
        PromotionEnd.send_keys(prmotionend[i])

        Div = driver.find_element_by_xpath("//*[@id='__next']/section/div/div[2]/form/div/div[2]")
        Div.click()
        # time.sleep(3)

        CashbackType = driver.find_element_by_xpath("//input[@value='instant']")
        CashbackType.click()

        CashbackDestination = driver.find_element_by_xpath("//select[@name='cashBackDestination']")
        CashbackDestination.send_keys(cashbackdestination[i])

        EnableUserScore = driver.find_element_by_xpath("//*[@id='__next']/section/div/div[2]/form/div/div[2]/div/div[9]/label/input")
        EnableUserScore.click()

        AmountperBDT = driver.find_element_by_xpath("//input[@name='userScorePerBdt']")
        AmountperBDT.send_keys(str(amountperbdt[i]))
        AmountperBDT.send_keys(Keys.BACKSPACE)
        AmountperBDT.send_keys(Keys.BACKSPACE)

        UserScore = driver.find_element_by_xpath("//input[@name='userScorePoint']")
        UserScore.send_keys(str(userscore[i]))
        UserScore.send_keys(Keys.BACKSPACE)
        UserScore.send_keys(Keys.BACKSPACE)

        Submit = driver.find_element_by_xpath("//span[contains(text(), 'Submit')]")
        Submit.click()
        # time.sleep(3)

        SubmitBtn = driver.find_element_by_xpath("/html/body/reach-portal[1]/div/div/div/section[2]/div/div[3]/div/button")
        SubmitBtn.click()

        MinOrderQuantity = driver.find_element_by_xpath("//input[@name='min_order_quantity']")
        MinOrderQuantity.click()
        MinOrderQuantity.send_keys(Keys.BACKSPACE)
        # time.sleep(2)
        MinOrderQuantity.send_keys(str(minorderquantity[i]))
        MinOrderQuantity.send_keys(Keys.BACKSPACE)
        MinOrderQuantity.send_keys(Keys.BACKSPACE)

        MinOrderAmount = driver.find_element_by_xpath("//input[@name='min_order_amount']")
        MinOrderAmount.click()
        MinOrderAmount.send_keys(Keys.BACKSPACE)
        # time.sleep(2)
        MinOrderAmount.send_keys(str(minorderamount[i]))
        MinOrderAmount.send_keys(Keys.BACKSPACE)
        MinOrderAmount.send_keys(Keys.BACKSPACE)

        MaxOrderQuantity = driver.find_element_by_xpath("//input[@name='max_order_quantity']")
        MaxOrderQuantity.click()
        MaxOrderQuantity.send_keys(Keys.BACKSPACE)
        MaxOrderQuantity.send_keys(str(maxorderquantity[i]))
        MaxOrderQuantity.send_keys(Keys.BACKSPACE)
        MaxOrderQuantity.send_keys(Keys.BACKSPACE)

        MaxOrderAmount = driver.find_element_by_xpath("//input[@name='max_order_amount']")
        MaxOrderAmount.click()
        MaxOrderAmount.send_keys(Keys.BACKSPACE)
        # time.sleep(2)
        MaxOrderAmount.send_keys(str(maxorderamount[i]))
        MaxOrderAmount.send_keys(Keys.BACKSPACE)
        MaxOrderAmount.send_keys(Keys.BACKSPACE)

        EditBefore = driver.find_element_by_xpath("//input[@name='edit_before']")
        EditBefore.click()
        time.sleep(2)
        # SelectTime = driver.find_element_by_xpath("/html/body/reach-portal[2]/div/div/div/section[2]/div/div[1]/div[5]/label/div[2]/div/div/div[1]/div[2]/div[1]/svg/g/circle[2]")
        # SelectTime.click()
        # time.sleep(2)
        # SelectPM = driver.find_element_by_xpath("/html/body/reach-portal[2]/div/div/div/section[2]/div/div[1]/div[5]/label/div[2]/div/div/div[1]/div[2]/div[2]/button[2]")
        # SelectPM.click()
        # time.sleep(2)
        EditBefore.send_keys(Keys.CONTROL, "a")
        EditBefore.send_keys(Keys.BACKSPACE)
        time.sleep(2)
        EditBefore.send_keys(editbefore[i])

        click = driver.find_element_by_xpath("/html/body/reach-portal[2]/div/div/div/section[2]/div/div[1]/div[5]/label/div[2]/div/div/div[1]/div[1]")
        click.click()

        ConfigSubmit = driver.find_element_by_xpath("//div[@class='ml-3']|div/button[@type='submit']")
        ConfigSubmit.click()
print("Campaign Created Successfully")
# driver.close()