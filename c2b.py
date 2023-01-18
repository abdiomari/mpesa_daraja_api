import requests
import keys
from requests.auth import HTTPBasicAuth
import json

consumer_key = keys.consumer_key
consumer_secret = keys.consumer_secret
api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"
r = requests.get(api_URL, auth = HTTPBasicAuth(consumer_key, consumer_secret))

# print(r.json())
json_response = r.json()
access_token = json_response["access_token"]
# print(access_token)
access_token = 'access-token'

def register_url():

    api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/registerurl"
    headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer %s' % access_token
    }

    request = {
        "ShortCode": keys.short_code,
        "ResponseType": "Completed",
        "ConfirmationURL": "https://mydomain.com/confirmation",
        "ValidationURL": "https://mydomain.com/validation",
    }

    response = requests.request("POST", api_url, headers = headers, data = request)
    # print(response.text.encode('utf8'))

# register_url()

def simulate_c2b_transaction():
    headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer %s' % access_token
    }
    request = {
        "ShortCode": keys.short_code,
        "CommandID": "CustomerPayBillOnline",
        "amount": "1",
        "MSISDN": keys.test_number,
        "BillRefNumber": "154",
    }
    
    response = requests.request("POST", 'https://sandbox.safaricom.co.ke/mpesa/c2b/v1/simulate', headers = headers, data = request)
    print(response.text.encode('utf8'))

simulate_c2b_transaction()