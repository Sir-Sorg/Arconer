import requests
from bs4 import BeautifulSoup
import json


def readCookies():
    with open('cookies_browser.json', 'r') as file:
        cookies = json.load(file)
    return cookies['Request Cookies']


session = requests.Session()

url = "https://code.abarkelas.ir/ppanel/upcoming/"
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
session.headers.update(headers)

cookies = readCookies()
session.cookies.update(cookies)

response = session.get(url=url)
print(f'Header is : {session.headers}')
print('='*100)
print(f'Sended cookies is : {session.cookies}')

document = BeautifulSoup(response.text, 'html.parser')
print('='*100)
print(document.prettify())

