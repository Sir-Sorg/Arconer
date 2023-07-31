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
        context = f'کلاس تدریس {self.subject} دانش آموز محترم {self.name} برگزار شد و در ساعت {self.time} تاریخ {self.date} به اتمام رسید و کلیه مطالب مشخص شده به خوبی آموزش دیده شد.'
        return context


session = requests.Session()

url = "https://code.abarkelas.ir/ppanel/upcoming/"
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
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
