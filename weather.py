#!/usr/bin/env python
# -*- coding:utf-8 -*-

import requests
import jsay

json_url = 'http://weather.livedoor.com/forecast/webservice/json/v1'
# 地域コード 千葉県
payload = {'city': '120010'}

# キーワード引数
response = requests.get(json_url, params=payload)
json = response.json()
text = json['description']['text']

speech = text.replace('\n','').replace('\r','').replace(' ','')

#print(speech)
#jsay.execute('こんばんは')
jsay.execute(speech)
