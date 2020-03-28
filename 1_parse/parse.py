


import json
import lxml.html
import requests
import time
import pickle
import os


headers = {}

session = requests.session()
with open("./session.bin", "rb") as f:
    session = pickle.load(f)


response = session.get('https://bkstat.vip/auth/vk', headers=headers)
print(response.url)     # url после всех 302-х редиректов
time.sleep(1.2)

data = {"pageSize": 15000, "page": 1000, "sorted": [], "filtered": []}
headers['Cookie'] = response.request.headers._store['cookie'][1]

r = requests.post('https://bkstat.vip/api/mk/stat', headers=headers, data=data)
page = json.loads(r.text)
print(r.url)

pages = page['pages']
print(pages)


with open('./stat/stat.txt', 'w') as output_file:    # пересоздание, очистка файла
    output_file.write('')

for i in range(0, pages):

    time.sleep(2.1)
    print(i)

    data['page'] = i
    r = requests.post('https://bkstat.vip/api/mk/stat', headers=headers, data=data)


    with open('./stat/stat.txt', 'a', encoding='utf8') as file:
        file.write(r.text + '\n')

