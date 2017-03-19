#!/usr/bin/env python
# -*- coding:utf-8 -*-

import requests

import asyncio
import aiohttp

import jsay

async def fetch(session, url, payload):
    with aiohttp.Timeout(10):
        async with session.get(url, params=payload) as response:
            assert response.status == 200
            return await response.json()

if __name__ == '__main__':
    url = 'http://weather.livedoor.com/forecast/webservice/json/v1'
    payload = {'city': '120010'}
    
    loop = asyncio.get_event_loop()
    with aiohttp.ClientSession(loop=loop) as session:
        json = loop.run_until_complete(fetch(session, url, payload))
        text = json['description']['text']
        speech = text.replace('\n','').replace('\r','').replace(' ','')
        #print(speech)
        jsay.execute(speech)
