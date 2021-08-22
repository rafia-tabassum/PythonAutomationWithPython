import time

from Utility import chrome_driver, bt_login
from MerchantCreate import create_merchant
from ExpressShopCreate import create_express_shop
from PrimaryShopCreate import create_primaryshop

driver = chrome_driver()

driver.get("https://beta-erp.evaly.com.bd/auth/login")
driver.maximize_window()

bt_login(driver)
time.sleep(5)
# create_merchant(driver)
# create_express_shop(driver)
create_primaryshop(driver)
# driver.close()