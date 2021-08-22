import json

from Utility import post_data
from Utility import shop_csv_file_read
import pandas as pd
import time

df = shop_csv_file_read()

requests_url = 'https://api-dev.evaly.com.bd/evaly-merchant-api/api/v1/admin/shops/express-shop/'  # Create Category API URL
# df.to_csv(r"D:\Programming\file\Category.csv", index=False, header='Id, Name, Slug, Status, Approved, Department',
#           mode='a')

for i in range(0, 3):
    shop_name = "Shop Name" + str(i)
    request_body = {
        "name": shop_name,
        "image_url": "https://s3-ap-southeast-1.amazonaws.com/media.evaly.com.bd/media/images/63d8dc9191ba-whatsapp-image-2021-06-15-at-55848-pm-1.jpeg",
        "department": 13
    }
    data = post_data(requests_url, json.dumps(request_body))
    print(data)
    shop_slug = data['mother_shop_slug']
    shop_name = data['name']
    shop_address = data['address']
    shop_image = data['logo_image']
    product_status = data['status']
    category_status = data['approved']
    df = pd.DataFrame([[product_id, product_name, product_slug, product_status, category_status, product_department]],
                      columns=['Id', 'Name', 'Slug', 'Status', 'Approved', 'Department'])

    df.to_csv(r"E:\Pythonproj\BTProject\shopwiseproductenlist\Shop.csv", index=False, header=False, mode='a')
    print("Write Successful data === " + str(i + 1))
    time.sleep(2)
