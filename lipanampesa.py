import base64
from datetime import datetime
# from urllib.request import HTTPBasicAuthHandler


import requests
from requests.auth import HTTPBasicAuth

import keys


# gen timestamp

# print(datetime.now())
# 2023-01-09 19:40:08.611633  ~ 20230109194008 
unformatted_time = datetime.now()
formattedtime = unformatted_time.strftime("%Y%m%d%H%M%S")
# print(formattedtime)

# password generator
data_to_encode = keys.business_shortcode + keys.lipa_na_mpesa_passkey + formattedtime
encoded = base64.b64encode(data_to_encode.encode())
# print(encoded)

decoded = encoded.decode('utf-8')

# print(decoded)

consumer_key = keys.consumer_key
consumer_secret = keys.consumer_secret
api_url = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"
r = requests.get(api_url,  auth=HTTPBasicAuth(consumer_key, consumer_secret))
# r= requests.request("GET", api_url)
print(r.json())
json_response = r.json()
access_token = json_response['access_token']

def lipa_na_mpesa():
        
    # access_token = access_token
    api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
    headers ={"Authorization" : "Bearer %s" % access_token}

    request = {
        "BusinessShortCode":keys.business_shortcode,    
        "Password": decoded,    
        "Timestamp":formattedtime,    
        "TransactionType": "CustomerPayBillOnline",    
        "Amount":"1",    
        "PartyA":keys.phone_number,    
        "PartyB":keys.business_shortcode,    
        "PhoneNumber":keys.phone_number,    
        "CallBackURL":"https://fullstackdjango.com/lipanampesa/",    
        "AccountReference":"Test1",    
        "TransactionDesc":"Test1"
    }

    response = requests.post(api_url, json=request, headers = headers)
    print(response.text)

lipa_na_mpesa()