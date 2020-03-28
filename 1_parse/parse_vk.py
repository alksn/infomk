

import lxml.html
import requests
import time
import pickle


login = ''
password = ''
url = 'https://vk.com/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'ru-ru,ru;q=0.8,en-us;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate',
    'Connection': 'keep-alive',
    'DNT': '1'
}


session = requests.session()
data = session.get(url, headers=headers)
page = lxml.html.fromstring(data.content)

form = page.forms[0]
form.fields['email'] = login
form.fields['pass'] = password

response = session.post(form.action, data=form.form_values())
print('onLoginDone' in response.text)

with open('./session.bin', 'wb') as f:
    pickle.dump(session, f)

with open("./session.bin", "rb") as f:
    session = pickle.load(f)


# человек сначала переходит на основной сайт, но здесь не обязательно
# response1 = session.get('https://bkstat.vip/', headers=headers)
# time.sleep(1.2)

response = session.get('https://bkstat.vip/auth/vk', headers=headers)
print(response.url)     # url после всех 302-х редиректов
time.sleep(1.2)

data = {"pageSize": 5, "page": 0, "sorted": [], "filtered": []}

# не обязательный запрос-проверка
#r1 = requests.post('https://bkstat.vip/auth/vk/ismember', headers=headers, data={"groupId": '142104089', "userId": '22406085'})

headers['Cookie'] = response.request.headers._store['cookie'][1]
r = requests.post('https://bkstat.vip/api/mk/stat', headers=headers, data=data)

print(r.text)


