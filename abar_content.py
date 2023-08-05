import requests
from bs4 import BeautifulSoup
import json
import re


def readCookies() -> dict:
    with open('cookies_browser.json', 'r') as file:
        cookies = json.load(file)
    return cookies['Request Cookies']


def writeCookies(cookies: dict) -> None:
    jsonFormat = {'Request Cookies': cookies}
    with open('cookies_browser.json', 'w') as file:
        jsonFormat = json.dumps(jsonFormat)
        file.write(jsonFormat)


def loggin():
    global session
    global document
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

    document = BeautifulSoup(response.text, 'html.parser')
    csrfmiddlewaretoken = document.find('input', type='hidden', attrs={
        'name': 'csrfmiddlewaretoken'})
    csrfmiddlewaretoken = csrfmiddlewaretoken['value']

    for _ in range(5):  # five time try if enter pin code wrong
        pin_code = input(f'Enter SMS that Sended to "{phone}": ')

        # What's wrong, why did you change the phone property to phone_number, Idiot? I was here for ten minutes
        payload = {
            'csrfmiddlewaretoken': csrfmiddlewaretoken,
            'phone_number': phone,
            'next': '/ppanel',
            'pin_code': pin_code
        }
        response = session.post(
            'https://code.abarkelas.ir/ppanel/verify/', data=payload)
        print('='*100)
        print(f'Sended payload is : {payload}')

        document = BeautifulSoup(response.text, 'html.parser')
        if document.find('div', id='tutor_name', class_='center aligned header'):
            print('='*100)
            print('You have Successfully logged in.')
            return True
        else:
            print('='*100)
            print('You are "NOT logged in" You may have entered the code incorrectly')
    return False


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
    status = loggin()
    response = session.get(url=url)
    writeCookies(cookies := session.cookies.get_dict())
    print('='*100)
    print(f'This cookies saved : {cookies}')
    document = BeautifulSoup(response.text, 'html.parser')

tableRows = document.find_all('tr')
tableRows = tableRows[1:]  # Remove header

classes = list()
for tr in tableRows:
    tableData = tr.find_all('td')
    # print(tableData)
    # print('='*50)
    classes.append(Classroom(tableData))

for object in classes:
    print(object.content())
    print('='*100)
