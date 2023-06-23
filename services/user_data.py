from datetime import datetime

import bcrypt
from aiohttp import ClientSession

from configs.settings import COLLECTION, API_ROOT, COLLECTION_ADV



async def add_user(user_id, data):
    date = datetime.now().date()
    password = data['password']
    password = password.encode('utf-8')
    hashed = bcrypt.hashpw(password, bcrypt.gensalt(10))
    COLLECTION.insert_one({
        '_id': user_id,
        'date': str(date),
        'email': data['email'],
        'password': hashed,
        'access_token': data['access'],
        'refresh_token': data['refresh']
    })


async def add_adv(user_id, adv_id, location, scheme):
    date = datetime.now().date()
    COLLECTION_ADV.insert_one({
        '_id': adv_id,
        'date': str(date),
        'user': user_id,
        'location': location,
        'scheme': scheme,
    })


async def update_token(user_id, data):
    COLLECTION.update_one({'_id': user_id}, {'$set': {'access_token': data['access'],
                                                      'refresh_token': data['refresh']}})


async def get_user(user_id):
    if COLLECTION.find_one({'_id': user_id}):
        return COLLECTION.find_one({'_id': user_id})
    else:
        return False


async def get_new_token(user_id):
    if COLLECTION.find_one({'_id': user_id}):
        user = COLLECTION.find_one({'_id': user_id})
        data = {
            "refresh": f"{user['refresh_token']}"
        }
        async with ClientSession() as session:
            async with session.post(f'{API_ROOT}/api/token/refresh/', data=data) as response:
                token = await response.json()
        await update_token(user_id, token)
        return True
    else:
        return False


async def get_adv(flat_id, user_id):
    await get_new_token(user_id)
    user = await get_user(user_id)
    async with ClientSession() as session:
        async with session.get(
            url=f'{API_ROOT}/api/v1/flat/{flat_id}/',
            headers={
                'Authorization': f'Bearer {user.get("access_token")}',
            },
        ) as response:
            _json = await response.json()
            return _json





