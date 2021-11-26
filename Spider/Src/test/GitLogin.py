import requests
from lxml import etree

username = 'CraHdz'
password = 'Crackerh0507'

def main():
    session = requests.session()
    session.headers = {'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'}
    login(session)
    checkLogin(session)


def login(session):
    global username, password
    url_login = "https://github.com/login"
    url_post = "https://github.com/session"
    try:
        data = session.get(url_login, timeout=5,)
    except Exception as e:
        print("request time out")
        print(e)
    else:
        token = get_token(data.content)
        data_form = {
            'commit': 'Sign in',
            'authenticity_token': token,
            'login': username,
            'password': password,
            'trusted_device':'',
            'webauthn-support': 'supported',
            'webauthn-iuvpaa-support': 'unsupported',
            'return_to': 'https://github.com/login',
            'allow_signup':'',
            'client_id':'',
            'integration':'',
            'required_field_318a':'',
            'timestamp':'1637922009679',
            'timestamp_secret': '441195156cc0cd31de7ffe4bbfcd1b0698e762f1849c6ea26e7276173cbdca28'

         }
        session.post(url_post, data=data_form)

def get_token(data):
    html = etree.HTML(data)
    element = html.xpath('//*[@id="login"]/div[4]/form/input[1]')[0]
    print()
    token = element.xpath('./@value')
    print(token)
    return token;

def checkLogin(session):
    url_check = "https://github.com/CraHdz"
    response = session.get(url_check)
    with open("git.html", 'wb') as file:
        file.write(response.content)


if __name__ == "__main__":
    main()