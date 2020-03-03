import json
import httplib
import base64


 
# get accesson token
import requests 
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=5qXyDFPNwL0BdCrH3kkCK9Ml&client_secret=3a36271d89acf5eed76481727910b68c'
response_str = requests.get(host)
if response_html_str:
    print(response_str.json())
    
    
access_token=response_str.json().get('access_token')

# test asr 
f=open('8k.amr','rb')
data=f.read(6340)

speech=base64.b64encode(data)
length=6340
params={'format':"amr","rate":8000,"channel":1,"cuid":"eps32","token":access_token,"speech":speech,"len":length}
a=json.dumps(params)
print a
conn = httplib.HTTPConnection("vop.baidu.com",80)
conn.request("GET","/server_api",a)
response=conn.getresponse()
# print response.status,response.reason
print response.read()