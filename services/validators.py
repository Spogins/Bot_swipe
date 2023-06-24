import re
from aiohttp import ClientSession
from configs.settings import API_ROOT


def is_email(text: str):
    patern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    if re.fullmatch(patern, text):
        return True
    else:
        return False


async def check_email(text):
    data = {'email': text}
    async with ClientSession() as session:
        async with session.post(f'{API_ROOT}/api/v1/check_email/check/', data=data) as response:
            email = await response.json()
            return email.get('check')


# trying to get TOKEN`s
async def auth_check(username: str, password: str):
    data = {'username': username, 'password': password}
    async with ClientSession() as session:
        async with session.post(f'{API_ROOT}/api/token/', data=data) as response:
            token = await response.json()
            return token


async def registration(data):
    register_date = {
        "email": f"{data['username']}",
        "password": f"{data['password']}",
        "confirm_password": f"{data['password']}"
    }
    async with ClientSession() as session:
        async with session.post(f'{API_ROOT}/api/registration/builder', data=register_date) as response:
            return await response.json()


def password_check(passwd):
    # reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
    reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d@$!#%*?&]{6,20}$"

    # compiling regex
    pat = re.compile(reg)

    # searching regex
    mat = re.search(pat, passwd)

    # validating conditions
    if not mat:
        return "Password invalid!"
    else:
        return False
