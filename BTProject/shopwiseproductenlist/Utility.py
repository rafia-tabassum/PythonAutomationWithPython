import json
import pandas as pd
import requests

admin_name = 'ishak'
admin_password = '#121123!'

# admin_name = 'ehealthallaccess'
# admin_password = '#121123!'


def get_data(request_url):
    data = {'username': admin_name, 'password': admin_password}
    r = requests.post('https://beta-erp.evaly.com.bd/auth/login', data=json.dumps(data))
    token = json.loads(r.text)
    token_filter = token['data']
    access_token = token_filter['access_token']
    headers = {'Authorization': 'Bearer ' + str(access_token), 'Content-Type': 'application/json;charset=UTF-8'}
    r = requests.get(request_url, headers=headers)
    json_data = json.loads(r.text)
    # data = json.dumps(json_data, indent=4)
    return json_data


def post_data(request_url, request_body):
    data = {'username': admin_name, 'password': admin_password}
    r = requests.post('https://beta-erp.evaly.com.bd/auth/login', data=json.dumps(data))
    token = json.loads(r.text)
    token_filter = token['data']
    access_token = token_filter['access_token']
    headers = {'Authorization': 'Bearer ' + str(access_token), 'Content-Type': 'application/json;charset=UTF-8'}
    r = requests.post(request_url, data=request_body, headers=headers)
    # r = requests.get(request_url, headers=headers)
    json_data = json.loads(r.text)
    # data = json.dumps(json_data, indent=4)
    return json_data


def put_data(request_url, request_body):
    data = {'username': admin_name, 'password': admin_password}
    r = requests.post('https://beta-erp.evaly.com.bd/auth/login', data=json.dumps(data))
    token = json.loads(r.text)
    token_filter = token['data']
    access_token = token_filter['access_token']
    headers = {'Authorization': 'Bearer ' + str(access_token)}
    r = requests.put(request_url, data=request_body, headers=headers)
    # r = requests.get(request_url, headers=headers)
    json_data = json.loads(r.text)
    # data = json.dumps(json_data, indent=4)
    return json_data


def shop_csv_file_read():
    df = pd.read_csv(
        f'https://docs.google.com/spreadsheets/d/1igzYLzyOwt9UdKWf-KfmkpzBdKX5lTTj7sSv4ksXiwI/export?format=csv')
    return df


def shop_csv_file_write():
    df = pd.to_csv(
        f'https://docs.google.com/spreadsheets/d/1igzYLzyOwt9UdKWf-KfmkpzBdKX5lTTj7sSv4ksXiwI/edit?format=csv')
    return df


def shop_csv():
    df = pd.read_csv(r"E:\Pythonproj\BTProject\shopwiseproductenlist\Shop.csv", header=None)
    return df


def approved_shop_csv():
    df = pd.read_csv(r"E:\Pythonproj\BTProject\shopwiseproductenlist\ShopStatus.csv", header=None)
    return df


# def product_csv():
#     df = pd.read_csv(r"D:\Programming\file\Product.csv", header=None)
#     return df

