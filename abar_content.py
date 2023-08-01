import requests
from bs4 import BeautifulSoup
import json
import re


def readCookies():
    with open('cookies_browser.json', 'r') as file:
        cookies = json.load(file)
    return cookies['Request Cookies']


class Classroom:
    def __init__(self, tableDatas) -> None:
        self.name = tableDatas[1].get_text(strip=True)
        dateTime = tableDatas[0].find('div').get_text(strip=True)
        self.date = re.findall('.{2}\/.{2}\/.{2}', dateTime)[0]  # Find Date
        self.time = re.findall('.{2}:.{2}$', dateTime)[
            0]  # Find finishing time
        tableDatas[0].div.decompose()
        self.subject = tableDatas[0].get_text(strip=True)

    def content(self):
        context = f'کلاس تدریس {self.subject} دانش آموز محترم {self.name} برگزار شد و در ساعت {self.time} تاریخ {self.date} به اتمام رسید و کلیه مطالب مشخص شده آموزش دیده شد.'
        return context


session = requests.Session()

url = "https://code.abarkelas.ir/ppanel/upcoming/"
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
    "Origin": "https://code.abarkelas.ir"}
session.headers.update(headers)

cookies = readCookies()
session.cookies.update(cookies)

response = session.get(url=url)
print('='*100)
print(f'Header is : {session.headers}')
print('='*100)
print(f'Sended cookies is : {session.cookies}')

document = BeautifulSoup(response.text, 'html.parser')
print('='*100)
# print(document.prettify())

if document.find('input', type='text', attrs={"name": "phone"}):
    phone = '09391375798'
    print(f'Cookies was Expierd re-Enter Begining...\nSMS sends to "{phone}"')
    # B*tchs, you only used one input to verify your identity, you have to reach us
    csrfmiddlewaretoken = document.find('input', type='hidden', attrs={
        'name': 'csrfmiddlewaretoken'})
    csrfmiddlewaretoken = csrfmiddlewaretoken['value']
    payload = {'csrfmiddlewaretoken': csrfmiddlewaretoken,
               'phone': phone,
               'next': '/ppanel'}
    response = session.post(
        'https://code.abarkelas.ir/ppanel/login/', data=payload)
    with open('s.html', 'w') as f:
        f.write(response.text)
    print(response.text)

tableRows = document.find_all('tr')
tableRows = tableRows[1:]  # Remove header

classes = list()
for tr in tableRows:
    tableData = tr.find_all('td')
    print(tableData)
    print('='*50)
    classes.append(Classroom(tableData))

for object in classes:
    print(object.content())
    print('='*100)
