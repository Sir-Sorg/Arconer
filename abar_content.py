import requests
import json


def readCookies():
    with open('cookies_browser.json', 'r') as cookies:
        cookiesDict = json.load(cookies)
    return cookiesDict['Request Cookies']


session = requests.Session()

url = "https://code.abarkelas.ir/ppanel/upcoming/"
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
session.headers.update(headers)

cookies = readCookies()
session.cookies.update(cookies)

response = session.get(url=url)
print(session.headers)
print(session.cookies)
with open('s.html', 'w') as t:
    t.write(str(response.text))
