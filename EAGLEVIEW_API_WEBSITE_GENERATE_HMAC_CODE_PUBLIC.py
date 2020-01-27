import hmac
import os
import requests
import hashlib
import time
import calendar

##This script makes no assumptions about how you store your keys, and the variables are just placeholders
##Would not recommend storing plain text in the script in real life, use environmental variables or something

api_key = "YOUR_API_KEY"
ts = calendar.timegm(time.gmtime())

api_key_with_timestamp = api_key + str(ts)
api_key_with_timestamp = api_key_with_timestamp.encode()

secret_key = 'YOUR_SECRET_KEY'.encode()

auth_signature = hmac.new(secret_key, api_key_with_timestamp, hashlib.md5).hexdigest()

auth_request_url = f"https://pol.pictometry.com/Gateway/v1/authenticate/{api_key}/{ts}/{auth_signature}"

auth_r = requests.get(auth_request_url)
auth_status_code = auth_r.status_code

print(auth_status_code)

if auth_status_code == 200:
    auth_response_json = auth_r.json()
    auth_token = auth_response_json['response']['token']
    print(auth_token) ## Print for test only, to be sure everything work, don't do this when running the script for real