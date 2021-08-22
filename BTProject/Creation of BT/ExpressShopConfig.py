

min_quantity= 1
min_amount = 300
max_quantity = 200
max_amount = 3400000

def express_shop_config(driver):
    driver.find_element_by_name('is_delivery_hero_allowed').click()
    driver.find_element_by_name('is_cod_allowed').click()

    MinQuantity = driver.find_element_by_name('min_order_quantity')
    MinQuantity.send_keys(min_quantity)

    MaxQuantity = driver.find_element_by_name('max_order_quantity')
    MaxQuantity.send_keys(max_quantity)

    MinAmount = driver.find_element_by_name('min_order_amount')
    MinAmount.send_keys(min_amount)

    MaxAmount = driver.find_element_by_name('max_order_amount')
    MaxAmount.send_keys(max_amount)